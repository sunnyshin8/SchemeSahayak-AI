@echo off
REM Test CyborgDB and Start Backend

echo ===============================================
echo CyborgDB Backend Startup Script
echo ===============================================

cd /d %~dp0

echo.
echo [1/4] Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo [2/4] Testing CyborgDB installation...
python -c "import cyborgdb; print('✓ cyborgdb is installed')" 2>nul
if errorlevel 1 (
    echo ✗ cyborgdb not found. Installing...
    pip install cyborgdb
)

echo.
echo [3/4] Testing CyborgDB connection...
cd backend
python test_cyborg_install.py

echo.
echo [4/4] Starting backend server...
echo Backend will start on http://localhost:8000
echo Press Ctrl+C to stop
python main.py

pause
