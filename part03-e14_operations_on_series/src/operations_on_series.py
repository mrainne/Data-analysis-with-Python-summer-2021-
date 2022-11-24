#!/usr/bin/env python3
import pandas as pd

def create_series(L1, L2):
    idx = ['a', 'b', 'c']

    if len(L1) != 3 or len(L2) != 3:
        return (None, None)
    else:
        return (pd.Series(L1, idx), pd.Series(L2, idx))

def modify_series(s1, s2):
    s1["d"] = s2["b"]
    new_s1 = s1
    new_s2 = s2.drop("b")
    return (new_s1, new_s2)
    
def main():
    L1 = [1]
    L2 = [1, 2]
    L3 = [1, 2, 3]
    L4 = [1, 2, 3, 4]
    print(create_series(L1, L1))
    print(create_series(L3, L4))
    s1, s2 = create_series(L3, L3)
    new_s1, new_s2 = modify_series(s1, s2)
    print(new_s1 + new_s2)

if __name__ == "__main__":
    main()
