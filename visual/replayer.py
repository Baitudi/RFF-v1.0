import cv2
import os
import time

def replay_snapshots(folder_path="rff_dreams", delay=0.3):
    """
    Replays saved RFF dream snapshots one by one.
    folder_path: path to rff_dreams/
    delay: time (in seconds) between frames
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

    print(f"[REPLAYER] Replaying {len(image_files)} snapshots from {folder_path}")

    for img_name in image_files:
        img_path = os.path.join(folder_path, img_name)
        image = cv2.imread(img_path)

        if image is not None:
            cv2.imshow("RFF Replayer", image)
            key = cv2.waitKey(int(delay * 1000)) & 0xFF
            if key == ord('q') or key == 27:
                print("[REPLAYER] Replay aborted by user.")
                break
        else:
            print(f"[WARNING] Failed to load: {img_path}")

    cv2.destroyAllWindows()
