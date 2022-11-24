#!/usr/bin/env python3

def detect_ranges(L):
    # sort list before handling
    sorted_list = sorted(L)

    # create variable for result list
    result = []
    
    i = 1

    while i < len(sorted_list):
        start = sorted_list[i-1] # start of range
        n = sorted_list[i] # next item in list
        if n -  start > 1: # start and n not consecutive numbers
            result.append(start) # add start to result list
            i += 1
        else: # start and n are consecutive numbers
            step = 1
            while start + step in sorted_list:
            # find sequence of consecutive numbers in list 
                n = start + step
                step += 1
                
            result.append((start, n+1)) # add range to result list
            i += step # set i to correct index
    if i == len(sorted_list):
        # add last item to result list
        result.append(sorted_list[-1])
    return result

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)
    L = [-4, -2, 0, 2, 4]
    result = detect_ranges(L)
    print(L)
    print(result)
    L = [1, 2, 4]
    result = detect_ranges(L)
    print(L)
    print(result)
if __name__ == "__main__":
    main()
