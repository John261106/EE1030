import sys   
sys.path.insert(0, '/home/john-bobby/MyRepos/matgeo/codes/CoordGeo')
import numpy as np
import matplotlib.pyplot as plt
import ctypes 
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen
libnorm=ctypes.CDLL('./libnorm.so')
libnorm.norm.argtypes = [ctypes.POINTER(ctypes.c_double)]
libnorm.norm.restype = ctypes.c_double
vector=np.array([-6,8],dtype=np.double)
vector_pointer=vector.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
vector_norm=libnorm.norm(vector_pointer);
print(vector_norm)

O = np.array(([0, 0])).reshape(-1,1)
A = np.array(([-6, 8])).reshape(-1,1)
x_OA=line_gen(O,A)
tri_coords = np.block([[O,A]])

plt.plot(x_OA[0,:], x_OA[1,:], label='$0A$')
plt.annotate("O\n(0,0)", (0,0),textcoords="offset points",xytext=(20,5),ha='center')
plt.annotate("A\n(-6,8)", (-6,8),textcoords="offset points",xytext=(20,5),ha='center')
plt.annotate(f'Norm={vector_norm}',(-3,4),textcoords="offset points",xytext=(20,5),ha='center')
plt.scatter(tri_coords[0,:], tri_coords[1,:])
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.savefig("/home/john-bobby/MyRepos/EE1030/Assignment3/Figs/Fig1.png")


