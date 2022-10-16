from Spheres.Andres.andres import Andres
from Spheres.sphere_visualizer import Sphere_Visualizer
from ursina import *

sphere = Andres()
sphere.generate()
sphere.get_voxel_count()
step = 10
app = Ursina()
curr = 0
multi_colored = False

def get_color(x, y, z):
    if z >= 0:
        if x >= 0 and y >= 0:
            return color.red
        elif x >= 0 and y < 0:
            return color.blue
        elif x < 0 and y < 0:
            return color.green
        elif x < 0 and y >= 0:
            return color.yellow

    else:
        if x >= 0 and y >= 0:
            return color.black
        elif x >= 0 and y < 0:
            return color.gray
        elif x < 0 and y < 0:
            return color.orange
        elif x < 0 and y >= 0:
            return color.white
    return color.cyan

def one_shot():
    for point in sphere.points:
        Entity(model = 'cube', position = (point.x, point.y, point.z), texture = 'white_cube', color =  get_color(point.x, point.y, point.z))

def input(key):
    if key == 'up arrow':    
        global curr
        for point in sphere.points[curr : curr + step]:
            Entity(model = 'cube', position = (point.x, point.y, point.z), texture = 'white_cube', color =  get_color(point.x, point.y, point.z)) 
        curr += 10 

    if key == 'space':
        for point in sphere.points[curr :]:
            Entity(model = 'cube', position = (point.x, point.y, point.z), texture = 'white_cube', color =  get_color(point.x, point.y, point.z)) 




EditorCamera()
app.run()





