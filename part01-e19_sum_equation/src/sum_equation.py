#!/usr/bin/env python3
from functools import reduce
def sum_equation(L):
    if len(L) == 0:
        result = "0 = 0"
    else:
        result = " + ".join(map(str, L)) + " = " + str(reduce(lambda x,y: x+y, L, 0))
    return result
def main():
    print(sum_equation([1,5,7]))

if __name__ == "__main__":
    main()
