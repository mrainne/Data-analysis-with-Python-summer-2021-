#!/usr/bin/env python3

import pandas as pd
import numpy as np

def special_missing_values():
    #df = pd.read_csv("part04-e14_special_missing_values/src/UK-top40-1964-1-2.tsv", sep='\t')
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep='\t')
    df.replace({'New': None, 'Re' : None}, inplace=True)    
    return df[df['Pos'] > df['LW'].astype(float)]

def main():
    print(special_missing_values())

if __name__ == "__main__":
    main()
