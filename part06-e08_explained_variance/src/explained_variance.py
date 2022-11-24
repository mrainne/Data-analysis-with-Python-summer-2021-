#!/usr/bin/env python3
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

def explained_variance():
    df = pd.read_csv('src/data.tsv', sep='\t')
    pca = PCA()
    pca.fit(df)
    print(df.var(axis=0).to_list())
    print(pca.explained_variance_)
    return df.var(axis=0).to_list(), pca.explained_variance_

def main():
    v, ev = explained_variance()
    print('The variances are:', ' '.join('{:.3f}'.format(var) for var in v))
    print('The explained variances after PCA are:', ' '.join('{:.3f}'.format(var) for var in ev))
    print(sum(v), sum(ev))
    plt.plot(range(1, len(ev)+1), np.cumsum(ev))
    plt.show()
    
if __name__ == "__main__":
    main()
