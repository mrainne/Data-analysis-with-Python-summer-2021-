#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model
from sklearn.linear_model import LinearRegression

def coefficient_of_determination():
    md = pd.read_csv("src/mystery_data.tsv", sep="\t")
    X = md.loc[:, 'X1':'X5'].to_numpy()
    Y = md.Y.to_numpy()
    model = LinearRegression(fit_intercept=True).fit(X,Y)
    r2_all = model.score(X, Y)
    X1 = X[:, 0].reshape(-1, 1)
    model1 = LinearRegression(fit_intercept=True).fit(X1, Y)
    r2_x1 = model1.score(X1,Y)
    X2 = X[:, 1].reshape(-1, 1)
    model2 = LinearRegression(fit_intercept=True).fit(X2, Y)
    r2_x2 = model2.score(X2, Y)
    X3 = X[:, 2].reshape(-1, 1)
    model3 = LinearRegression(fit_intercept=True).fit(X3, Y)
    r2_x3 = model3.score(X3, Y)
    X4 = X[:, 3].reshape(-1, 1)
    model4 = LinearRegression(fit_intercept=True).fit(X4, Y)
    r2_x4 = model4.score(X4, Y)
    X5 = X[:, 4].reshape(-1, 1)
    model5 = LinearRegression(fit_intercept=True).fit(X5, Y)
    r2_x5 = model5.score(X5, Y)
    
    return (r2_all, r2_x1, r2_x2, r2_x3, r2_x4, r2_x5)
    
def main():
    features = ['X', 'X1', 'X2', 'X3', 'X4', 'X5']
    coefficients = coefficient_of_determination()
    for i, c in enumerate(coefficients, 0):
        print("R2-score with feature(s) {}: {}".format(features[i], c))

if __name__ == "__main__":
    main() 
