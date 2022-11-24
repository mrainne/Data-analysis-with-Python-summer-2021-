#!/usr/bin/env python3

import pandas as pd

def below_zero():
    #df = pd.read_csv("part04-e11_below_zero/src/kumpula-weather-2017.csv")
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    return df["d"][df["Air temperature (degC)"] < 0].count()

def main():
    bz = below_zero()
    print("Number of days below zero: {}".format(bz))
    
if __name__ == "__main__":
    main()
