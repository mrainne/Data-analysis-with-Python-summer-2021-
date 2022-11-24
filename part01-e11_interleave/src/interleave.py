#!/usr/bin/env python3

def interleave(*lists):
    result = []
    for item in list(zip(*lists)):
        result.extend(item)
    return result

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
