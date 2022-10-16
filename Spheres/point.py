from ursina import color
class Point:
    def __init__(self, x = 0, y = 0, z = 0) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.color = color.gray 

    def get_color(self):
        if self.z >= 0:
            if self.x >= 0 and self.y >= 0:
                self.color = color.red
            elif self.x >= 0 and self.y < 0:
                self.color = color.blue
            elif self.x < 0 and self.y < 0:
                self.color = color.green
            elif self.x < 0 and self.y >= 0:
                self.color = color.yellow

        else:
            if self.x >= 0 and self.y >= 0:
                self.color = color.black
            elif self.x >= 0 and self.y < 0:
                self.color = color.gray
            elif self.x < 0 and self.y < 0:
                self.color = color.orange
            elif self.x < 0 and self.y >= 0:
                self.color = color.white
        self.color = color.cyan
        return self.color

    def plot_48_voxels(self):
        points = []
        x, y, z = self.x, self.y, self.z
        points.extend(self.__plot_all_signs(x,y,z))
        points.extend(self.__plot_all_signs(x,z,y))
        points.extend(self.__plot_all_signs(y,z,x))
        points.extend(self.__plot_all_signs(y,x,z))
        points.extend(self.__plot_all_signs(z,x,y))
        points.extend(self.__plot_all_signs(z,y,x))
        return points 


    def __plot_all_signs(self, i, j, k):
        return [Point(x = i, y = j, z = k), Point(x = -i, y = j, z = k), Point(x = -i, y = -j, z = k), Point(x = -i, y = -j, z = -k), Point(x = i, y = -j, z = k), Point(x = i, y = -j, z = -k), Point(x = i, y = j, z = -k), Point(x = -i, y = j, z = -k)]

        
        

