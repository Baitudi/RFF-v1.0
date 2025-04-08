import cv2
import numpy as np

def draw_flywheel_curve(frame, points, color=(0, 255, 255), thickness=2, tension=0.5):
    """
    Draws a smooth curved line (flywheel style) connecting a series of points.

    Args:
        frame (ndarray): The image/frame to draw on.
        points (list): List of (x, y) tuples forming the curve path.
        color (tuple): BGR color of the curve.
        thickness (int): Line thickness.
        tension (float): Curve tension between 0 (linear) and 1 (smoothest).

    Returns:
        frame (ndarray): Frame with flywheel curve drawn.
    """
    if len(points) < 2:
        return frame

    curve_pts = []

    for i in range(1, len(points)):
        p0 = np.array(points[i - 1], dtype=np.float32)
        p1 = np.array(points[i], dtype=np.float32)
        for t in np.linspace(0, 1, num=20):
            pt = (1 - t) * p0 + t * p1 + tension * np.sin(t * np.pi) * (p1 - p0)
            curve_pts.append(tuple(pt.astype(int)))

    for i in range(1, len(curve_pts)):
        cv2.line(frame, curve_pts[i - 1], curve_pts[i], color, thickness)

    return frame
