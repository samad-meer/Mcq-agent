@echo off
rem Answers the quiz on screen with Gemini: the mouse moves to each correct option and clicks it.
rem Add --dry-run to only point at the answer without clicking. Other options go to the agent too,
rem for example: run.bat --model gemini-3.8-flash
rem For a provider other than Gemini, run mcq_agent.py directly with --provider and --model.
setlocal
cd /d "%~dp0"

if not defined GEMINI_API_KEY for /f "usebackq delims=" %%k in (`powershell -NoProfile -Command "[Environment]::GetEnvironmentVariable('GEMINI_API_KEY','User')"`) do set "GEMINI_API_KEY=%%k"
if not defined GEMINI_API_KEY for /f "usebackq delims=" %%k in (`powershell -NoProfile -Command "[Environment]::GetEnvironmentVariable('GEMINI_API_KEY','Machine')"`) do set "GEMINI_API_KEY=%%k"

echo.
echo Switch to your quiz now and leave the mouse alone.
echo To stop, move the mouse to a corner of the screen.
.venv\Scripts\python mcq_agent.py --provider gemini --model gemini-3.5-flash-lite --delay 10 %*

echo.
pause
