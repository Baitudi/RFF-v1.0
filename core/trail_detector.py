# core/trail_detector.py

import cv2
import numpy as np
from PIL import ImageGrab

# Define the trail color in BGR (example: updated to your theme)
TRAIL_BGR_LOWER = np.array([85, 110, 130])   # Adjust based on detection tests
TRAIL_BGR_UPPER = np.array([105, 140, 160])

def detect_trail_live(region=(990, 556, 930, 474)):
    """
    Capture live screen and detect trail points based on color range.
    Returns a list of (x, y) points.
    """
    x, y, w, h = region
    screen = np.array(ImageGrab.grab(bbox=(x, y, x + w, y + h)))
    frame_bgr = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)

    # Create mask to detect trail color
    mask = cv2.inRange(frame_bgr, TRAIL_BGR_LOWER, TRAIL_BGR_UPPER)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    points = []
    for contour in contours:
        for pt in contour:
            x, y = pt[0]
            points.append((x, y))

    # Sort trail points left to right
    points.sort(key=lambda p: p[0])
    return points
