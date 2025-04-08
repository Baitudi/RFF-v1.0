import cv2
from visual.flywheel_curve_renderer import draw_flywheel_curve

def draw_ghost_memory(
    frame,
    ghost_trail,
    intensity=0.4,
    color=(200, 200, 255),
    radius=4,
    use_curve=True
):
    """
    Draws a ghost memory overlay showing past AI trail (curved or point-based).

    Args:
        frame (ndarray): Frame to draw on.
        ghost_trail (list): List of (x, y) points from AI memory.
        intensity (float): Overlay alpha (0.0–1.0).
        color (tuple): BGR color for trail.
        radius (int): Radius of each ghost dot if curve is off.
        use_curve (bool): If True, draws flywheel curve instead of dots.

    Returns:
        ndarray: Frame with ghost memory overlay applied.
    """
    overlay = frame.copy()

    if not ghost_trail:
        return frame

    if use_curve and len(ghost_trail) >= 2:
        overlay = draw_flywheel_curve(
            overlay,
            points=ghost_trail,
            color=color,
            thickness=2,
            tension=0.5
        )
    else:
        for pt in ghost_trail:
            cv2.circle(overlay, pt, radius, color, -1)

    return cv2.addWeighted(overlay, intensity, frame, 1 - intensity, 0)
