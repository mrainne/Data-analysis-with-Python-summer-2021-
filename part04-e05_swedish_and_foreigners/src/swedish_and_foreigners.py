#!/usr/bin/env python3

import pandas as pd

def swedish_and_foreigners():
    #df = pd.read_csv("part04-e05_swedish_and_foreigners/src/municipal.tsv", sep="\t", index_col="Region 2018")
    df = pd.read_csv("src/municipal.tsv", sep="\t", index_col="Region 2018")
    df2 = df["Akaa":"Äänekoski"]
    df3 = df2[(df2["Share of Swedish-speakers of the population, %"] > 5) & (df2["Share of foreign citizens of the population, %"] > 5)][["Population", "Share of Swedish-speakers of the population, %", "Share of foreign citizens of the population, %"]]
    
    return df3

def main():
    print(swedish_and_foreigners())

if __name__ == "__main__":
    main()
