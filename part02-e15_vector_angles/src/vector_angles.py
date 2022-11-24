#!/usr/bin/env python3

import numpy as np
import scipy.linalg

def vector_angles(X, Y):
    inner_prod = np.sum(X*Y)
    c = inner_prod / (scipy.linalg.norm(X) * scipy.linalg.norm(Y))
    
    return np.degrees(np.arccos(np.clip(c, -1, 1)))

def main():
    X = np.array([[0, 0 ,1], [1, 1, 0]])
    Y = np.array([[0, 0, 1], [1, 1, 0]])
    print(vector_angles(X, Y))

if __name__ == "__main__":
    main()
