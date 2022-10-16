from abc import abstractmethod
from turtle import color

class Sphere:
    def __init__(self, radius = 10) -> None:
        self.points = []
        self.voxel_count = 0
        self.radius = radius

    @abstractmethod
    def generate(self):
        pass

    def get_voxel_count(self):
        self.voxel_count = len(list(set(self.points)))

    
