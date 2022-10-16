from ursina import *
from Spheres.sphere import Sphere

class Sphere_Visualizer:
    def __init__(self, sphere : Sphere, label = 'sphere', multi_colored = False) -> None:
        self.sphere = sphere
        self.label = label
        self.color = color.blue
        self.multi_colored = multi_colored

    def one_shot(self):
        app = Ursina()
        for point in self.sphere.points:
            point.get_color()
            Entity(model = 'cube', position = (point.x, point.y, point.z), texture = 'white_cube', color = self.color if not self.multi_colored else point.color)
        EditorCamera()
        app.run()

    def phase_plot(self, step = 10):
        self.sphere.get_voxel_count()
        app = Ursina()
        curr = 0
        EditorCamera()
        app.run()
        while curr <= self.sphere.voxel_count:
            for point in self.sphere.points[curr : curr + step]:
                point.get_color()
                Entity(model = 'cube', position = (point.x, point.y, point.z), texture = 'white_cube', color = self.color if not self.multi_colored else point.color) 
                curr += 10   
        

        



    