@echo off
cls

:: Infinite color cycle loop
:loop
for %%c in (1 2 3 4 5 6 7 8 9 A B C D E F) do (
  color %%c
  echo Color %%c

  :: 1 second delay
  timeout /t 1 >nul
)

goto loop
