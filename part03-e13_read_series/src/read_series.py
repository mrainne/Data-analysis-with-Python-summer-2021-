#!/usr/bin/env python3
import pandas as pd

def read_series():
    idx = []
    value = []

    while True:
        line = input("Input index and value separated by whitespace (end = enter):" )
        if line.strip() == "":
            break
        elif len(line.split()) != 2:
            raise TypeError("Invalid input")
        else:
            idx.append(line.split()[0])
            value.append(line.split()[1])

    return pd.Series(value, idx)

def main():
    read_series()

if __name__ == "__main__":
    main()
