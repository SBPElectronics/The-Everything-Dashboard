import tkinter as tk
import threading
from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageDraw
import subprocess
import os
import sys

# --- Path to the script you want to run ---
CRYPTO_PATH = "crypto_info.py"  # Make sure this is in the same folder or provide full path

# --- Function to run the script ---
def run_script():
    try:
        # Run the external Python file
        subprocess.run([sys.executable, CRYPTO_PATH], check=True)
    except subprocess.CalledProcessError as e:
        print("Script failed:", e)

# --- Function to show the Tkinter window ---
def show_window():
    def on_close():
        window.withdraw()  # Just hide instead of closing
    if window.state() == 'withdrawn':
        window.deiconify()
    window.lift()
    window.focus_force()
    window.protocol("WM_DELETE_WINDOW", on_close)

# --- Create a circular system tray icon image ---
def create_image():
    image = Image.new('RGB', (64, 64), color=(255, 255, 255))
    draw = ImageDraw.Draw(image)
    draw.ellipse((16, 16, 48, 48), fill=(0, 128, 255))
    return image

# --- Set up the system tray icon ---
def setup_tray():
    icon = Icon("MyApp", create_image(), menu=Menu(
        MenuItem("Open Window", lambda: show_window()),
        MenuItem("Quit", lambda: icon.stop())
    ))
    icon.run()

# --- Start the tray icon in a separate thread ---
def run_tray():
    threading.Thread(target=setup_tray, daemon=True).start()

# --- Tkinter GUI Setup ---
window = tk.Tk()
window.title("My App Window")
window.geometry("300x200")

label = tk.Label(window, text="Hello! This is the main window.")
label.pack(pady=10)

run_button = tk.Button(window, text="Run test_script.py", command=run_script)
run_button.pack(pady=5)

# --- Hide the window initially ---
window.withdraw()

# --- Start tray icon and GUI loop ---
run_tray()
window.mainloop()
