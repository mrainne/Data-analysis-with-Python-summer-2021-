#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def center(a):
    y, x = a.shape[:2]
        
    center_y = (y-1)/2
    center_x = (x-1)/2
    
    return (center_y, center_x)   # note the order: (center_y, center_x)

def radial_distance(a):
    mid_y, mid_x = center(a)
    indices = np.indices(a.shape[:2]) # create an array of indices of a
    # indices[0] = row indices, indices[1] = column indices
    result = np.sqrt((indices[1]-mid_x)**2+(indices[0]-mid_y)**2)
    
    return result

def scale(a, tmin=0.0, tmax=1.0):

    """Returns a copy of array 'a' with its values scaled to be in the range
[tmin,tmax]."""
    a_copy = a.copy()
    r = np.max(a_copy) - np.min(a_copy)

    # min-max-scaling
    scale = tmin + (a_copy - np.min(a_copy))*(tmax - tmin)/r

    return np.zeros_like(a_copy) if r == 0 else scale 

def radial_mask(a):
    rm = 1 - scale(radial_distance(a), 0.0, 1.0)

    return rm 

def radial_fade(a):
    return a * radial_mask(a)[:,:, np.newaxis]

def main():
    painting = plt.imread("src/painting.png")
    #painting = plt.imread("part03-e12_radial_fade/src/painting.png")
    
    plt.subplot(3,1,1)
    plt.imshow(painting)
    plt.subplot(3,1,2)
    plt.imshow(radial_mask(painting))
    plt.subplot(3,1,3)
    plt.imshow(radial_fade(painting))
    plt.show()
if __name__ == "__main__":
    main()
