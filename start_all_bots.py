import os
import sys
import subprocess
import time
import threading

def run_bot(folder, name):
    """একটি বট চালায়"""
    print(f"🚀 Starting {name}...")
    
    # ফোল্ডার আছে কিনা চেক করুন (কেস-সেনসিটিভ)
    if not os.path.exists(folder) or not os.path.isdir(folder):
        print(f"❌ {name} folder not found: {folder}")
        return
    
    try:
        # ফোল্ডারে যান
        os.chdir(folder)
        print(f"📁 Changed to: {os.getcwd()}")
        
        # main.py চালান
        result = subprocess.run(
            [sys.executable, "main.py"],
            check=True,
            capture_output=True,
            text=True
        )
        print(f"✅ {name} started successfully")
        print(result.stdout)
        
    except subprocess.CalledProcessError as e:
        print(f"❌ {name} error: {e.stderr}")
    except Exception as e:
        print(f"❌ {name} error: {e}")

if __name__ == "__main__":
    print("🎬 Reward Bots - Starting both bots on Render...")
    
    # বর্তমান ডিরেক্টরি
    current_dir = os.getcwd()
    print(f"📁 Current directory: {current_dir}")
    
    # ফোল্ডার লিস্ট (সঠিকভাবে দেখুন)
    try:
        folders = [f for f in os.listdir(current_dir) if os.path.isdir(os.path.join(current_dir, f))]
        print(f"📁 Folders found: {folders}")
    except Exception as e:
        print(f"❌ Error listing folders: {e}")
        folders = []
    
    # ইমেজ বট চালান
    if "image_bot" in folders:
        threading.Thread(target=run_bot, args=("image_bot", "Image Bot"), daemon=True).start()
    else:
        print("❌ image_bot folder not found!")
    
    # ভিডিও বট চালান
    if "video_bot" in folders:
        threading.Thread(target=run_bot, args=("video_bot", "Video Bot"), daemon=True).start()
    else:
        print("❌ video_bot folder not found!")
    
    print("✅ Both bots started!")
    
    # বট চালু রাখুন
    while True:
        time.sleep(60)
