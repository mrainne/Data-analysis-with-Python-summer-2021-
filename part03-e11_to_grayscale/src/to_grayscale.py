#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def to_grayscale(p):
    p_copy = p.copy()
    return np.dot(p_copy, [0.2126, 0.7152, 0.0722])

def to_red(p):
    p_copy = p.copy()
    p_copy[:, :, 1:] = 0
    return p_copy

def to_green(p):
    p_copy = p.copy()
    p_copy[:,:, 0] = 0
    p_copy[:,:, 2] = 0
    return p_copy

def to_blue(p):
    p_copy = p.copy()
    p_copy[:, :, :2] = 0
    return p_copy

def main():
    painting = plt.imread("src/painting.png")
    #painting = plt.imread("part03-e11_to_grayscale/src/painting.png")

    plt.imshow(to_grayscale(painting), cmap=plt.set_cmap("gray"))

    plt.subplot(3,1,1)
    plt.imshow(to_red(painting))
    plt.subplot(3,1,2)
    plt.imshow(to_green(painting))
    plt.subplot(3,1,3)
    plt.imshow(to_blue(painting))
    plt.show()

if __name__ == "__main__":
    main()
