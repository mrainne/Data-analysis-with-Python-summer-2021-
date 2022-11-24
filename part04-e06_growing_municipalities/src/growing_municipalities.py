#!/usr/bin/env python3

import pandas as pd

def growing_municipalities(df):
    growing = df[df["Population change from the previous year, %"]>0]

    return growing.shape[0]/df.shape[0]

def main():
    df = pd.read_csv("src/municipal.tsv", sep="\t", index_col="Region 2018")
    #df = pd.read_csv("part04-e06_growing_municipalities/src/municipal.tsv", sep="\t", index_col="Region 2018")
    print("Proportion of growing municipalities: {:.1f}%".format(growing_municipalities(df["Akaa":"Äänekoski"])))

if __name__ == "__main__":
    main()
