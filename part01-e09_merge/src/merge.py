#!/usr/bin/env python3

def merge(L1, L2):
    merged = []
    i, j = 0, 00

    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            merged.append(L1[i])
            i += 1
        else:
            merged.append(L2[j])
            j += 1

    merged = merged + L1[i:] + L2[j:]
    return merged

def main():
    print(merge(sorted([3,2,1]),[4,5,6]))
    print(merge([1, 3, 5], [2, 4, 6]))
    print(merge([2, 6, 8], [1, 3, 7]))
    print(merge([7,8,9], [1,2,3]))

if __name__ == "__main__":
    main()
