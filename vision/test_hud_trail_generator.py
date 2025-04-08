import numpy as np
import matplotlib.pyplot as plt
import math

# Sample trail points (can be replaced with live trail data later)
trail_points = np.array([
    [100, 200],
    [150, 220],
    [200, 180],
    [250, 230],
    [300, 210],
    [350, 240],
    [400, 220],
    [450, 200],
])

def bezier_curve(points, num=300):
    n = len(points) - 1
    curve = np.zeros((num, 2))
    t = np.linspace(0, 1, num)
    for i in range(n + 1):
        binom = math.comb(n, i)
        bernstein = binom * (1 - t) ** (n - i) * t ** i  # shape: (num,)
        curve += np.outer(bernstein, points[i])         # shape: (num, 2)
    return curve

# Generate curve
curve = bezier_curve(trail_points, num=300)

# Plotting the HUD Trail View
plt.figure(figsize=(10, 6))
plt.plot(trail_points[:, 0], trail_points[:, 1], 'o--', alpha=0.4, label='Raw Trail')
plt.plot(curve[:, 0], curve[:, 1], color='cyan', linewidth=2.5, label='Flywheel Curve')
plt.title("RFF HUD Trail → Bezier Curve")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.legend()
plt.gca().set_facecolor("#111111")        # HUD Viewport
plt.gcf().patch.set_facecolor("#000000")  # Full HUD background
plt.show()
