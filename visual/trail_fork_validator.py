import cv2
import numpy as np

TRAIL_COLOR = (0, 255, 0)
TRAIL_TOLERANCE = 20

def find_trail_points(image):
    lower = np.array([max(0, c - TRAIL_TOLERANCE) for c in TRAIL_COLOR], dtype=np.uint8)
    upper = np.array([min(255, c + TRAIL_TOLERANCE) for c in TRAIL_COLOR], dtype=np.uint8)
    mask = cv2.inRange(image, lower, upper)
    points = cv2.findNonZero(mask)
    return [tuple(pt[0]) for pt in points] if points is not None else []

def is_fork_valid(fork, trail):
    if not trail: return False
    end = fork["end"]
    for pt in trail:
        if np.linalg.norm(np.subtract(end, pt)) < 25:
            return True
    return False
