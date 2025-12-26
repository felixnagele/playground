@echo off
color 0a
cls

:: Infinite loop for random numbers
:loop
echo %random%%random%%random%%random%%random%%random%%random%

:: Short delay using ping (50 ms)
ping 127.0.0.1 -n 1 -w 50 >nul

goto loop
