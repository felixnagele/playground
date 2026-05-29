@echo off
setlocal enabledelayedexpansion

echo Preparing environments...
call uv python install 3.14 || exit /b %errorlevel%
call uv python install 3.15+freethreaded || exit /b %errorlevel%

if not exist ".venv-classic" call uv venv .venv-classic --python 3.14 || exit /b %errorlevel%
if not exist ".venv-nogil"   call uv venv .venv-nogil   --python 3.15+freethreaded || exit /b %errorlevel%

call .venv-classic\Scripts\python.exe benchmark.py

pause
endlocal
