#!/usr/bin/env python3


def main():
    for i in range(1, 11):
        t = triple(i)
        s = square(i)
        if t < s:
            break

        print("triple("+str(i)+")=="+str(t)+" square("+str(i)+")=="+str(s))

def triple(num):
    return 3 * num

def square(num):
    return num ** 2

if __name__ == "__main__":
    main()
