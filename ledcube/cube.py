import numpy as np

class Pattern:

    def __init__(self):
        self.length = 0
        self.width = 0
        self.height = 0
        self.cursor = 0
        self.voxels = []
        self.voxel_count = 0

    def add_voxel(self, voxel):
        self.voxel_count += 1
        self.voxels.append(voxel)

    def remove_voxel(self, index):
        self.voxel_count -= 1
        self.voxels.remove(index)

    def move_voxel(self, old_index, new_index):
        self.voxels.insert(new_index, self.voxels.pop(old_index))


class Voxel:

    def __init__(self, length, width, height):
        self.values = np.zeros((length, width, height))
        self.duration = 0
