#!/usr/bin/env python3

import pandas as pd

def average_temperature():
    #df = pd.read_csv("part04-e10_average_temperature/src/kumpula-weather-2017.csv")
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    return df["Air temperature (degC)"][df["m"] == 7].mean()


def main():
    print("Average temperature in July: {:.1f}".format(average_temperature()))

if __name__ == "__main__":
    main()
