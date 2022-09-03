from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np

previous = [0] * 100000

X, Y, Z = [], [], []
for i in range(0,2):
  X.append([])
  Y.append([])
  Z.append([])


def putpixel(x, y, z):
  zz = int(z)
  zz = zz%2
  X[zz].append(x)
  Y[zz].append(y)
  Z[zz].append(z)


def drawCircle(xc, yc, x, y, z):
	putpixel(xc+x, yc+y, z)
	putpixel(xc-x, yc+y, z)
	putpixel(xc+x, yc-y, z)
	putpixel(xc-x, yc-y, z)
	putpixel(xc+y, yc+x, z)
	putpixel(xc-y, yc+x, z)
	putpixel(xc+y, yc-x, z)
	putpixel(xc-y, yc-x, z)


def circleDCS( xc, yc, z, r):
  psum=0
  csum=0
  count1=0
  i = 0
  j = r
  s = 0
  w = r
  l = w<<1
  k = 0

  while (j >= i):
    count1 = 0
    while True:
        drawCircle(xc, yc, i, j, z)
        count1+=1
        s = s + i
        i+=1
        s = s + i
        if s > w:
          break

    psum = psum + previous[k]
    csum = csum + count1
    if psum<csum:
      drawCircle(xc,yc, i-1, j-1, z)

    previous[k]=count1
    k+=1
    w = w + l
    l = l - 2
    j-=1

x = 10
for i in range(10,20):
  for r in range(1,x):
    circleDCS(10, 10, int(i), r)
  x-=1

x = 10
i = 10
while x > 0:
  for r in range(1,x):
    circleDCS(10, 10, int(i), r)
  i-=1
  x-=1


# zline = np.linspace(0, -25, 24)
# xline = np.sin(zline)
# yline = np.cos(zline)
# ax.plot3D(xline, yline, zline, 'gray')

# plt.xlim([-30, 30])
# plt.ylim([-25, 25])


def plot_td():
  x,y,z = np.indices((21, 21 , 21))
  fig = plt.figure()
  ax = plt.gca(projection='3d')
  for i in range(len(X[0])):
    red_x, red_y, red_z = X[0][i], Y[0][i], Z[0][i]
    red_voxel = (x == (red_x)) & (y == (red_y)) & (z == (red_z))
    ax.voxels(red_voxel, facecolor = 'red', edgecolor = 'black')
  for i in range(len(X[1])):
    blue_x, blue_y, blue_z = X[1][i], Y[1][i], Z[1][i]
    blue_voxel = (x == (blue_x)) & (y == (blue_y)) & (z == (blue_z))
    ax.voxels(blue_voxel, facecolor = 'blue', edgecolor = 'black')
  plt.show()

plot_td()
