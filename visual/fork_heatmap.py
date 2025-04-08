import cv2
import numpy as np

# Global canvas for persistent heatmap drawing
heatmap_canvas = None

def update_heatmap(hit_points, fail_points, size=(800, 600)):
    """
    Creates or updates a heatmap showing hit (green) and miss (red) fork locations.

    Args:
        hit_points (list): List of (x, y) coordinates for successful forks.
        fail_points (list): List of (x, y) coordinates for failed forks.
        size (tuple): Size of the heatmap canvas (width, height).

    Returns:
        heatmap_canvas (ndarray): The visual heatmap frame.
    """
    global heatmap_canvas
    heatmap_canvas = np.zeros((size[1], size[0], 3), dtype=np.uint8)

    for pt in hit_points:
        cv2.circle(heatmap_canvas, pt, 5, (0, 255, 0), -1)  # Green hit
    for pt in fail_points:
        cv2.circle(heatmap_canvas, pt, 5, (0, 0, 255), -1)  # Red miss

    return heatmap_canvas

def show_heatmap(window_name="Fork Heatmap"):
    """
    Displays the current heatmap in a separate OpenCV window.
    """
    if heatmap_canvas is not None:
        cv2.imshow(window_name, heatmap_canvas)
