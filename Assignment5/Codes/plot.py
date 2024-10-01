import sys                                          
sys.path.insert(0, '/home/john-bobby/MyRepos/matgeo/codes/CoordGeo') 
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import ctypes
      
from line.funcs import *
from triangle.funcs import *
from conics.funcs import *
libparabola=ctypes.CDLL('./parabola.so')
libparabola.parabola.argtypes = [ctypes.c_double]
libparabola.parabola.restype = ctypes.c_double

x1 = 0
x2 = 1
y1 = libparabola.parabola(x1)
y2 = libparabola.parabola(x2)
A = np.array(([x1, y1])).reshape(-1, 1)
B = np.array(([x2, y2])).reshape(-1, 1)
C = np.array(([x2, 0])).reshape(-1, 1)
x_1 = line_gen(C, B)

# Setting up plot with increased figure size
fig = plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
ax = fig.add_subplot(111, aspect='equal')
len = 100
y = np.linspace(-8, 8, len)

# Conic parameters
V = np.array(([0, 0], [0, 1]))
u = -2 * e1
f = 0

n, c, F, p = conic_param(V, u, f)

# Eigenvalues and eigenvectors
D_vec, P = LA.eig(V)
D = np.diag(D_vec)

# Standard parabola parameters
eta = 2 * u.T @ p
flen = -eta / D_vec[1]

# Standard parabola generation
x = parab_gen(y, flen)

# Affine Parabola parameters
cA = np.block([u + eta * p * 0.5, V]).T
cb = np.block([[-f], [0.5 * eta * p - u]])
O = LA.lstsq(cA, cb, rcond=None)[0]  # vertex

# Affine parabola generation
xStandardparab = np.block([[x], [y]])
Of = O.flatten()
xActualparab = P @ xStandardparab + Of[:, np.newaxis]

# Filter for the upper half of the parabola (y >= 0)
upper_half_indices = xActualparab[1, :] >= 0
xActualparab_upper = xActualparab[:, upper_half_indices]

# Plotting
plt.plot(xActualparab_upper[0, :], xActualparab_upper[1, :], label='Parabola', color='r')
plt.plot(x_1[0, :], x_1[1, :], label='$x=1$')
plt.annotate("A(0,0)", (x1, y1), textcoords="offset points", xytext=(20, 5), ha='center')
plt.annotate("B(1,2)", (x2, y2), textcoords="offset points", xytext=(20, 5), ha='center')



# Use set_position
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

plt.legend(loc='best')
plt.grid()  # minor

plt.savefig("/home/john-bobby/MyRepos/EE1030/Assignment5/Figs/Fig1.png")

