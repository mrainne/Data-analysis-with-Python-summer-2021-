#!/usr/bin/env python3
import numpy as np
import functools

def matrix_power(a, n):

    if n == 0:
        result = np.eye(a.shape[0])
    elif n >= 1:
        result = functools.reduce(np.matmul, (a for _ in range(n)))
    elif n < 0:
        a_inv = np.linalg.inv(a)
        result = functools.reduce(np.matmul, (a_inv for _ in range(-n)))
    
    return result

def main():
    a = np.random.randint(0, 25, (5,5))
    print(a)
    n = np.random.randint(-10, 10)
    print(n)
    print(matrix_power(a, n))
if __name__ == "__main__":
    main()
