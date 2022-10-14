from turtle import circle
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
from ursina import * 
from ursina.prefabs.first_person_controller import FirstPersonController

previous = [0] * 100000
X, Y, Z = [], [], []

for i in range(0,2):
  X.append([])
  Y.append([])
  Z.append([])

s = set()

def putpixel(x, y, z):
  zz = int(z)
  zz = zz%2
  X[zz].append(x)
  Y[zz].append(y)
  Z[zz].append(z)

  s.add((x,y,z))
  s.add((x,z,y))
  s.add((y,z,x))
  s.add((y,x,z))
  s.add((z,x,y))
  s.add((z,y,x))


mapy = {}
mapx = {}


def drawCircle(xc, yc, x, y, z, cnt):
  if cnt == 0:
    x1 = xc+x
    y1 = yc+y
    if y1 in mapy.keys():
      mapy[y1] = max(mapy[y1], x1)
    else:
      mapy[y1] = x1
    
    if x1 in mapx.keys():
      mapx[x1] = max(mapx[x1], y1)
    else:
      mapx[x1] = y1

    x1 = xc + y
    y1 = yc + x
    if y1 in mapy.keys():
      mapy[y1] = max(mapy[y1], x1)
    else:
      mapy[y1] = x1
    if x1 in mapx.keys():
      mapx[x1] = max(mapx[x1], y1)
    else:
      mapx[x1] = y1

  putpixel(xc+x, yc+y, z)
  putpixel(xc-x, yc+y, z)
  putpixel(xc+x, yc-y, z)
  putpixel(xc-x, yc-y, z)
  putpixel(xc+y, yc+x, z)
  putpixel(xc-y, yc+x, z)
  putpixel(xc+y, yc-x, z)
  putpixel(xc-y, yc-x, z)


def circleDCS( xc, yc, z, r, cnt):
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
        drawCircle(xc, yc, i, j, z, cnt)
        count1+=1
        s = s + i
        i+=1
        s = s + i
        if s > w:
          break

    psum = psum + previous[k]
    csum = csum + count1
    if psum<csum:
      drawCircle(xc,yc, i-1, j-1, z, cnt)

    previous[k]=count1
    k+=1
    w = w + l
    l = l - 2
    j-=1

#  drawing a circle first on xy plane
cnt = 0
circleDCS(10,10,10,10,cnt)
cnt = 1

# from the previously drawn circle, calculated the gradient by which we have to change z axis and the radius respectively
for key in mapy:
  print(key, mapy[key])
  circleDCS(10,10,key,mapy[key]-10,cnt)
  circleDCS(10,10,20-key,mapy[key]-10,cnt)

for key in mapx:
  print(key, mapx[key])
  circleDCS(10,10,mapx[key],key-10,cnt)
  circleDCS(10,10,20-mapx[key],key-10,cnt)

# writing points in the file
with open("myfile.txt","w") as file1:
  for x,y,z in s:
    file1.write(str(x) + ',' + str(y) + ',' + str(z) + '\n')


def plot_td():
  x,y,z = np.indices((25, 25 , 25))
  fig = plt.figure()
  ax = plt.gca(projection='3d')
  # ax = fig.add_subplot(111, projection='3d')
  for i in range(len(X[0])):
    red_x, red_y, red_z = X[0][i], Y[0][i], Z[0][i]
    red_voxel = (x == (red_x)) & (y == (red_y)) & (z == (red_z))
    ax.voxels(red_voxel, facecolor = 'red', edgecolor = 'black')
    # ax.scatter(red_x,red_y,red_z,c='r')
    
  for i in range(len(X[1])):
    blue_x, blue_y, blue_z = X[1][i], Y[1][i], Z[1][i]
    blue_voxel = (x == (blue_x)) & (y == (blue_y)) & (z == (blue_z))
    ax.voxels(blue_voxel, facecolor = 'blue', edgecolor = 'black')
    # ax.scatter(blue_x,blue_y,blue_z,c='b')

  plt.show()

# plot_td()