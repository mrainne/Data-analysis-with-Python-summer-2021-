#!/usr/bin/env python3

import pandas as pd

def best_record_company():
    #top40 = pd.read_csv("part05-e05_best_record_company/src/UK-top40-1964-1-2.tsv", sep='\t')
    top40 = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep='\t')
    
    # find top publisher, group by publisher, count sum of WoC and get
    # publisher with maximum number of weeks
    top_publisher = top40.groupby('Publisher')['WoC'].sum().idxmax()

    return top40[top40.Publisher == top_publisher]

def main():
    print(best_record_company())
    

if __name__ == "__main__":
    main()
