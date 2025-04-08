import cv2
import os

def run_replayer_gui(folder_path="rff_dreams"):
    """
    GUI-based replayer for RFF dream snapshots.

    Controls:
        - p: Play / Pause
        - n: Next frame
        - b: Back one frame
        - q or ESC: Quit
        - Speed slider: Adjust playback speed (in ms)
    """
    if not os.path.exists(folder_path):
        print(f"[ERROR] Folder not found: {folder_path}")
        return

    image_files = sorted([
        f for f in os.listdir(folder_path)
        if f.lower().endswith((".png", ".jpg"))
    ])

    if not image_files:
        print(f"[INFO] No snapshots found in: {folder_path}")
        return

    index = 0
    total = len(image_files)
    playing = False
    speed = 100  # Initial playback speed in milliseconds

    cv2.namedWindow("RFF Replayer UI")
    cv2.createTrackbar("Speed (ms)", "RFF Replayer UI", speed, 1000, lambda x: None)

    while True:
        img_path = os.path.join(folder_path, image_files[index])
        image = cv2.imread(img_path)

        if image is None:
            print(f"[WARNING] Could not load: {img_path}")
            index = (index + 1) % total
            continue

        # Display frame info and status
        label = f"[{index + 1}/{total}] {'▶ PLAYING' if playing else '⏸ PAUSED'}"
        cv2.putText(image, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

        # Display control hints
        controls = "[p] Play/Pause   [n] Next   [b] Back   [q] Quit"
        cv2.putText(image, controls, (10, image.shape[0] - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 1)

        cv2.imshow("RFF Replayer UI", image)

        key = cv2.waitKey(speed if playing else 100) & 0xFF

        if key == ord('q') or key == 27:
            print("[UI] Exit requested.")
            break
        elif key == ord('p'):
            playing = not playing
        elif key == ord('n'):
            index = (index + 1) % total
        elif key == ord('b'):
            index = (index - 1 + total) % total

        if playing and key == 255:  # No key pressed while playing
            index = (index + 1) % total

        # Read the current slider value
        speed = cv2.getTrackbarPos("Speed (ms)", "RFF Replayer UI")

    cv2.destroyAllWindows()
