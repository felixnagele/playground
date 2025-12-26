@echo off
setlocal enabledelayedexpansion
color 0e

:: Bar length
set barlength=20

:loop
:: Percent from 0 to 100 in steps of 5
for /l %%p in (0,5,100) do (

  :: Calculate # display amount
  set /a filled=%%p * barlength / 100

  :: Build the bar string
  set "bar="
  for /l %%i in (1,1,%barlength%) do (
    if %%i LEQ !filled! (
      set "bar=!bar!#"
    ) else (
      set "bar=!bar!-"
    )
  )

  cls
  echo Progress: [!bar!] %%p%%

  :: Wait for a short time
  timeout /t 0 >nul
)

goto loop
