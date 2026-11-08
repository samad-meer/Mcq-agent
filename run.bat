@echo off
rem Answers the quiz on screen with Gemini: the mouse moves to each correct option and clicks it.
rem Add --dry-run to only point at the answer without clicking. Other options go to the agent too,
rem for example: run.bat --model gemini-3.8-flash
rem For a provider other than Gemini, run mcq_agent.py directly with --provider and --model.
rem On a PC with no .venv yet, this runs setup.bat first to build it, then starts the agent.
cd /d "%~dp0" || (
    echo This folder is on a network share. Copy it onto this PC first.
    pause
    exit /b 1
)
setlocal

rem If this folder has no working .venv (first run on this PC, or the folder was copied
rem from another PC where the .venv cannot be reused), build it now by running setup.
".venv\Scripts\python.exe" -c "import sys" >nul 2>&1 && goto :haveenv
echo No ready .venv in this folder yet, so setup runs first to build it.
echo   Folder: "%~dp0"
echo.
call "%~dp0setup.bat"
".venv\Scripts\python.exe" -c "import sys" >nul 2>&1 && goto :haveenv
echo.
echo Setup could not build a working .venv in this folder. Read the messages above,
echo then double-click setup.bat in THIS folder and wait for "Setup complete".
echo.
pause
exit /b 1

:haveenv
rem The agent reads the key from the .env file next to it, or from the environment.
echo.
echo Switch to your quiz now and leave the mouse alone. The quiz must be on your main monitor.
echo To stop, move the mouse to a corner of the screen.
.venv\Scripts\python mcq_agent.py --provider gemini --model gemini-3.5-flash-lite --delay 10 %*

echo.
pause
