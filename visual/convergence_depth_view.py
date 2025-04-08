import cv2
import numpy as np

def render_convergence_depth(frame, forks, radius=40, min_overlap=3):
    """
    Highlights high-density fork convergence areas with intensity based on overlap.

    Args:
        frame (ndarray): The image to draw on.
        forks (list): List of fork dicts containing 'end' coordinates.
        radius (int): Pixel distance to consider forks "close".
        min_overlap (int): Minimum forks needed to trigger convergence glow.

    Returns:
        ndarray: Frame with convergence depth zones highlighted.
    """
    ends = [f["end"] for f in forks]
    density_map = np.zeros(frame.shape[:2], dtype=np.uint8)

    for i, pt in enumerate(ends):
        for j, other in enumerate(ends):
            if i != j:
                dist = np.linalg.norm(np.subtract(pt, other))
                if dist < radius:
                    cv2.circle(density_map, pt, radius, 5, -1)

    # Normalize density map for brightness scaling
    density_normalized = cv2.normalize(density_map, None, 0, 255, cv2.NORM_MINMAX)

    # Apply colormap for visual depth effect (turquoise to red)
    depth_color = cv2.applyColorMap(density_normalized, cv2.COLORMAP_HOT)

    # Blend with original frame
    blended = cv2.addWeighted(frame, 0.8, depth_color, 0.4, 0)

    return blended
