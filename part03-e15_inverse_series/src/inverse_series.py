#!/usr/bin/env python3

import pandas as pd

def inverse_series(s):
    return pd.Series(s.index, s.values)

def main():
    s1 = pd.Series([1, 2, 3], ['a', 'b', 'c'])
    print(inverse_series(s1))
    s2 = pd.Series([1, 1, 2], ['a', 'b', 'c'])
    print(inverse_series(s2))

if __name__ == "__main__":
    main()
