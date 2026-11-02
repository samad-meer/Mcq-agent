@echo off
rem Sets up the MCQ agent on a Windows 10 or 11 PC. Run it once, by double-clicking it or from a
rem terminal, with the internet connected. It installs Python 3.13 for your user account if the PC
rem does not have it (no admin rights needed), creates the .venv folder, installs the tested package
rem versions, and saves your Gemini API key on this PC. After it finishes, use run.bat.
setlocal EnableDelayedExpansion
cd /d "%~dp0"
set "PYVER=3.13.3"
set "ARCH=amd64"
if /i "%PROCESSOR_ARCHITECTURE%"=="ARM64" set "ARCH=arm64"
set "FAILED="

echo.
echo === MCQ agent setup ===
echo.

call :find_python
if not defined PY (
    echo Python 3.13 was not found on this PC, so it will be installed for your user account.
    call :install_python || goto :fail
    call :find_python
    if not defined PY (
        echo Python was installed, but this window cannot see it yet. Close this window and run setup.bat again.
        goto :fail
    )
)
echo Using Python: !PY!

if not exist ".venv\Scripts\python.exe" (
    echo Creating the virtual environment...
    "!PY!" -m venv .venv || goto :fail
)
echo Installing the tested package versions. This takes a minute...
".venv\Scripts\python.exe" -m pip install --disable-pip-version-check -q -r requirements.txt || goto :fail
".venv\Scripts\python.exe" -c "import mss, openai, pyautogui, PIL, pydantic" || goto :fail
echo Packages installed.

call :find_key
if not defined GEMINI_API_KEY (
    echo.
    echo You need your own free Gemini API key. Get one at https://aistudio.google.com/apikey
    echo It is saved on this PC only. The agent reads it from there.
    set /p "KEY=Paste the key and press Enter: "
    if "!KEY!"=="" (
        echo No key was entered. Run setup.bat again when you have one.
        goto :fail
    )
    setx GEMINI_API_KEY "!KEY!" >nul || goto :fail
    echo Key saved.
) else (
    echo A Gemini API key is already saved on this PC.
)

echo.
echo Setup complete. Open your quiz, run run.bat, and switch to the quiz within 10 seconds.
goto :end

:fail
set "FAILED=1"
echo.
echo Setup did not finish. Read the message above, fix it, and run setup.bat again.

:end
echo.
pause
if defined FAILED exit /b 1
exit /b 0

rem ---- helpers ----

:find_python
set "PY="
for /f "delims=" %%p in ('py -3.13 -c "import sys; print(sys.executable)" 2^>nul') do set "PY=%%p"
if defined PY exit /b 0
for %%p in ("%LOCALAPPDATA%\Programs\Python\Python313\python.exe" "%LOCALAPPDATA%\Programs\Python\Python313-arm64\python.exe" "%ProgramFiles%\Python313\python.exe") do (
    if not defined PY if exist "%%~p" set "PY=%%~p"
)
if defined PY exit /b 0
for /f "delims=" %%p in ('python -c "import sys; v=sys.version_info; print(sys.executable if v.major==3 and v.minor==13 else '')" 2^>nul') do set "PY=%%p"
exit /b 0

:install_python
set "INSTALLER=%TEMP%\python-%PYVER%-%ARCH%.exe"
set "URL=https://www.python.org/ftp/python/%PYVER%/python-%PYVER%-%ARCH%.exe"
echo Downloading Python %PYVER% from python.org, about 27 MB...
curl.exe -L --fail --silent --show-error -o "%INSTALLER%" "%URL%"
if errorlevel 1 (
    powershell -NoProfile -Command "[Net.ServicePointManager]::SecurityProtocol = 'Tls12'; Invoke-WebRequest -Uri '%URL%' -OutFile '%INSTALLER%'"
)
if not exist "%INSTALLER%" (
    echo The download failed. Check the internet connection and run setup.bat again.
    exit /b 1
)
if defined MCQ_SETUP_SKIP_INSTALL (
    echo [test] The installer was downloaded but not run.
    exit /b 0
)
echo Installing Python %PYVER% for your user account. This takes a minute or two...
"%INSTALLER%" /quiet InstallAllUsers=0 PrependPath=1 Include_launcher=1 Include_test=0 Include_doc=0
set "RESULT=!errorlevel!"
del "%INSTALLER%" >nul 2>&1
if "!RESULT!"=="0" exit /b 0
if "!RESULT!"=="3010" exit /b 0
echo The Python installer reported an error (code !RESULT!).
exit /b 1

:find_key
if defined GEMINI_API_KEY exit /b 0
for /f "usebackq delims=" %%k in (`powershell -NoProfile -Command "[Environment]::GetEnvironmentVariable('GEMINI_API_KEY','User')"`) do set "GEMINI_API_KEY=%%k"
if defined GEMINI_API_KEY exit /b 0
for /f "usebackq delims=" %%k in (`powershell -NoProfile -Command "[Environment]::GetEnvironmentVariable('GEMINI_API_KEY','Machine')"`) do set "GEMINI_API_KEY=%%k"
exit /b 0
