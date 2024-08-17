import numpy as np
import matplotlib.pyplot as plt


A = (4, -3)
B = (8, 5)
P = (7, 3)


x_coords = [A[0], B[0], P[0], A[0]]
y_coords = [A[1], B[1], P[1], A[1]]


plt.figure(figsize=(8, 6))


plt.plot(x_coords, y_coords, 'bo-') 


plt.text(A[0], A[1], f'A{A}', fontsize=12, verticalalignment='bottom', horizontalalignment='right')
plt.text(B[0], B[1], f'B{B}', fontsize=12, verticalalignment='bottom', horizontalalignment='right')
plt.text(P[0], P[1], f'P{P}', fontsize=12, verticalalignment='bottom', horizontalalignment='right')


plt.title('Plot of Points A, B, and P')
plt.xlabel('X coordinate')
plt.ylabel('Y coordinate')


plt.gca().set_aspect('equal', adjustable='box')


plt.grid(True)


plt.show()

