import matplotlib.pyplot as plt
import numpy as np


def cool_pattern(size=100, frequencies=(1, 2, 3), amplitudes=(1, 1, 1), levels=50):
    x = np.linspace(-1, 1, size)
    y = np.linspace(-1, 1, size)
    X, Y = np.meshgrid(x, y)

    # Convert Cartesian (X,Y) to polar (R,Theta)
    R = np.sqrt(X**2 + Y**2)
    Theta = np.arctan2(Y, X)

    pattern = np.zeros((size, size))

    for freq, amp in zip(frequencies, amplitudes):
        wave = amp * np.sin(np.sqrt(R) * freq * np.pi * Theta)
        pattern += wave

    pattern = np.round(pattern * levels) / levels

    return pattern

def plot_cool_pattern(pattern):
    plt.imshow(pattern, cmap='gray', interpolation='nearest')
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    size = 500
    frequencies = (5, 15, 25)
    amplitudes = (1, 0.6, 0.3)
    levels = 20
    pattern = cool_pattern(size, frequencies, amplitudes, levels)
    plot_cool_pattern(pattern)
