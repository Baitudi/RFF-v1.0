import numpy as np
from math import cos, sin, radians

class PhantomEngine:
    def __init__(self):
        self.phantom_trails = []
        self.volatility_index = 1.0
        self.dream_map = []

    def inject_failed_forks(self, failed_points):
        """
        Inject fork failures from hallucination memory (drift patterns).
        """
        self.dream_map.extend(failed_points)
        self.volatility_index += 0.1 * len(failed_points)

    def generate_phantom_forks(self, current_position, momentum=1.0):
        """
        Generate invisible forks based on fork drift logic.
        Returns a list of fork prediction dicts.
        """
        forks = []
        np.random.seed(42)  # consistent ghost generation
        angles = [-45, 0, 45]

        for angle in angles:
            drift = self.volatility_index * np.random.uniform(0.8, 1.2)
            dx = int(momentum * drift * cos(radians(angle)))
            dy = int(momentum * drift * sin(radians(angle)))
            phantom_point = (current_position[0] + dx, current_position[1] + dy)
            forks.append({
                "point": phantom_point,
                "confidence": round(np.random.uniform(0.5, 0.9), 2),
                "phantom": True
            })

        self.phantom_trails.append((current_position, forks))
        return forks

    def get_phantom_history(self):
        return self.phantom_trails


# 🔁 Direct test execution
if __name__ == "__main__":
    import pickle
    import os

    def load_phantom_model(path="models/phantom_model_beta.pkl"):
        if not os.path.exists(path):
            print(f"[ERROR] Phantom model not found at: {path}")
            exit()
        with open(path, "rb") as f:
            return pickle.load(f)

    # Initialize engine
    engine = PhantomEngine()

    # Load and inject phantom model
    model = load_phantom_model()
    engine.inject_failed_forks(model["drift_patterns"])

    # Generate forks
    result = engine.generate_phantom_forks(current_position=(100, 100), momentum=1.5)

    print("\n📡 PHANTOM FORKS GENERATED:")
    for fork in result:
        print(fork)
