import cv2
import os

def export_replay_to_video(folder_path="rff_dreams", output_path="rff_replay.mp4", fps=6):
    """
    Exports a series of images from the given folder into a video file.
    
    Args:
        folder_path (str): Path to folder containing replay frames (.png or .jpg)
        output_path (str): Output video file name (e.g., 'rff_replay.mp4')
        fps (int): Frames per second for the output video
    
    Returns:
        None
    """
    images = sorted([
        f for f in os.listdir(folder_path)
        if f.lower().endswith(('.png', '.jpg'))
    ])
    
    if not images:
        print(f"[EXPORT ERROR] No image files found in {folder_path}")
        return

    first = cv2.imread(os.path.join(folder_path, images[0]))
    h, w = first.shape[:2]

    out = cv2.VideoWriter(
        output_path,
        cv2.VideoWriter_fourcc(*"mp4v"),
        fps,
        (w, h)
    )

    for f in images:
        img_path = os.path.join(folder_path, f)
        img = cv2.imread(img_path)
        if img is not None:
            out.write(img)

    out.release()
    print(f"[EXPORT] Replay video saved to: {output_path}")
