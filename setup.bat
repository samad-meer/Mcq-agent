@echo off
rem Sets up the MCQ agent on a Windows 10 or 11 PC. Run it once, by double-clicking it or from a
rem terminal, with the internet connected. It installs Python 3.13 for your user account if the PC
rem does not have it (no admin rights needed), creates the .venv folder, installs the tested package
rem versions, and saves your Gemini API key in the .env file here. After it finishes, use run.bat.
cd /d "%~dp0" || (
    echo This folder is on a network share. Copy it onto this PC first, then run setup.bat there.
    goto :fail
)
rem 146 = 260, the longest path Windows allows by default, minus 25 for \.venv\Lib\site-packages\
rem and 89 for the longest file openai 3.42.0 installs. Recompute if requirements.txt changes.
if not "%CD:~145%"=="" (
    echo This folder's path is longer than 145 characters, more than Windows allows for the files setup installs.
    echo Move the folder somewhere short, such as C:\mcq-agent or your Desktop, and run setup.bat again.
    goto :fail
)
if not exist "requirements.txt" goto :nofiles
if not exist "mcq_agent.py" goto :nofiles
setlocal EnableDelayedExpansion
set "PYVER=3.13.3"
set "MIN_INSTALLER_BYTES=20000000"
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

rem A .venv copied from another PC, or left by a Python that is gone, cannot start; it is rebuilt.
".venv\Scripts\python.exe" -c "import sys" >nul 2>&1 || (
    if exist ".venv\pyvenv.cfg" echo The .venv folder was made on another PC or with a Python that is gone, so it is rebuilt.
    echo Creating the virtual environment...
    "!PY!" -m venv --clear .venv || goto :fail
)
echo Installing the tested package versions. This takes a minute or two...
".venv\Scripts\python.exe" -m pip install --disable-pip-version-check -q -r requirements.txt || goto :fail
".venv\Scripts\python.exe" -c "import mss, openai, pyautogui, PIL, pydantic" || goto :fail
echo Packages installed.

rem The key lives in the .env file next to the agent; a key set as an environment variable still counts.
set "KEY="
set "HAVEKEY="
echo.
".venv\Scripts\python.exe" mcq_agent.py --provider gemini --check-key 2>nul && set "HAVEKEY=1"
if defined HAVEKEY (
    set /p "KEY=Press Enter to keep that key, or paste a new one and press Enter: "
) else (
    echo You need your own free Gemini API key. Get one at https://aistudio.google.com/apikey
    echo Use the Copy button next to the key. It is saved in the .env file in this folder; keep that file to yourself.
    set /p "KEY=Paste the key and press Enter: "
)
if defined KEY set "KEY=!KEY: =!"
if defined KEY (
    ".venv\Scripts\python.exe" mcq_agent.py --provider gemini --save-key "!KEY!" || goto :fail
) else if not defined HAVEKEY (
    echo No key was entered. Run setup.bat again when you have one.
    goto :fail
)

echo.
echo Setup complete. Open your quiz, run run.bat, and switch to the quiz within 10 seconds.
goto :end

:nofiles
echo setup.bat is running from "%~dp0" but requirements.txt and mcq_agent.py are not there.
echo If you opened it inside the ZIP window, right-click the ZIP, choose Extract All, and run setup.bat from the extracted folder.

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
rem Delayed expansion is off in here, so a path with an exclamation mark survives. A path that
rem comes back garbled by the console's code page is dropped in favour of the known install folders.
setlocal DisableDelayedExpansion
set "PY="
for /f "delims=" %%p in ('py -3.13 -c "import sys; print(sys.executable)" 2^>nul') do set "PY=%%p"
if defined PY if not exist "%PY%" set "PY="
if not defined PY for %%p in ("%LOCALAPPDATA%\Programs\Python\Python313\python.exe" "%LOCALAPPDATA%\Programs\Python\Python313-arm64\python.exe" "%ProgramFiles%\Python313\python.exe") do (
    if not defined PY if exist "%%~p" set "PY=%%~p"
)
if not defined PY for /f "delims=" %%p in ('python -c "import sys; v=sys.version_info; print(sys.executable if v.major==3 and v.minor==13 else '')" 2^>nul') do set "PY=%%p"
if defined PY if not exist "%PY%" set "PY="
endlocal & set "PY=%PY%"
exit /b 0

:install_python
set "INSTALLER=%TEMP%\python-%PYVER%-%ARCH%.exe"
set "URL=https://www.python.org/ftp/python/%PYVER%/python-%PYVER%-%ARCH%.exe"
del "%INSTALLER%" >nul 2>&1
echo Downloading Python %PYVER% from python.org, about 27 MB...
where /q curl.exe && curl.exe -L --fail -# -o "%INSTALLER%" "%URL%"
if errorlevel 1 (
    del "%INSTALLER%" >nul 2>&1
    powershell -NoProfile -Command "$ProgressPreference = 'SilentlyContinue'; [Net.ServicePointManager]::SecurityProtocol = 'Tls12'; $p = [Net.WebRequest]::DefaultWebProxy; if ($p) { $p.Credentials = [Net.CredentialCache]::DefaultCredentials }; Invoke-WebRequest -UseBasicParsing -Uri '%URL%' -OutFile '%INSTALLER%'"
)
rem A download that broke off leaves a short file, which must never be run as the installer.
if not exist "%INSTALLER%" goto :baddownload
for %%s in ("%INSTALLER%") do if %%~zs LSS %MIN_INSTALLER_BYTES% goto :baddownload
if defined MCQ_SETUP_SKIP_INSTALL (
    echo [test] The installer was downloaded but not run.
    exit /b 0
)
echo Installing Python %PYVER% for your user account. This takes a minute or two...
rem InstallLauncherAllUsers=0 keeps the install free of admin prompts on a PC that already has
rem an all-users py launcher from an older Python.
"%INSTALLER%" /quiet InstallAllUsers=0 InstallLauncherAllUsers=0 PrependPath=1 Include_launcher=1 Include_test=0 Include_doc=0
set "RESULT=!errorlevel!"
del "%INSTALLER%" >nul 2>&1
if "!RESULT!"=="0" exit /b 0
if "!RESULT!"=="3010" exit /b 0
echo The Python installer reported an error (code !RESULT!).
exit /b 1

:baddownload
del "%INSTALLER%" >nul 2>&1
echo The download did not complete. Check the internet connection, any proxy or antivirus, and run setup.bat again.
exit /b 1
