import time
import pyautogui
from datetime import datetime
import os

# === Both monitors are 1920x1080 ===
# Monitor 1 is on the left (0, 0)
monitor_1_region = (0, 0, 1920, 1080)

# Monitor 2 is on the right (1920, 0)
monitor_2_region = (1920, 0, 1920, 1080)

# === Save folder ===
save_path = os.path.expanduser("~/Desktop/RFF_Screenshots")

if not os.path.exists(save_path):
    os.makedirs(save_path)

# === Screenshot interval (30 minutes) ===
interval = 1800

print(f"Dual-monitor screenshot capture is LIVE! Saving every {interval//60} minutes.")

try:
    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        
        # Capture Monitor 1
        m1_image = pyautogui.screenshot(region=monitor_1_region)
        m1_filename = os.path.join(save_path, f"monitor1_{timestamp}.png")
        m1_image.save(m1_filename)
        print(f"Monitor 1 screenshot saved: {m1_filename}")

        # Capture Monitor 2
        m2_image = pyautogui.screenshot(region=monitor_2_region)
        m2_filename = os.path.join(save_path, f"monitor2_{timestamp}.png")
        m2_image.save(m2_filename)
        print(f"Monitor 2 screenshot saved: {m2_filename}")

        time.sleep(interval)

except KeyboardInterrupt:
    print("Auto-screenshot stopped manually.")
