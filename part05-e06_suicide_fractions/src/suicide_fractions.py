#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    #suicide_data = pd.read_csv("part05-e06_suicide_fractions/src/who_suicide_statistics.csv")
    suicide_data = pd.read_csv("src/who_suicide_statistics.csv") 

    frac_of_suicides_per_pop = suicide_data.groupby('country').apply(lambda df: (df['suicides_no']/df['population']).mean())
    return frac_of_suicides_per_pop

def main():
    print(suicide_fractions().head)

if __name__ == "__main__":
    main()
