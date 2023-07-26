import matplotlib.pyplot as plt
import numpy as np

num_points = 1000
num_cycles = 10

# Generate the values for theta
theta = np.linspace(0, num_cycles * 1 * np.pi, num_points)

# Define the parametric equations for the x and y coordinates
x = np.cos( theta) + 0.5 * np.cos(20 * theta)
y = np.sin(3 * theta) + 0.5 * np.sin(20 * theta)

# Create an array of colors based on the theta values to change gradually
colors = theta / (num_cycles * 2 * np.pi)

# Plot the parametric design with gradually changing colors
plt.scatter(x, y, c=colors, cmap='viridis', s=10)  # Use 'scatter' instead of 'plot' to set individual colors
plt.colorbar()  # Add a colorbar to show the color scale
plt.axis('equal')
plt.axis('off')
plt.show()
