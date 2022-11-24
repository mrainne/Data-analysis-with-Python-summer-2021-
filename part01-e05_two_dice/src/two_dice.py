#!/usr/bin/env python3

def main():
    # dice 1
    for dice1 in range(1,7):
        for dice2 in range(1,7):
            if dice1 + dice2 == 5:
                print((dice1,dice2))
            continue

if __name__ == "__main__":
    main()
