import cv2

def draw_trail(frame, trail_points, color=(0, 255, 0), radius=3):
    """
    Draws a glowing trail of the player's past positions on the given frame.

    Parameters:
    - frame: The image/frame to draw on
    - trail_points: List of (x, y) tuples representing the trail path
    - color: Color of the trail (default green)
    - radius: Radius of the trail dots
    """
    if not trail_points:
        return frame

    # Draw solid trail dots
    for pt in trail_points:
        cv2.circle(frame, pt, radius, color, -1)

    # Add glow effect on recent points
    overlay = frame.copy()
    for pt in trail_points[-10:]:
        cv2.circle(overlay, pt, radius + 6, color, -1)
    frame = cv2.addWeighted(overlay, 0.2, frame, 0.8, 0)

    return frame
