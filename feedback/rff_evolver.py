# feedback/rff_evolver.py

import os
import json
import shutil

def evolve_from_dreams(dream_folder="rff_dreams", evolved_folder="rff_dreams_evolved"):
    if not os.path.exists(evolved_folder):
        os.makedirs(evolved_folder)

    evolved_data = []

    for filename in os.listdir(dream_folder):
        if not filename.endswith(".json"):
            continue
        source_path = os.path.join(dream_folder, filename)
        dest_path = os.path.join(evolved_folder, filename)

        try:
            with open(source_path, "r") as f:
                dream = json.load(f)

            forks = dream.get("forks", [])
            filtered_forks = [f for f in forks if f.get("confidence", 0.0) >= 0.25]

            evolved_data.extend(filtered_forks)

            shutil.copy2(source_path, dest_path)

        except Exception as e:
            print(f"[RFF] Failed evolving: {filename} — {e}")

    return evolved_data
