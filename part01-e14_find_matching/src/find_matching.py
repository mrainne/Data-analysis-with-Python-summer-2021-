#!/usr/bin/env python3

def find_matching(L, pattern):
    result = []
    for i, item in enumerate(L):
        if pattern in item:
            result.append(i)
    return result

def main():
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))

if __name__ == "__main__":
    main()
