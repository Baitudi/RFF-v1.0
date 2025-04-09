
import numpy as np

def generate_terrain_field(image, trail, forks):
    field = np.zeros_like(image[:, :, 0])
    for fork in forks:
        x, y = fork["end"]
        cv2.circle(field, (x, y), 10, 100, -1)
    for pt in trail:
        x, y = pt
        cv2.circle(field, (x, y), 5, 200, -1)
    return field
