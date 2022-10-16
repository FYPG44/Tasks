import matplotlib.pyplot as plt
import numpy as np

def plot_td(X, Y, Z):
    x,y,z = np.indices((X, Y, Z))
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    with open("output_nsh.txt") as f:
        for line in f.readlines():
            tmp = list(map(int, line.rstrip().split(",")))
            i, j, k = tmp[0], tmp[1], tmp[2]
            voxel = (x == (i)) & (y == (j)) & (z==(k))
            ax.voxels(voxel, facecolor = "green", edgecolor = "black")
            # ax.scatter(i,j,k)
    
    f.close()
    plt.show()

#   for i in range(len(X[0])):
#     red_voxel = (x == (red_x)) & (y == (red_y)) & (z==(red_z))
#     ax.voxels(red_voxel, facecolor = 'red')

plot_td(30, 40, 50)