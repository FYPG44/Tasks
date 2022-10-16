from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
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



     
with open("output_nsh.txt") as f: #insert path to points
        for line in f.readlines():
            tmp = list(map(int, line.rstrip().split(",")))
            i, j, k = tmp[0], tmp[1], tmp[2]
            Entity(model='cube', position = (i,j,k), color = get_color(i,j,k), texture  = 'white_cube')
            

EditorCamera()




app.run()