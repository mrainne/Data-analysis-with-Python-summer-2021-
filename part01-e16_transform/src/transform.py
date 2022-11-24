#!/usr/bin/env python3

def transform(s1, s2):
    L1 = list(map(int, s1.split()))
    L2 = list(map(int, s2.split()))

    return [x*y for x,y in list(zip(L1, L2))]

def main():
    print(transform("1 5 3", "2 6 -1"))

if __name__ == "__main__":
    main()
