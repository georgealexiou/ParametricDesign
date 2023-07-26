import matplotlib.pyplot as plt
import numpy as np

center_x = 1.0
center_y = 1.0
radius = 1.0

theta = np.linspace(0, 2*np.pi, 100)

x = center_x + radius * np.cos(theta)
y = center_y + radius * np.sin(theta)

plt.plot(x, y)
plt.show()
