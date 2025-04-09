import cv2

def rewind_trail(image, trail_points, max_frames=10):
    """
    Draws a fading trail to visualize movement history.
    Newer points are brighter; older points fade out.

    Args:
        image: Frame to draw on.
        trail_points: List of (x, y) coordinates.
        max_frames: Number of past points to show.
    """
    if not trail_points:
        return image

    trail_len = min(len(trail_points), max_frames)
    for i in range(trail_len):
        point = trail_points[-(i+1)]
        fade_intensity = 255 - int((i / trail_len) * 200)  # older = dimmer
        color = (0, fade_intensity, 0)  # Green trail with fading
        cv2.circle(image, point, 3, color, -1)

    return image
