
import json
import os

SCORE_PATH = "models/meta/phantom_score_log.json"

def decay_memory(threshold=0.4, decay_rate=0.05):
    if not os.path.exists(SCORE_PATH):
        print("[MemoryForgiveness] No memory log found.")
        return

    with open(SCORE_PATH, "r") as f:
        forks = json.load(f)

    updated = []
    for fork in forks:
        score = fork.get("score", 1.0)
        if score < threshold:
            score *= (1 - decay_rate)
        fork["score"] = max(0.0, round(score, 3))
        updated.append(fork)

    with open(SCORE_PATH, "w") as f:
        json.dump(updated, f, indent=2)

    print(f"[MemoryForgiveness] Decayed {len(updated)} fork scores.")
