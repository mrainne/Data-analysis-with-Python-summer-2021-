#!/usr/bin/env python3

import pandas as pd
import numpy as np

def last_week():
    singles = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep='\t')
    #singles = pd.read_csv("part04-e15_last_week/src/UK-top40-1964-1-2.tsv", sep='\t')
    m = (singles["LW"] == "New") | (singles["LW"] == "Re")
    singles.loc[m, "LW"] = np.nan
    singles["LW"] = pd.to_numeric(singles["LW"])

    # sort by column LW and drop rows with missing data
    sortedByLW = singles.dropna().sort_values('LW')
     
    # set correct Peak Pos
    sortedByLW['Peak Pos'] = sortedByLW['Peak Pos'].where(
            (sortedByLW['Peak Pos'] == sortedByLW.LW) | 
            (sortedByLW['Peak Pos'] < sortedByLW.Pos), axis=0)

    # set correct WoC
    sortedByLW.WoC = sortedByLW.WoC - 1
    
    # replace missing LW values with null values
    sortedByLW = sortedByLW.set_index('LW').reindex(range(1, 41)).reset_index()
    
    # set Pos to LW
    sortedByLW.Pos = sortedByLW.LW

    # set LW to Nan
    sortedByLW.LW = np.nan

    return sortedByLW

def main():
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)


if __name__ == "__main__":
    main()
