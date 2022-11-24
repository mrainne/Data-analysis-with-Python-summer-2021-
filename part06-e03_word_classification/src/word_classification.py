#!/usr/bin/env python3

from collections import Counter
import urllib.request
from lxml import etree

import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn import model_selection

alphabet="abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = set(alphabet)

# Returns a list of Finnish words
def load_finnish():
    finnish_url="https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename="src/kotus-sanalista_v1.xml"
    load_from_net=False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines=[]
            for line in data:
                lines.append(line.decode('utf-8'))
        doc="".join(lines)
    else:
        with open(filename, "rb") as data:
            doc=data.read()
    tree = etree.XML(doc)
    s_elements = tree.xpath('/kotus-sanalista/st/s')
    return list(map(lambda s: s.text, s_elements))

def load_english():
    with open("src/words", encoding="utf-8") as data:
        lines=map(lambda s: s.rstrip(), data.readlines())
    return lines

def get_features(a):
    from sklearn.feature_extraction.text import CountVectorizer

    vec = CountVectorizer(input='content', analyzer='char_wb', vocabulary=alphabet)
    X = vec.fit_transform(a)
    return X.toarray()

def contains_valid_chars(s):
    return set(s).issubset(alphabet_set)

def get_features_and_labels():
    fin = np.array(list(filter(contains_valid_chars, map(np.str.lower, load_finnish()))))
    eng = np.array(list(filter(contains_valid_chars, list(map(np.str.lower, filter(lambda l: (not np.str.isupper(l[0])), load_english())))))) 
    X = np.vstack((get_features(fin), get_features(eng)))

    y_fin = np.zeros((len(fin),1))
    y_eng = np.ones((len(eng),1))
    y = np.vstack((y_fin, y_eng))

    return X, y


def word_classification():
    X, y = get_features_and_labels()
    model = MultinomialNB()
    cvs = cross_val_score(model, X, y, cv=model_selection.KFold(n_splits=5, shuffle=True, random_state=0))

    return cvs


def main():
    print("Accuracy scores are:", word_classification())
    
if __name__ == "__main__":
    main()
