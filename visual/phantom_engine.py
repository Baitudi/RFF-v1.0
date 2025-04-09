import numpy as np

class PhantomEngine:
    def __init__(self):
        self.phantom_trails = []
        self.volatility_index = 1.0  # base scale
        self.dream_map = []

    def inject_failed_forks(self, failed_points):
        """
        Learn from past fork failures to adjust phantom fork generation.
        """
        self.dream_map.extend(failed_points)
        self.volatility_index += 0.1 * len(failed_points)

    def generate_phantom_forks(self, current_position, momentum=1.0):
        """
        Simulate invisible forks using ghost pattern logic.
        """
        forks = []
        np.random.seed(42)  # deterministic for test
        angles = [-45, 0, 45]
        for angle in angles:
            drift = self.volatility_index * np.random.uniform(0.8, 1.2)
            dx = int(momentum * drift * np.cos(np.radians(angle)))
            dy = int(momentum * drift * np.sin(np.radians(angle)))
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