import cv2
from visual.flywheel_curve_renderer import draw_flywheel_curve

def draw_ghost_overlay(image, forks, center_color=(0, 255, 0), glow_thickness=2):
    """
    Draws ghost forks on top of the input image using flywheel glow effect.
    - forks: List of fork dictionaries with 'point', 'confidence', and 'phantom' keys
    - image: Base frame to draw on
    """
    if not forks:
        return image

    base_point = forks[0]["point"]

    # Draw center marker
    cv2.circle(image, base_point, 5, center_color, -1)

    # Draw directional curves
    image = draw_flywheel_curve(image, forks, center_color=center_color, thickness=glow_thickness)

    # Annotate forks with confidence
    for fork in forks:
        pt = fork["point"]
        label = f"{int(fork['confidence'] * 100)}%"
        cv2.putText(image, label, (pt[0] + 6, pt[1] - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (180, 255, 180), 1)

    return image

def draw_ghost_memory(image, forks, glow_color=(180, 180, 255)):
    """
    Draws ghost forks from memory logs in soft faded style.
    """
    if not forks:
        return image

    for fork in forks:
        end = fork["end"]
        correct = fork.get("correct", False)

        # Green for correct, red for wrong
        color = (0, 255, 0) if correct else (0, 0, 255)
        cv2.circle(image, end, 4, color, -1)

    return image
