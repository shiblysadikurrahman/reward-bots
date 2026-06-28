import os
import sys
import subprocess
import time
import threading

def run_bot(folder, name):
    """একটি বট চালায়"""
    print(f"🚀 Starting {name}...")
    os.chdir(folder)
    try:
        subprocess.run([sys.executable, "main.py"], check=True)
    except Exception as e:
        print(f"❌ {name} error: {e}")

if __name__ == "__main__":
    print("🎬 Reward Bots - Starting both bots on Render...")
    
    # Environment Variables থেকে টোকেন নেওয়া
    # Render-এ আলাদা করে দিতে হবে
    
    # দুই বট আলাদা থ্রেডে চালানো
    thread1 = threading.Thread(target=run_bot, args=("image_bot", "Image Bot"))
    thread2 = threading.Thread(target=run_bot, args=("video_bot", "Video Bot"))
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
