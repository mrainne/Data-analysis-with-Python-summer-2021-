#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def subfigures(a):
    x = a[:, 0]
    y = a[:, 1]
    colors = a[:, 2]
    sizes = a[:, 3]

    plt.subplot(1, 2, 1)
    plt.plot(x, y)
    plt.subplot(1, 2, 2)
    plt.scatter(x, y, c=colors, s=sizes)
    plt.show()


def main():
    a = np.random.randint(0, 50, (5, 4))
    subfigures(a)

if __name__ == "__main__":
    main()
