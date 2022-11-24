#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    result = []

    with open(filename, "r") as file:
        file.readline()

        for line in file:
            m = re.search(r"(\d{1,3})\s+(\d{1,3})\s+(\d{1,3})\s+(.+)", line)
            print(m.groups())
            r = m.group(1)
            g = m.group(2)
            b = m.group(3)
            desc = m.group(4)
            result.append("\t".join([r,g,b,desc]))
        
    return result


def main():
    print(red_green_blue("part02-e03_red_green_blue/src//rgb.txt"))

if __name__ == "__main__":
    main()
