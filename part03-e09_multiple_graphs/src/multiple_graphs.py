#!/usr/bin/env python3

import matplotlib.pyplot as plt

def main():
    ax, ay = [2,4,6,7], [4,3,5,1]
    bx, by = [1,2,3,4], [4,2,3,1]
    plt.plot(ax, ay)
    plt.plot(bx, by)
    plt.title("First graph")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.show()

if __name__ == "__main__":
    main()
