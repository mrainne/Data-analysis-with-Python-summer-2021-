#!/usr/bin/env python3

import sys

def file_count(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    line_count = len(lines)
    words = [w for l in lines for w in l.split()]
    word_count = len(words)
    char_count = sum(len(l) for l in lines)
    return (line_count, word_count, char_count)

def main():
    for f in sys.argv[1:]:
        print("{}\t{}\t{}\t{}".format(*file_count(f), f))

if __name__ == "__main__":
    main()
