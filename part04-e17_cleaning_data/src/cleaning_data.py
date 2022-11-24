#!/usr/bin/env python3

import pandas as pd
import numpy as np


def cleaning_data():
    #ps = pd.read_csv("part04-e17_cleaning_data/src/presidents.tsv", sep="\t")
    ps = pd.read_csv("src/presidents.tsv", sep="\t")
    
    # set President to correct form
    # 1. find Presidents where name is in format lastname, firstname
    # 2. split these
    # 3. change the order to firstname, lastname
    # 4. join names
    ps.President = ps.President.where(~ps.President.str.contains(','), ps.President.str.split(',').str[::-1].str.join(' ')).str.strip()

    # clean Start
    # remove addional information with splitting
    # select first object
    # map to integer
    ps.Start = ps.Start.str.split().str[0].map(int)

    # clean Last
    # find incorrect format and set to NaN
    # set dtype to float
    ps.Last = ps.Last.where(ps.Last != '-').astype(float)

    # clean Seasons
    # find incorrect format with where
    # map incorrect value ('two') to correct (2)
    # map dtype to integer
    ps.Seasons = ps.Seasons.where(ps.Seasons != 'two', ps.Seasons.map({'two' : 2})).map(int)
    
    # Clean Vice-presidents (same as Presidents)
    # set capital letters to both names
    ps['Vice-president'] = ps['Vice-president'].where(~ps['Vice-president'].str.contains(','), ps['Vice-president'].str.split(',').str[::-1].str.join(' ')).str.title().str.strip()
    
    return ps

def main():
    print(cleaning_data())

if __name__ == "__main__":
    main()
