import cv2
import os

def run_ghost_replay(folder_path="rff_dreams", delay=0.3):
    """
    Replays RFF snapshots with ghost fork trail overlays.
    Each frame fades in the previous snapshots like an AI memory echo.
    Press 'q' or ESC to exit replay.
    """
    if not os.path.exists(folder_path):
        print(f"[ERROR] Folder not found: {folder_path}")
        return

    image_files = sorted([
        f for f in os.listdir(folder_path)
        if f.lower().endswith((".png", ".jpg"))
    ])

    if not image_files:
        print(f"[INFO] No snapshots to replay in: {folder_path}")
        return

    print(f"[GHOST REPLAY] Replaying {len(image_files)} frames from '{folder_path}'")

    ghost_frames = []

    for idx, img_name in enumerate(image_files):
        img_path = os.path.join(folder_path, img_name)
        frame = cv2.imread(img_path)

        if frame is None:
            print(f"[WARNING] Could not load: {img_path}")
            continue

        ghost_frames.append(frame.copy())

        ghost_overlay = frame.copy()
        for past_frame in ghost_frames[-10:-1]:
            ghost_overlay = cv2.addWeighted(ghost_overlay, 0.9, past_frame, 0.1, 0)

        label = f"[{idx+1}/{len(image_files)}] GHOST MEMORY VIEW"
        cv2.putText(ghost_overlay, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        cv2.imshow("RFF Ghost Replayer", ghost_overlay)
        key = cv2.waitKey(int(delay * 1000)) & 0xFF

        if key == ord('q') or key == 27:
            print("[GHOST] Replay aborted by user.")
            break

    cv2.destroyAllWindows()
    print("[GHOST] Replay complete.")
