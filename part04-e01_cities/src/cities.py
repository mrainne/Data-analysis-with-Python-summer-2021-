#!/usr/bin/env python3

import pandas as pd

def cities():
    c = ["Helsinki", "Espoo", "Tampere", "Vantaa", "Oulu"]
    p = [643272, 279044, 231853, 223027, 201810]
    a = [715.48, 528.03, 689.59, 240.35, 3817.52]
    return pd.DataFrame({"Population" : p, "Total area" : a}, index = c) 
    
def main():
    print(cities())

if __name__ == "__main__":
    main()
