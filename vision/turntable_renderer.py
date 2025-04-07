import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def render_turntable(x, y, z, forks):
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title('RFF Turntable HUD — Trail + Fork Intelligence')
    ax.plot(x, y, z, color='cyan', linewidth=2, label='Main Trail (Tt)')

    for idx, fork in enumerate(forks):
        ax.plot(fork[0], fork[1], fork[2], linestyle='--', linewidth=1.5,
                label=f'Fork {idx+1}')

    ax.set_xlabel('Chart Progression')
    ax.set_ylabel('Momentum')
    ax.set_zlabel('Hyper Depth')
    ax.grid(True)
    ax.legend()
    plt.tight_layout()
    plt.show()