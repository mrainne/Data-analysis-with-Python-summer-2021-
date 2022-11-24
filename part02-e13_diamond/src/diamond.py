#!/usr/bin/env python3

import numpy as np

def diamond(n): 
    n1 = np.eye(n, dtype=int)[:,::-1] # inverse diagonal matrix
    n2 = np.eye(n, dtype=int)# inverse diagonal matrix
    u = np.concatenate((n1, n2[:, 1:]), axis = 1) # upper part of diamond 
    return np.array(np.concatenate((u,u[-2::-1])))

def main():
    print(diamond(3))
    print(diamond(1))

if __name__ == "__main__":
    main()
