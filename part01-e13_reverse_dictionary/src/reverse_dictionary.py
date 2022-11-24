#!/usr/bin/env python3

def reverse_dictionary(d):
    result = {}
    for key, value in d.items():
        for v in value:
            if v not in result:
                result[v] = [key]
            else:
                result[v].append(key)

    return result

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))

if __name__ == "__main__":
    main()
