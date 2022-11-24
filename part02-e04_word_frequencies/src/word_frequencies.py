#!/usr/bin/env python3

def word_frequencies(filename):
    result = dict()

    with open(filename, "r") as f:
        lines = f.readlines()
    
    for line in lines:
        words = line.split()
        for word in words:
            word = word.strip("""!\"#$%&'()*,-./:;?@[]_""")#strip('''!"#$%&\'()*,-./:;?@[]_''')
            if word in result:
                result[word] += 1
            else:
                result[word] = 1
    return result

def main():
    freq = word_frequencies("part02-e04_word_frequencies/src/alice.txt")
    print("The ", freq["The"])
    print("Project", freq["Project"])
    print("Gutenberg", freq["Gutenberg"])
    print("EBook", freq["EBook"])
    print("of", freq["of"])

if __name__ == "__main__":
    main()
