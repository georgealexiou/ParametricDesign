import matplotlib.pyplot as plt
import numpy as np


def cool_pattern(size=100, frequencies=(5, 10, 15), amplitudes=(1, 0.5, 0.2)):
    x = np.linspace(-1, 1, size)
    y = np.linspace(-1, 1, size)
    X, Y = np.meshgrid(x, y)

    pattern = np.zeros((size, size))

    for freq, amp in zip(frequencies, amplitudes):
        wave = amp * np.sin(freq * np.pi * X) * np.cos(freq * np.pi * Y)
        pattern += wave

    return pattern

def plot_cool_pattern(pattern):
    pattern = (pattern - np.min(pattern)) / (np.max(pattern) - np.min(pattern))  # normalize to 0-1
    plt.imshow(pattern, cmap='gray', interpolation='bilinear')
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    size = 300
    frequencies = (2, 8, 15)
    amplitudes = (1, 0.6, 0.3)
    pattern = cool_pattern(size, frequencies, amplitudes)
    plot_cool_pattern(pattern)
