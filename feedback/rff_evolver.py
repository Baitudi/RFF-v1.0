import os
import json

DREAM_DIR = "rff_dreams"
CONF_MAP_FILE = "confidence_map.json"

def evolve_from_dreams():
    if not os.path.exists(CONF_MAP_FILE):
        print("No existing confidence map. Run rff_memory first.")
        return

    with open(CONF_MAP_FILE, "r") as f:
        confidence_map = json.load(f)

    updated_map = confidence_map.copy()

    for dream_file in os.listdir(DREAM_DIR):
        if dream_file.endswith(".json"):
            try:
                with open(os.path.join(DREAM_DIR, dream_file)) as f:
                    dream_data = json.load(f)
            except json.JSONDecodeError:
                print(f"[RFF] Skipped corrupted dream file: {dream_file}")
                continue

            decision = dream_data["dreams"][0]["original_decision"]
            chart = dream_data["chart"]
            key = str((chart, decision))

            for dream in dream_data["dreams"]:
                if key not in updated_map:
                    updated_map[key] = {"confidence": 0.0, "total": 0}
                entry = updated_map[key]

                entry["total"] += 1
                if dream["simulated_outcome"] == "success":
                    entry["confidence"] = min(100.0, entry["confidence"] + 1.0)
                else:
                    entry["confidence"] = max(0.0, entry["confidence"] - 1.0)

    with open(CONF_MAP_FILE, "w") as f:
        json.dump(updated_map, f, indent=2)

    print("Confidence map evolved using dream data.")
