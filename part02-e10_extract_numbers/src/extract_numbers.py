#!/usr/bin/env python3

def extract_numbers(s):
    result = []
    i = f = 0

    for item in s.split():
        try:
            i = int(item)
            result.append(i)
        except Exception:
            try:
                f = float(item)
                result.append(f)
            except Exception:
                continue

    return result

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
