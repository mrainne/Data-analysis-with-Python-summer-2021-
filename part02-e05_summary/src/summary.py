#!/usr/bin/env python3

import sys
import math

def summary(filename):
    nums = []
    with open(filename, "r") as f:
        for line in f:
            try:
                x = float(line)
                nums.append(x)
            except ValueError:
                continue

    s = sum(nums)
    a = s / len(nums)
    d = math.sqrt(sum([(n - a)**2 for n in nums])/(len(nums)-1))
    
    return (s, a, d)

def main():
    for f in sys.argv[1:]: 
        print("File: {} Sum: {:f} Average: {:f} Stddev: {:f}".format(f, *summary(f))) 

if __name__ == "__main__":
    main()
