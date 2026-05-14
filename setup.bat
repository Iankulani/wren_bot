@echo off
title AWESOME WREN BOT Installer
color 0A

echo ============================================
echo    🐦 AWESOME WREN BOT - Installation
echo ============================================
echo.

echo [1/5] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found. Please install Python 3.7+ from python.org
    pause
    exit /b 1
)
python --version
echo.

echo [2/5] Creating virtual environment...
python -m venv wren_env
if errorlevel 1 (
    echo [ERROR] Failed to create virtual environment
    pause
    exit /b 1
)
echo OK
echo.

echo [3/5] Activating environment and installing dependencies...
call wren_env\Scripts\activate.bat
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] Failed to install dependencies
    pause
    exit /b 1
)
echo OK
echo.

echo [4/5] Creating configuration directories...
mkdir .wren_bot 2>nul
mkdir .wren_bot\payloads 2>nul
mkdir .wren_bot\workspaces 2>nul
mkdir .wren_bot\scans 2>nul
mkdir .wren_bot\nikto_results 2>nul
mkdir .wren_bot\whatsapp_session 2>nul
mkdir .wren_bot\phishing_pages 2>nul
mkdir reports 2>nul
mkdir .wren_bot\traffic_logs 2>nul
mkdir .wren_bot\phishing_templates 2>nul
mkdir .wren_bot\captured_credentials 2>nul
mkdir .wren_bot\ssh_keys 2>nul
mkdir .wren_bot\ssh_logs 2>nul
mkdir .wren_bot\time_history 2>nul
mkdir .wren_bot\wordlists 2>nul
mkdir .wren_bot\web_static 2>nul
mkdir .wren_bot\api_keys 2>nul
mkdir .wren_bot\sessions 2>nul
echo OK
echo.

echo [5/5] Creating run script...
echo @echo off > run_wren.bat
echo call wren_env\Scripts\activate.bat >> run_wren.bat
echo python wren_bot.py %%* >> run_wren.bat
echo pause >> run_wren.bat
echo OK
echo.

echo ============================================
echo    ✅ INSTALLATION COMPLETE!
echo ============================================
echo.
echo To start the bot, run: run_wren.bat
echo.
echo Web Interface: http://localhost:8080
echo.
pause