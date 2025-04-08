import cv2
import numpy as np
import math

def draw_fork_with_glow(frame, start, end, confidence):
    """
    Draws a glowing directional fork arrow between two points, colored based on confidence level.

    Args:
        frame (ndarray): Image to draw on.
        start (tuple): (x, y) coordinates for fork origin.
        end (tuple): (x, y) coordinates for fork endpoint.
        confidence (float): Range 0.0 (low) to 1.0 (high). Affects color and glow intensity.

    Returns:
        ndarray: Frame with fork overlay.
    """
    # Calculate glow color: Green = high confidence, Red = low confidence
    glow = int(255 * confidence)
    color = (0, glow, 255 - glow)  # Red–Green scale
    thickness = 2 + int(confidence * 2)  # Thicker for higher certainty

    overlay = frame.copy()
    cv2.arrowedLine(overlay, start, end, color, thickness, tipLength=0.3)

    # Apply transparency to simulate glow
    alpha = 0.6 + confidence * 0.4  # Glow intensity
    return cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0)
