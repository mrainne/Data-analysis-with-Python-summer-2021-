#!/usr/bin/env python3

import pandas as pd

def subsetting_with_loc():
    #df = pd.read_csv("part04-e07_subsetting_with_loc/src/municipal.tsv", index_col="Region 2018", sep="\t")
    df = pd.read_csv("src/municipal.tsv", index_col="Region 2018", sep="\t")
    return df.loc["Akaa":"Äänekoski", ["Population", "Share of Swedish-speakers of the population, %", "Share of foreign citizens of the population, %"]] 

def main():
    print(subsetting_with_loc())


if __name__ == "__main__":
    main()
