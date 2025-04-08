# Memory and confidence mapping logic
# feedback/rff_memory.py

import json
import os

def build_confidence_map(dream_folder="rff_dreams"):
    confidence_map = {}

    for filename in os.listdir(dream_folder):
        if not filename.endswith(".json"):
            continue
        file_path = os.path.join(dream_folder, filename)
        try:
            with open(file_path, "r") as f:
                dream = json.load(f)
            forks = dream.get("forks", [])
            for fork in forks:
                key = tuple(fork.get("start", [0, 0]))
                direction = fork.get("direction", "wait")
                confidence = fork.get("confidence", 0.0)

                if key not in confidence_map:
                    confidence_map[key] = {"up": 0, "down": 0, "wait": 0}

                confidence_map[key][direction] += confidence
        except Exception as e:
            print(f"[RFF] Skipped corrupted dream file: {filename}")

    return confidence_map
