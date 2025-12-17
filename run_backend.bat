@echo off
cd /d %~dp0
call venv\Scripts\activate.bat

echo Starting backend with verbose output...
cd backend
python -u main.py
pause
