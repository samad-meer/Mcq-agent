@echo off
rem Answers the quiz on screen with Gemini: the mouse moves to each correct option and clicks it.
rem Add --dry-run to only point at the answer without clicking. Other options go to the agent too,
rem for example: run.bat --model gemini-3.8-flash
rem For a provider other than Gemini, run mcq_agent.py directly with --provider and --model.
cd /d "%~dp0" || (
    echo This folder is on a network share. Copy it onto this PC first.
    pause
    exit /b 1
)
setlocal
".venv\Scripts\python.exe" -c "import sys" >nul 2>&1 || (
    echo Run setup.bat first: the .venv folder is missing, or it was made on another PC.
    echo.
    pause
    exit /b 1
)

rem The agent reads the key from the .env file next to it, or from the environment.
echo.
echo Switch to your quiz now and leave the mouse alone. The quiz must be on your main monitor.
echo To stop, move the mouse to a corner of the screen.
.venv\Scripts\python mcq_agent.py --provider gemini --model gemini-3.5-flash-lite --delay 10 %*

echo.
pause
