from ursina import *
from Spheres.point import Point
step = 10
app = Ursina()
curr = 0
multi_colored = False
points = []
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

with open("trying_sphere.txt") as f: #insert path to points
        for line in f.readlines():
            tmp = list(map(int, line.rstrip().split(",")))
            i, j, k = tmp[0], tmp[1], tmp[2]
            points.append(Point(x = i-10, y = j-10, z = k-10))

def input(key):
    if key == 'up arrow':    
        global curr
        for point in points[curr : curr + step]:
            Entity(model = 'cube', position = (point.x, point.y, point.z), texture = 'white_cube', color =  get_color(point.x, point.y, point.z)) 
        curr += 10 

    if key == 'space':
        for point in points[curr :]:
            Entity(model = 'cube', position = (point.x, point.y, point.z), texture = 'white_cube', color =  get_color(point.x, point.y, point.z)) 




EditorCamera()
app.run()