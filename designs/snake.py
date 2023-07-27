import matplotlib.pyplot as plt
import numpy as np

num_points = 1000
num_cycles = 5

theta = np.linspace(0, num_cycles * 2 * np.pi, num_points)

plt.ion()

plt.figure()

for i in range(1, 100):
    frequency_x = 10 + i
    amplitude_x = 1.5 + i / 50
    phase_x = 0.5 + i / 100
    x = amplitude_x * np.cos(frequency_x * theta + phase_x) + 0.2 * np.random.randn(num_points)

    frequency_y = 5 + i
    amplitude_y = 1.0 + i / 100
    phase_y = 1.0 + i / 50
    y = amplitude_y * np.sin(frequency_y * theta + phase_y) + 0.2 * np.random.randn(num_points)

    plt.clf()

    plt.plot(x, y, color='black', linewidth=1)
    plt.scatter(x, y, c=theta, cmap='twilight', s=5)
    plt.colorbar()
    plt.axis('equal')
    plt.axis('off')

    plt.pause(0.1)

plt.ioff()

plt.show()
