#!/usr/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def fit_line(x, y):
    model = LinearRegression(fit_intercept=True)
    model.fit(x[:,np.newaxis], y)
    slope = model.coef_[0]
    intercept = model.intercept_
    return (slope, intercept)
    return 0, 0
    
def main():
    np.random.seed(0)
    n=20
    x=np.linspace(0, 10, n)
    y=x*2 + 1 + 1*np.random.randn(n)
    s, i = fit_line(x, y)
    print("Slope: {:.1f}".format(s))
    print("Intercept: {}".format(i))
    plt.plot(x,y, 'o')
    plt.plot(x, x*s + i, 'r')
    plt.show()

if __name__ == "__main__":
    main()
