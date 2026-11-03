@echo off
rem The same as run.bat with --fast: a shorter reply and only the quiz's part of the screen is sent.
rem Other options pass through, for example: run_fast.bat --debug
call "%~dp0run.bat" --fast %*
