import math
import numpy as np

class PhantomEngine:
    def __init__(self):
        self.memory = []
        self.failed_forks = []
        self.correct_forks = []
        self.last_direction = None

    def record_fork(self, origin, end, is_success):
        fork = {
            "origin": origin,
            "end": end,
            "angle": self._calculate_angle(origin, end)
        }
        self.memory.append(fork)

        if is_success:
            self.correct_forks.append(end)
        else:
            self.failed_forks.append(end)

    def _calculate_angle(self, start, end):
        dx, dy = end[0] - start[0], end[1] - start[1]
        return math.degrees(math.atan2(dy, dx))

    def most_common_direction(self):
        if not self.memory:
            return None
        angles = [f["angle"] for f in self.memory]
        avg_angle = sum(angles) / len(angles)
        self.last_direction = avg_angle
        return avg_angle

    def get_ghost_path(self, steps=5, length=40):
        """
        Generates a forward path in the direction of memory's average angle.
        """
        if not self.last_direction:
            self.most_common_direction()

        if self.last_direction is None:
            return []

        rad = math.radians(self.last_direction)
        direction = (math.cos(rad) * length, math.sin(rad) * length)
        ghost_path = []
        x, y = self.memory[-1]["end"] if self.memory else (300, 300)

        for _ in range(steps):
            x += direction[0]
            y += direction[1]
            ghost_path.append((int(x), int(y)))

        return ghost_path

    def get_memory(self):
        return self.memory

    def get_failures(self):
        return self.failed_forks

    def get_successes(self):
        return self.correct_forks
