import cv2

class TrailRewinder:
    def __init__(self):
        self.frames = []
        self.index = -1

    def add_frame(self, frame):
        """
        Adds a new frame to the rewind buffer.
        """
        self.frames.append(frame.copy())
        self.index = len(self.frames) - 1

    def step_back(self):
        """
        Goes one step backward in the frame buffer.
        """
        if self.index > 0:
            self.index -= 1
        return self.frames[self.index] if self.frames else None

    def step_forward(self):
        """
        Goes one step forward in the frame buffer.
        """
        if self.index < len(self.frames) - 1:
            self.index += 1
        return self.frames[self.index] if self.frames else None

    def current(self):
        """
        Returns the current frame in view.
        """
        return self.frames[self.index] if self.frames else None

    def reset(self):
        """
        Clears the rewind memory buffer.
        """
        self.frames = []
        self.index = -1
