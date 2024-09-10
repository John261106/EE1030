import sys   
sys.path.insert(0, '/home/john-bobby/MyRepos/matgeo/codes/CoordGeo')



import numpy as np
import matplotlib.pyplot as plt
import ctypes
import mpmath 

# Load the shared library
lib = ctypes.CDLL('./libvector_norm.so')

# Define the argument and return types of the vector_norm function
lib.vector_norm.argtypes = (ctypes.POINTER(ctypes.c_double), ctypes.c_int)
lib.vector_norm.restype = ctypes.c_double

def calculate_norm(vector):
    vector_c = (ctypes.c_double * len(vector))(*vector)
    norm = lib.vector_norm(vector_c, len(vector))
    return norm

def plot_vector(vector):
    norm = calculate_norm(vector)
    
    # Convert norm to a higher precision using mpmath
    norm_precise = mpmath.nstr(norm, 5)
    
    # Plotting
    fig, ax = plt.subplots()
    ax.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color='r', label=f'Vector ({vector[0]}, {vector[1]})')
    ax.plot([0, vector[0]], [0, vector[1]], 'b-', linewidth=2)
    
    # Setting labels and title
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.axhline(0, color='grey', linestyle='--')
    ax.axvline(0, color='grey', linestyle='--')
    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Vector and Its Norm')
    plt.legend()
    
    # Adding the norm as a label
    mid_point = (vector[0] / 2, vector[1] / 2)
    ax.text(mid_point[0], mid_point[1], f'Norm = {norm_precise}', fontsize=12, ha='right')
    
    plt.grid()
    plt.savefig("Fig1.png")

# Vector (-6, 8)
vector = [-6, 8]
plot_vector(vector)

