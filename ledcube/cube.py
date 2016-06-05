import numpy as np


class Pattern:
    def __init__(self, dim):
        self.length = dim[0]
        self.width = dim[1]
        self.height = dim[2]
        self.cursor = 0
        self.frames = []

    def add_frame(self, index, frame_values, duration):

        dims = (self.height, self.length, self.width)

        if self.frames:
            self.frames.insert(index, Frame(dims, frame_values, duration))
        else:
            self.frames.append(Frame(dims, frame_values, duration))

    def save_frame(self, index, frame_values, duration):
        dims = (self.height, self.length, self.width)
        self.frames[index] = Frame(dims, frame_values, duration)

    def remove_frame(self, index):
        self.frames.pop(index)

    def get_frame(self, index):
        frame_values = self.frames[index].values.reshape(self.length * self.height * self.width)
        return list(frame_values)

    def move_frame_up(self, index):
        self.frames.insert(index - 1, self.frames.pop(index))

    def move_frame_down(self, index):
        self.frames.insert(index + 1, self.frames.pop(index))

    def save(self, filename):
        pass

    def load(self, filename):
        print(filename)
        pass


class Frame:
    def __init__(self, dim, values, duration):
        self.values = np.array(values)
        self.values = self.values.reshape((dim[0], dim[1], dim[2]))
        print(self.values)

        self.duration = duration
