import cv2
import math

def draw_prediction_forks(frame, origin, angles, length=80, confidence_levels=None):
    """
    Draws fork arrows on a frame given a list of angles and optional confidence levels.

    Args:
        frame (ndarray): The image/frame to draw on.
        origin (tuple): (x, y) coordinate from which all forks originate.
        angles (list): List of angles (in degrees) to draw the forks.
        length (int): Length of each fork arrow.
        confidence_levels (list): List of confidence values (0.0 to 1.0) per fork.

    Returns:
        ndarray: Frame with prediction arrows overlaid.
    """
    overlay = frame.copy()

    for i, angle in enumerate(angles):
        radians = math.radians(angle)
        end = (
            int(origin[0] + math.cos(radians) * length),
            int(origin[1] + math.sin(radians) * length)
        )

        # Get confidence-based color and thickness
        confidence = confidence_levels[i] if confidence_levels else 1.0
        color = (
            int(255 * (1 - confidence)),   # Red (low confidence)
            int(255 * confidence),         # Green (high confidence)
            0                              # Blue fixed to 0
        )
        thickness = 1 + int(confidence * 3)

        # Draw the fork arrow
        cv2.arrowedLine(overlay, origin, end, color, thickness, tipLength=0.3)

    # Blend overlay with original frame
    return cv2.addWeighted(overlay, 0.7, frame, 0.3, 0)
