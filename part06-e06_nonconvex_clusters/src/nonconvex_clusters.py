#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score
import scipy

def nonconvex_clusters():
    df = pd.read_csv('src/data.tsv', sep='\t')
    X = df[['X1', 'X2']]
    y = df.y

    eps = np.arange(0.05, 0.2, 0.05)
    scores = []
    clusters = []
    outliers = []
    for e in eps:
        model = DBSCAN(eps=e)
        model.fit(X)
        n_labels = len(set(model.labels_))
        n_clusters = n_labels - (1 if -1 in model.labels_ else 0)
        clusters.append(n_clusters)
        outliers.append(list(model.labels_).count(-1))
        if len(set(y)) == n_clusters:
            permutation = find_permutation(n_clusters, y, model.labels_)
            new_labels = [ permutation[label] for label in model.labels_[model.labels_!=-1]]
            scores.append(accuracy_score(y[model.labels_!=-1], new_labels))
        else:
            scores.append(np.nan)

    return pd.DataFrame({'eps' : eps, 'Score': scores, 'Clusters' : clusters, 'Outliers': outliers}).astype(float)

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        if i != -1:
            idx = labels == i
            new_label=scipy.stats.mode(real_labels[idx])[0][0]  # Choose the most common label among data points in the cluster
            permutation.append(new_label)
            
    return permutation

def main():
    print(nonconvex_clusters())

if __name__ == "__main__":
    main()
