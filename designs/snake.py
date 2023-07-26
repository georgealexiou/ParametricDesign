import matplotlib.pyplot as plt
import numpy as np

num_points = 1000
num_cycles = 5

# Generate the values for theta
theta = np.linspace(0, num_cycles * 2 * np.pi, num_points)

# Start interactive mode
plt.ion()

# Create the plot
plt.figure()

for i in range(1, 100):  # Update the plot 100 times
    # Define the parametric equations for the x and y coordinates
    frequency_x = 10 + i
    amplitude_x = 1.5 + i / 50
    phase_x = 0.5 + i / 100
    x = amplitude_x * np.cos(frequency_x * theta + phase_x) + 0.2 * np.random.randn(num_points)

    frequency_y = 5 + i
    amplitude_y = 1.0 + i / 100
    phase_y = 1.0 + i / 50
    y = amplitude_y * np.sin(frequency_y * theta + phase_y) + 0.2 * np.random.randn(num_points)

    # Clear the previous plot
    plt.clf()

    # Plot the parametric design with a colormap for color variation
    plt.plot(x, y, color='black', linewidth=1)
    plt.scatter(x, y, c=theta, cmap='twilight', s=5)  # Use 'scatter' to set individual colors
    plt.colorbar()  # Add a colorbar to show the color scale
    plt.axis('equal')
    plt.axis('off')

    # Update the plot
    plt.pause(0.1)  # Add a short pause (in seconds) to view the changes

# Turn off interactive mode after the loop
plt.ioff()

# Keep the plot window open until manually closed
plt.show()
