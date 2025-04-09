
import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def render_3d_fork_hud(score_path="models/meta/phantom_score_log.json"):
    try:
        with open(score_path, "r") as f:
            forks = json.load(f)
    except:
        print("[3D HUD] Score log not found.")
        return

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title("RFF 3D Fork Confidence HUD")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Confidence (Z)")

    for fork in forks:
        x0, y0 = fork["start"]
        x1, y1 = fork["end"]
        score = fork["score"]
        dx = x1 - x0
        dy = y1 - y0
        dz = score * 100  # Z = confidence

        ax.quiver(x0, y0, 0, dx, dy, dz, color=(1-score, score, 0), arrow_length_ratio=0.1)

    plt.tight_layout()
    plt.show()
