import cv2
import numpy as np

def highlight_convergence_zones(frame, forks, radius=30):
    """
    Highlights convergence zones where multiple forks end closely together.
    
    Args:
        frame (ndarray): The frame to draw on.
        forks (list): List of fork dictionaries with "end" coordinates.
        radius (int): Distance threshold to consider points as converging.
    
    Returns:
        frame (ndarray): Frame with visualized convergence zones.
    """
    ends = [f["end"] for f in forks]
    zones = []

    for i, pt in enumerate(ends):
        close = sum(
            1 for j in range(len(ends))
            if i != j and np.linalg.norm(np.subtract(pt, ends[j])) < radius
        )
        if close >= 2:
            zones.append(pt)

    for pt in zones:
        cv2.circle(frame, pt, radius, (255, 255, 0), 2)  # Yellow convergence circles

    return frame
