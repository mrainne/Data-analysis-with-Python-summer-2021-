#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    result = []
    with open(filename, "r") as file:
        for line in file:
            m = re.search(r"(\d{2,}) ([A-Z][a-z]{2}) (\s?\d{1,2}) (\d{2}):(\d{2}) (.*)", line)
            size = int(m.group(1))
            month = m.group(2)
            day = int(m.group(3))
            hour = int(m.group(4))
            minute = int(m.group(5))
            f = m.group(6)
            result.append(tuple([size, month, day, hour, minute, f]))
    return result

def main():
    print(file_listing("part02-e02_file_listing/src/listing.txt"))

if __name__ == "__main__":
    main()
