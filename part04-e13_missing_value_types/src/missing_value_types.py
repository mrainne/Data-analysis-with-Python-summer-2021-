#!/usr/bin/env python3

import pandas as pd
import numpy as np

def missing_value_types():
    state = ['United Kingdom', 'Finland', 'USA', 'Sweden', 'Germany', 'Russia']
    year_of_independence = [np.nan, 1917, 1776, 1523, np.nan, 1992]
    president = [None, 'Niinistö', 'Trump', None, 'Steinmeier', 'Putin']

    return pd.DataFrame({'Year of independence': year_of_independence, 'President' : president}, index=state)
               
def main():
    print(missing_value_types())

if __name__ == "__main__":
    main()
