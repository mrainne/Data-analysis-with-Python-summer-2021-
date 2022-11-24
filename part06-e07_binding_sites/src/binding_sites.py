#!/usr/bin/env python3

import pandas as pd
import numpy as np
import scipy
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score
from sklearn.metrics import pairwise_distances

from matplotlib import pyplot as plt

import seaborn as sns
sns.set(color_codes=True)
import scipy.spatial as sp
import scipy.cluster.hierarchy as hc

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        new_label=scipy.stats.mode(real_labels[idx])[0][0]  # Choose the most common label among data points in the cluster
        permutation.append(new_label)
    return permutation

def toint(x):    
    return dict(zip('ACGT', [0, 1, 2, 3]))[x]

def get_features_and_labels(filename):
    df = pd.read_csv(filename, sep='\t')
    X = df.X.map(lambda x: [toint(it) for it in list(x)])
    y = df.y
    return (np.array(X.to_list()), np.array(df.y))

def plot(distances, method='average', affinity='euclidean'):
    mylinkage = hc.linkage(sp.distance.squareform(distances), method=method)
    g=sns.clustermap(distances, row_linkage=mylinkage, col_linkage=mylinkage )
    g.fig.suptitle(f"Hierarchical clustering using {method} linkage and {affinity} affinity")
    plt.show()

def cluster_euclidean(filename):
    X, y = get_features_and_labels(filename)
    clustering = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='average')
    y_pred = clustering.fit_predict(X)
    permutation = find_permutation(2, y, y_pred)
    new_labels = [ permutation[label] for label in y_pred]
    return accuracy_score(y, new_labels)

def cluster_hamming(filename):
    X, y = get_features_and_labels(filename)
    distances = pairwise_distances(X, metric='hamming')
    clustering = AgglomerativeClustering(n_clusters=2, affinity='precomputed', linkage='average')
    y_pred = clustering.fit_predict(distances)
    permutation = find_permutation(2, y, y_pred)
    new_labels = [ permutation[label] for label in y_pred]
    return accuracy_score(y, new_labels)

def main():
    print("Accuracy score with Euclidean affinity is", cluster_euclidean("src/data.seq"))
    print("Accuracy score with Hamming affinity is", cluster_hamming("src/data.seq"))

if __name__ == "__main__":
    main()
