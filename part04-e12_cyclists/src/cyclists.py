#!/usr/bin/env python3

import pandas as pd

def cyclists():
    #df = pd.read_csv("part04-e12_cyclists/src/Helsingin_pyorailijamaarat.csv", sep=';')
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=';')
    cleaned = df.dropna(how='all').dropna(axis=1, how='all')
    return cleaned


def main():
    print(cyclists().shape)
    
if __name__ == "__main__":
    main()
