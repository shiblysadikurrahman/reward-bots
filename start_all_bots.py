import os
import sys
import subprocess
import time
import asyncio
import threading

def run_bot(folder, name):
    """একটি বট চালায়"""
    print(f"🚀 Starting {name}...")
    
    # ফোল্ডার আছে কিনা চেক করুন
    if not os.path.exists(folder):
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

def run_bot_async(folder, name):
    """একটি বট চালায় (Asyncio সহ)"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    try:
        # ফোল্ডারে যান
        os.chdir(folder)
        print(f"📁 Starting {name} in: {os.getcwd()}")
        
        # main.py চালান
        loop.run_until_complete(run_async_subprocess(name))
    except Exception as e:
        print(f"❌ {name} error: {e}")
    finally:
        loop.close()

async def run_async_subprocess(name):
    """Async subprocess"""
    try:
        proc = await asyncio.create_subprocess_exec(
            sys.executable, "main.py",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await proc.communicate()
        if proc.returncode == 0:
            print(f"✅ {name} started successfully")
        else:
            print(f"❌ {name} error: {stderr.decode()}")
    except Exception as e:
        print(f"❌ {name} error: {e}")

if __name__ == "__main__":
    print("🎬 Reward Bots - Starting both bots on Render...")
    
    # বর্তমান ডিরেক্টরি
    current_dir = os.getcwd()
    print(f"📁 Current directory: {current_dir}")
    
    # ফোল্ডার লিস্ট
    folders = os.listdir(current_dir)
    print(f"📁 Folders found: {folders}")
    
    # ইমেজ বট চালান
    if "image_bot" in folders:
        threading.Thread(target=run_bot, args=("image_bot", "Image Bot")).start()
    else:
        print("❌ image_bot folder not found!")
    
    # ভিডিও বট চালান
    if "video_bot" in folders:
        threading.Thread(target=run_bot, args=("video_bot", "Video Bot")).start()
    else:
        print("❌ video_bot folder not found!")
    
    print("✅ Both bots started!")
