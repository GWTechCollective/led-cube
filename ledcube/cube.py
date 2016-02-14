import numpy as np

class Pattern:

    def __init__(self):
        self.length = 0
        self.width = 0
        self.height = 0
        self.cursor = 0
        self.frames = []
        self.frame_count = 0

    def add_frame(self, frame):
        self.frame_count += 1
        self.frames.append(frame)

    def remove_frame(self, index):
        self.frame_count -= 1
        self.frame.remove(index)

    def move_frame(self, old_index, new_index):
        self.voxels.insert(new_index, self.voxels.pop(old_index))

    def save(self, filename):
        print(filename)
        pass

    def load(self, filename):
        print(filename)
        pass


class Frame:

    def __init__(self, length, width, height):
        self.values = np.zeros((length, width, height))
        self.duration = 0
