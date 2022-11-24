#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression

def mystery_data():
    md = pd.read_csv("src/mystery_data.tsv", sep="\t")
    X = md[['X1', 'X2', 'X3', 'X4', 'X5']].to_numpy()
    Y = md['Y']
    model = LinearRegression(fit_intercept=False)
    model.fit(X, Y)
    return model.coef_

def main():
    coefficients = mystery_data()
    # print the coefficients here
    for i,c in enumerate(coefficients, 1):
        print("Coefficient of X{} is {}".format(i, c))

if __name__ == "__main__":
    main()
