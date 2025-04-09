import pickle
import os

def load_phantom_model(path="models/phantom_model_beta.pkl"):
    """
    Loads the phantom model from disk.
    Returns a dictionary containing:
    - drift_patterns: List of XY drift tuples
    - fork_confidence_map: {'up': float, 'down': float, 'wait': float}
    - bias_profile: Model bias info (momentum drag, reflex delay, decay)
    - version: Model version string
    """
    if not os.path.exists(path):
        print(f"[ERROR] Phantom model not found at: {path}")
        return None

    with open(path, "rb") as f:
        try:
            model_data = pickle.load(f)
            print(f"[LOADED] Phantom model (v{model_data.get('version', 'unknown')})")
            return model_data
        except Exception as e:
            print(f"[ERROR] Failed to load phantom model: {e}")
            return None

# Example usage:
if __name__ == "__main__":
    model = load_phantom_model()
    if model:
        print("Drift Patterns:", model["drift_patterns"])
        print("Fork Confidence:", model["fork_confidence_map"])
        print("Bias Profile:", model["bias_profile"])
