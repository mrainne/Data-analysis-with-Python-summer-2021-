#!/usr/bin/env python3

import pandas as pd

def main():
    #mun_info = pd.read_csv("part04-e03_municipal_information/src/municipal.tsv", sep = "\t")
    mun_info = pd.read_csv("src/municipal.tsv", sep = "\t")
    r, c = mun_info.shape
    print("Shape: " + str(r) + ", " + str(c))
    print("Columns:")
    for item in mun_info.columns:
        print(item)

if __name__ == "__main__":
    main()
