#!/usr/bin/env python3

import pandas as pd

def top_bands():
    #top40 = pd.read_csv("part05-e03_top_bands/src/UK-top40-1964-1-2.tsv", sep='\t')
    top40 = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep='\t')
    #bands = pd.read_csv("part05-e03_top_bands/src/bands.tsv", sep='\t')
    bands = pd.read_csv("src/bands.tsv", sep='\t')

    # in top 40 list artist name is in uppercase and band name in bands is 
    # title -> merge fails
    # change values in Band column to uppercase
    bands.Band = bands.Band.str.upper()

    top_bands = pd.merge(top40, bands, left_on='Artist', right_on='Band')
    return top_bands

def main():
    print(top_bands())

if __name__ == "__main__":
    main()
