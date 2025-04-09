import cv2

def render_prediction_overlay(image, forks, label_prefix="PHANTOM", color=(0, 255, 255)):
    """
    Draws fork labels and markers on top of the image.
    """
    if not forks:
        return image

    for i, fork in enumerate(forks):
        pt = fork["point"]
        label = f"{label_prefix} {i+1}"
        conf = f"{int(fork['confidence'] * 100)}%"

        # Draw dot
        cv2.circle(image, pt, 4, color, -1)

        # Draw label
        cv2.putText(image, label, (pt[0] + 6, pt[1] - 6),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.4, color, 1)

        # Draw confidence
        cv2.putText(image, conf, (pt[0] + 6, pt[1] + 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.4, (200, 200, 200), 1)

    return image