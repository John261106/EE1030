import matplotlib.pyplot as plt

# Read the data from the file
x = []
y = []
labels = []
text=["A","B","P"]

with open('data.txt', 'r') as file:
    for line in file:
        values = line.split()
        x_val = float(values[0])
        y_val = float(values[1])
        x.append(x_val)
        y.append(y_val)
        labels.append(f'({x_val}, {y_val})')

# Plot the data
plt.scatter(x, y, color='red', label='Data Points')
plt.plot(x, y, linestyle='-', color='blue', alpha=0.5)  # Optional line connecting points

# Label the coordinates
for i, label in enumerate(labels):
    plt.text(x[i], y[i], label, fontsize=9, ha='right')
    plt.annotate(text[i],(x[i],y[i]))
    

# Add titles and labels

plt.title('Plot of A, B and P')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

# Display the plot
plt.grid(True)
plt.savefig("Fig1.png")

