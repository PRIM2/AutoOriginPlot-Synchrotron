@echo off
title Run main_script
color 07

echo.
echo ==========================
echo    RUNNING MAIN_SCRIPT
echo ==========================
echo.

REM Check if Python exists
where python >nul 2>&1
if errorlevel 1 (
    echo Python not found.
    echo Download the latest version: https://www.python.org/downloads/
    echo.
    pause
    exit /b
)

REM Run Python script
python lib/main.py

echo.
echo =========================
echo    EXECUTION COMPLETED
echo =========================
echo.

pause
