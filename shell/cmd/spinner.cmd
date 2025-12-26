@echo off
setlocal enabledelayedexpansion
color 0c

:: Spinner characters
set "chars=\|/-"

:loop
for /l %%i in (0,1,3) do (
  set "c=!chars:~%%i,1!"

  cls
  echo !c!

  :: Faster spin
  timeout /t 0 >nul
)
goto loop
