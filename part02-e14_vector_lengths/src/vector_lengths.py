#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):
    return np.array(np.sqrt(np.sum(a**2, axis=1)))

def main():
     a = np.random.randint(0, 10, (3,4))
     print(vector_lengths(a))

if __name__ == "__main__":
    main()
