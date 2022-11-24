#!/usr/bin/env python3
import gzip
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes
from sklearn.metrics import accuracy_score

def spam_detection(random_state=0, fraction=1.0):
    spam_file = 'src/spam.txt.gz'
    ham_file = 'src/ham.txt.gz'
    with gzip.open(spam_file, 'rb') as sf:
        spam_content = sf.readlines()
    with gzip.open(ham_file, 'rb') as hf:
        ham_content = hf.readlines()

    spam = np.array(spam_content[:int(len(spam_content)*fraction)])#[:int(len(spam_content)*fraction)]
    ham = np.array(ham_content[:int(len(ham_content)*fraction)])#.split())#[:int(len(ham_content)*fraction)]
    print(spam.shape, ham.shape)
    f = np.concatenate((ham, spam), axis=0)
    lh = np.zeros((ham.shape))
    ls = np.ones((spam.shape))
    l = np.concatenate((lh, ls), axis=0)
    vec = CountVectorizer()
    X = vec.fit_transform(f)
    
    X_train, X_test, y_train, y_test = train_test_split(X, l, train_size=0.75, random_state=random_state)

    model = naive_bayes.MultinomialNB().fit(X_train, y_train)
    pred = model.predict(X_test)
    
    score = accuracy_score(pred, y_test)

    return score, X_test.shape[0], (y_test != pred).sum() 

def main():
    accuracy, total, misclassified = spam_detection()
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")

if __name__ == "__main__":
    main()
