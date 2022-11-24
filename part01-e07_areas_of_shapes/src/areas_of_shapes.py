#!/usr/bin/env python3

import math


def main():
    while True:
        shape = input("Choose a shape (triangle, rectangle, circle): ")
        if shape == "":
            break
        elif shape == "triangle":
            base = int(input("Give base of the triangle: "))
            height = int(input("Give height of the triangle: "))
            print("The area is {:6f}".format(base * height / 2))
        elif shape == "rectangle":
            width = int(input("Give width of the rectangle: "))
            height = int(input("Give height of the rectangle: "))
            print("The area is {:6f}".format(width * height))
        elif shape == "circle":
            radius = int(input("Give radius of the circle: "))
            print("The area is {:6f}".format(math.pi * radius**2))
        else:
            print("Unknown shape!")

if __name__ == "__main__":
    main()
