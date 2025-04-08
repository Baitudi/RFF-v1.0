import cv2
import os
import signal
import sys
import time

# === Config ===
SNAPSHOT_FOLDER = "rff_dreams"
IMAGE_TIMEOUT = 30        # seconds to wait before auto-next
TOTAL_RUN_TIMEOUT = 300   # max total seconds to run
start_time = time.time()

# === Exit Handler ===
def exit_handler(sig, frame):
    print("\n[INFO] Ctrl+C detected. Shutting down viewer...")
    cv2.destroyAllWindows()
    sys.exit(0)

signal.signal(signal.SIGINT, exit_handler)

# === Prepare Folder ===
if not os.path.exists(SNAPSHOT_FOLDER):
    print(f"[INFO] Creating snapshot folder: {SNAPSHOT_FOLDER}")
    os.makedirs(SNAPSHOT_FOLDER)

image_files = sorted([
    f for f in os.listdir(SNAPSHOT_FOLDER)
    if f.lower().endswith((".png", ".jpg", ".jpeg"))
])

if not image_files:
    print("[INFO] No snapshots found in rff_dreams/")
    sys.exit(0)

print(f"[INFO] {len(image_files)} snapshots loaded. Controls: [n] next, [p] previous, [q]/[ESC] quit.")

# === Viewer Loop ===
index = 0
while True:
    if time.time() - start_time > TOTAL_RUN_TIMEOUT:
        print("[INFO] Auto shutdown after total timeout.")
        break

    image_path = os.path.join(SNAPSHOT_FOLDER, image_files[index])
    image = cv2.imread(image_path)

    if image is None:
        print(f"[WARNING] Cannot load: {image_path}")
        index = (index + 1) % len(image_files)
        continue

    cv2.imshow("Dream Snapshot Viewer", image)

    key = cv2.waitKey(IMAGE_TIMEOUT * 1000) & 0xFF

    if key == ord('q') or key == 27:  # 'q' or ESC
        print("[INFO] Viewer closed by user.")
        break
    elif key == ord('n'):
        index = (index + 1) % len(image_files)
    elif key == ord('p'):
        index = (index - 1) % len(image_files)
    else:
        # Auto-next if no key pressed
        index = (index + 1) % len(image_files)

cv2.destroyAllWindows()
