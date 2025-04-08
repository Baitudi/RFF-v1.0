import cv2
import numpy as np

def draw_glow_floor(frame, grid_size=50, glow_strength=0.4, color=(100, 255, 255)):
    """
    Draws a glowing floor grid beneath the tactical HUD.

    Args:
        frame (ndarray): Input frame to overlay the floor grid on.
        grid_size (int): Size of each grid square.
        glow_strength (float): Opacity of the glow layer (0.0–1.0).
        color (tuple): BGR color of the glow grid lines.

    Returns:
        ndarray: Frame with floor grid applied.
    """
    height, width = frame.shape[:2]
    overlay = frame.copy()

    # Draw vertical grid lines
    for x in range(0, width, grid_size):
        cv2.line(overlay, (x, 0), (x, height), color, 1)

    # Draw horizontal grid lines
    for y in range(0, height, grid_size):
        cv2.line(overlay, (0, y), (width, y), color, 1)

    # Apply glowing blend
    return cv2.addWeighted(overlay, glow_strength, frame, 1 - glow_strength, 0)
