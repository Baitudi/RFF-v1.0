import cv2
import numpy as np

def draw_flywheel_curve(image, forks, center_color=(255, 255, 255), thickness=2):
    """
    Draws directional curved forks from a central point using bezier-style lines.
    """
    if not forks or len(forks) < 1:
        return image

    base = forks[0]["point"]
    for fork in forks:
        end = fork["point"]
        confidence = fork.get("confidence", 0.5)
        phantom = fork.get("phantom", False)

        # Style based on confidence
        if phantom:
            color = (100, 255, 100) if confidence > 0.7 else (50, 180, 50)
        else:
            color = (0, 255, 255)

        # Curve path (midpoint curve)
        mid = ((base[0] + end[0]) // 2, (base[1] + end[1]) // 2 - 30)
        pts = np.array([base, mid, end], np.int32).reshape((-1, 1, 2))
        cv2.polylines(image, [pts], isClosed=False, color=color, thickness=thickness, lineType=cv2.LINE_AA)

    return image