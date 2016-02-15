import numpy as np
import json

class Pattern:

    def __init__(self, dim):
        self.length = dim[0]
        self.width = dim[1]
        self.height = dim[2]
        self.cursor = 0
        self.frames = []
        self.frame_count = 0

    def add_frame(self, frame_values, duration):
        dims = (self.height, self.length, self.width)
        self.frame_count += 1
        self.frames.append(Frame(dims, frame_values, duration))

    def remove_frame(self, index):
        self.frame_count -= 1
        self.frame.remove(index)

    def move_frame(self, old_index, new_index):
        self.voxels.insert(new_index, self.voxels.pop(old_index))

    def save(self, filename):
        print(filename)
        json.dumps(self.frames)
        pass

    def load(self, filename):
        print(filename)
        pass


class Frame:

    def __init__(self,dim, values, duration):
        self.values = np.array(values)
        self.values = self.values.reshape((dim[0], dim[1], dim[2]))
        print(self.values)

        self.duration = duration
