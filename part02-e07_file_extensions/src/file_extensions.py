#!/usr/bin/env python3
import sys

def file_extensions(filename):
    extensions = {}
    no_extension =[]
    with open(filename, "r") as f:
        lines = f.readlines()
        
    for line in lines:
        l = line.strip()

        ls = l.split(".")
        if len(ls) == 1:
            no_extension.append(l)
        else:
            e = ls[-1]
            if e not in extensions:
                extensions[e] = [l]
            else:
                extensions[e].append(l)

    return (no_extension, extensions)

def main():
    fe = file_extensions("part02-e07_file_extensions/src/filenames.txt")
    print("{} files with no extension".format(len(fe[0])))

    for k, v in sorted(fe[1].items()):
        print(k, len(v))
if __name__ == "__main__":
    main()
