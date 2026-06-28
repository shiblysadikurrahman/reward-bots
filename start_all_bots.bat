@echo off
title Reward Bots - Image + Video

echo ========================================
echo    🖼️ Image Bot + 🎬 Video Bot
echo    Starting both bots simultaneously...
echo ========================================
echo.

start "Image Bot" cmd /c "cd /d C:\reward_bots\image_bot && python main.py"
start "Video Bot" cmd /c "cd /d C:\reward_bots\video_bot && python main.py"

echo.
echo ✅ Both bots are starting!
echo 📌 Check separate windows for logs.
echo.
echo Press any key to close this window...
pause >nul
