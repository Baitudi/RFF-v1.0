import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def simulate_live_trail():
    x = np.linspace(-10, 10, 400)
    y = np.sin(x) + 0.2 * np.cos(2 * x)
    z = np.cos(x) * 0.8 + 0.1 * np.random.randn(len(x))
    return x, y, z

def generate_dynamic_fork(x, y, z):
    slope = np.gradient(y, x)
    angle_map = np.clip(slope, -1, 1) * 0.75
    confidence = np.clip(1 - np.abs(np.gradient(slope)), 0.1, 1.0)
    fy = y + np.sin(angle_map * x) * confidence
    fz = z + np.cos(angle_map * x) * confidence
    glow = confidence * 1.8
    return fy, fz, glow

def render_fork_hud(x, y, z, fy, fz, glow):
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title("RFF Phase 6.3 — Live Trail + Fork Intelligence HUD")

    ax.plot(x, y, z, color='cyan', linewidth=2, label='Live Trail')
    ax.plot(x, fy, fz, color='lime', linestyle='--', linewidth=2, label='Fork Path')
    ax.scatter(x, fy, fz, c=glow, cmap='spring', alpha=0.5, s=10)

    ax.set_xlabel("Chart Progression")
    ax.set_ylabel("Momentum")
    ax.set_zlabel("Hyper Depth")
    ax.legend()
    plt.tight_layout()
    plt.show()