import ctypes
import matplotlib.pyplot as plt

# Load the shared library

lib = ctypes.CDLL('./section_formula.so')

# Define the argument and return types for the C function
lib.section_formula.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]

# Coordinates of points A and B
A = (4, -3)
B = (8, 5)
ratio_m = 3
ratio_n = 1

# Create variables for the result
x = ctypes.c_double()
y = ctypes.c_double()

# Call the section_formula function
lib.section_formula(A[0], A[1], B[0], B[1], ratio_m, ratio_n, ctypes.byref(x), ctypes.byref(y))

# P coordinates
P = (x.value, y.value)

# Plotting
plt.figure()
plt.xlim(2,10)
plt.ylim(-5,7)
plt.plot([A[0], B[0]], [A[1], B[1]], 'bo-', label='Line segment AB')
plt.plot(A[0], A[1], 'ro', label='Point A (4, -3)')
plt.plot(B[0], B[1], 'go', label='Point B (8, 5)')
plt.plot(P[0], P[1], 'mo', label=f'Point P ({P[0]:.2f}, {P[1]:.2f})')


plt.annotate(f"A({A[0]},{A[1]})",(A[0],A[1]))
plt.annotate(f"B({B[0]},{B[1]})",(B[0],B[1]))
plt.annotate(f"P({P[0]},{P[1]})",(P[0],P[1]))

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Plot of Points A, B, and P')
plt.legend()
plt.grid(True)
plt.savefig("Fig1.png")

