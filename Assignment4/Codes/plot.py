import sys   
sys.path.insert(0, '/home/john-bobby/MyRepos/matgeo/codes/CoordGeo')
import numpy as np
import matplotlib.pyplot as plt
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen
B = np.array(([-1, -3])).reshape(-1,1)
A = np.array(([1, 3])).reshape(-1,1)
C = np.array(([3, -1])).reshape(-1,1)
D = np.array(([-3, 1])).reshape(-1,1)
x_AB=line_gen(A,B)
x_CD=line_gen(C,D)
plt.plot(x_AB[0,:], x_AB[1,:], label='$AB$')
plt.plot(x_CD[0,:], x_CD[1,:], label='$CD$')
plt.annotate("m(direction vector)", (1,3),textcoords="offset points",xytext=(20,5),ha='center')
plt.annotate("n(normal vector)", (3,-1),textcoords="offset points",xytext=(20,5),ha='center')







ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.savefig("/home/john-bobby/MyRepos/EE1030/Assignment4/Figs/Fig1.png")
