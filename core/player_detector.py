# core/player_detector.py

import cv2
import numpy as np
from PIL import ImageGrab

# Define BGR values for player with and without glow
PLAYER_BGR_VALUES = [
    np.array([50, 163, 0]),   # Without glow
    np.array([56, 191, 29])   # With glow
]

# Detection region (Chart 4 - Bottom Right)
DETECTION_REGION = (1026, 650, 705, 330)  # (x, y, w, h)

def detect_player_position():
    """
    Detect the green blinking dot (player) in Chart 4.
    Returns (x, y) position or None.
    """
    x, y, w, h = DETECTION_REGION
    screen = np.array(ImageGrab.grab(bbox=(x, y, x + w, y + h)))
    frame_bgr = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)

    for bgr in PLAYER_BGR_VALUES:
        lower = bgr - 10
        upper = bgr + 10
        mask = cv2.inRange(frame_bgr, lower, upper)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            # Use the largest contour assuming it's the player
            largest = max(contours, key=cv2.contourArea)
            M = cv2.moments(largest)
            if M["m00"] > 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                return (cx, cy)
    
    return None
