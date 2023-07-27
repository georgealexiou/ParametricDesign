import matplotlib.pyplot as plt
import numpy as np

num_points = 1000
num_cycles = 10

theta = np.linspace(0, num_cycles * 1 * np.pi, num_points)

x = np.cos( theta) + 0.5 * np.cos(20 * theta)
y = np.sin(3 * theta) + 0.5 * np.sin(20 * theta)

colors = theta / (num_cycles * 2 * np.pi)

plt.scatter(x, y, c=colors, cmap='viridis', s=10)
plt.colorbar()
plt.axis('equal')
plt.axis('off')
plt.show()
