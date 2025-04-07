import numpy as np

def calculate_slope_and_velocity(trail_points):
    """
    Given a list of (x, y) trail points, compute the slope and velocity between each.
    Returns a list of segments with dx, dy, distance, and slope.
    """
    segments = []

    for i in range(1, len(trail_points)):
        x1, y1 = trail_points[i - 1]
        x2, y2 = trail_points[i]
        dx = x2 - x1
        dy = y2 - y1
        distance = np.hypot(dx, dy)
        slope = dy / dx if dx != 0 else float('inf')

        segments.append({
            'start': (x1, y1),
            'end': (x2, y2),
            'dx': dx,
            'dy': dy,
            'distance': distance,
            'slope': slope
        })

    return segments


def detect_wait_zones(segments, threshold=1.5):
    """
    Detects segments where movement is below the velocity threshold.
    Returns a list of wait zone coordinates.
    """
    wait_zones = [seg['end'] for seg in segments if seg['distance'] < threshold]
    return wait_zones
