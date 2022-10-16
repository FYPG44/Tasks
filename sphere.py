from itertools import permutations
import numpy as n
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt
# import matplotlib
# matplotlib.use('Random')
# import matplotlib.pyplot as plt


def other_points(x, y, z):
    return [(x, y, z), (-x, y, z), (x, -y, z), (-x, -y, z), (x, y, -z), (-x, y, -z), (x, -y, -z), (-x, -y, -z)]

def sphere(r):
    i =0
    j =0
#int k , q , r
    q = r
    k = r
    s = 0
    w = 0
#int v , e,
    e = r-1
    v=e
#int l , p
    p = 2*e
    l = p
#int h
    h = r * r
    S = []
# k0 = q, v0 =e, l0 = p, s0 = w
    while s*3 < h:
        while i <= j:
            S.append((abs(i),abs(j),abs(k)))#: { |i| , |j| ,|k|} ={ i, j, k}}
            #print(S)
            s = s + 2*i + 1
            i= i + 1
            if ( s > v):
                k = k - 1
                v = v + 1
                l = l - 2
        w = w + 2*(j - 1) + 1
        j = j + 1
        if ( w > e) :
            q = k - 1
            e = e + p
            p = p - 2
        i = 0
        k = q
        v = e
        l = p
        s = w
    while ( j <= k) :
        while ( j < k) :
       # s = s.union{(i, j, k): { |i| , |j| ,|k|} ={ i, j, k}} ye wali line aap dekh lena
            S.append((abs(i),abs(j),abs(k)))
            #print(S)
            s = (s + (2*i)) + 1
            i= i + 1
            if ( s > v):
                k = k - 1
                v = v + 1
                l = l - 2
        while (( j == k) and ( s < v)):
                    # s = s.union{(i, j, k): { |i| , |j| ,|k|} ={ i, j, k}}
            S.append((abs(i),abs(j),abs(k)))
                    #print(S)
            s = (s + (2*i)) + 1
            i = i + 1
        w = (w+((j-1)*2))+1
        j = j + 1
        if ( w > e) :
            q = k - 1
            e = e + p
            p = p - 2
        i = 0
        k = q
        v = e
        l = p
        s = w
    return(S)

T=[]
tmp=sphere(20)
print(tmp)
for point in tmp:
    for p in list(permutations([point[0], point[1], point[2]])):
        T.extend(other_points(p[0], p[1], p[2]))


x_val = n.array([x[0] for x in T])
y_val = n.array([x[1] for x in T])
z_val = n.array([x[2] for x in T])
#
#matplotlib.plot(x_val,y_val,z_val)
#
#matplotlib.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#x =[1,2,3,4,5,6,7,8,9,10]
#z =[2,3,3,3,5,7,9,11,9,10]


#
offset = 25
ax.scatter(x_val + offset, y_val + offset, z_val + offset, c='r', marker='o')
#

with open("output.txt", "w") as file1:
    for ind in range(len(x_val)):
        x, y, z = x_val[ind] + offset, y_val[ind] + offset, z_val[ind] + offset
        file1.write(f"{x},{y},{z}\n")

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()
