import cv2
import os

def run_replayer_dashboard(folder_path="rff_dreams"):
    """
    Launches a replay dashboard for RFF dream snapshots.
    Controls:
        p - Play/Pause toggle
        n - Next frame
        b - Back frame
        q or ESC - Exit viewer
    """
    if not os.path.exists(folder_path):
        print(f"[ERROR] Folder not found: {folder_path}")
        return

    image_files = sorted([
        f for f in os.listdir(folder_path)
        if f.lower().endswith((".png", ".jpg"))
    ])

    if not image_files:
        print(f"[INFO] No images to replay in: {folder_path}")
        return

    print(f"[DASHBOARD] Loaded {len(image_files)} snapshots.")

    index = 0
    paused = True

    while True:
        img_path = os.path.join(folder_path, image_files[index])
        image = cv2.imread(img_path)
        if image is None:
            print(f"[WARNING] Failed to load: {img_path}")
            index = (index + 1) % len(image_files)
            continue

        # Overlay status
        label = f"[{index + 1}/{len(image_files)}] - {'PAUSED' if paused else 'PLAYING'}"
        cv2.putText(image, label, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

        cv2.imshow("RFF Replayer Dashboard", image)

        key = cv2.waitKey(100) & 0xFF

        if key == ord('q') or key == 27:
            print("[DASHBOARD] Exiting replay.")
            break
        elif key == ord('p'):
            paused = not paused
        elif key == ord('n'):
            index = (index + 1) % len(image_files)
        elif key == ord('b'):
            index = (index - 1 + len(image_files)) % len(image_files)

        if not paused:
            index = (index + 1) % len(image_files)

    cv2.destroyAllWindows()
