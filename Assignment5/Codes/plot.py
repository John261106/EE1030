import sys                                          
sys.path.insert(0, '/home/john-bobby/MyRepos/matgeo/codes/CoordGeo') 
import numpy as np
import matplotlib.pyplot as plt
import ctypes
from line.funcs import *
from triangle.funcs import *
from conics.funcs import *

math_functions = ctypes.CDLL('./parabola.so')


math_functions.compute_values.argtypes = (ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_int)
math_functions.compute_value.argtypes = [ctypes.c_double]
math_functions.compute_value.restype = ctypes.c_double
math_functions.computeArea.argtypes=[ctypes.c_double,ctypes.c_double,ctypes.c_int]
math_functions.computeArea.restype=ctypes.c_double


x = np.linspace(0, 10, 100)  
y = np.zeros_like(x)
A = np.array(([0, math_functions.compute_value(0)])).reshape(-1, 1)
B = np.array(([1, math_functions.compute_value(1)])).reshape(-1, 1)
C = np.array(([1, -1])).reshape(-1, 1)
D = np.array(([1, 7])).reshape(-1, 1)
x_1 = line_gen(C, D)



math_functions.compute_values(x.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),y.ctypes.data_as(ctypes.POINTER(ctypes.c_double)), len(x))
print(f"The Area enclosed by the curve between x=0 and x=1 is {math_functions.computeArea(0,1,1000)}")


plt.ylim([0, 6]) 
plt.plot(x, y, label='y = 2√x')
plt.plot(x_1[0, :], x_1[1, :], label='$x=1$')
plt.annotate(f"A(0.0,{math_functions.compute_value(0)})", (0, math_functions.compute_value(0)), textcoords="offset points", xytext=(20, 5), ha='center')
plt.annotate(f"B(1.0,{math_functions.compute_value(1)})", (1, math_functions.compute_value(1)), textcoords="offset points", xytext=(20, 5), ha='center')
plt.title('Plot of y = 2√x')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.savefig("/home/john-bobby/MyRepos/EE1030/Assignment5/Figs/Fig1.png")

