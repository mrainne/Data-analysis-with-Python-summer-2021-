#!/usr/bin/env python

import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.linear_model import LinearRegression

days = dict(zip("ma ti ke to pe la su".split(), "Mon Tue Wed Thu Fri Sat Sun".split()))

months = dict(zip("tammi helmi maalis huhti touko kesä heinä elo syys loka marras joulu".split(), range(1, 13)))

def split_date(df):
    d = df["Päivämäärä"].str.split(expand=True)
    d.columns = ["Weekday", "Day", "Month", "Year", "Hour"]
    hourmin = d["Hour"].str.split(":", expand=True)
    d["Hour"] = hourmin.iloc[:, 0]
    d["Weekday"] = d["Weekday"].map(days)
    d["Month"] = d["Month"].map(months)
    d = d.astype({"Weekday": object, "Day": int, "Month": int, "Year": int, "Hour": int})

    return d

def split_date_continues():
    #df = pd.read_csv("part05-e13_cycling_weather_continues/src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = df.dropna(axis=0, how="all").dropna(axis=1, how="all")
    d = split_date(df)
    df = df.drop("Päivämäärä", axis=1)
    
    return pd.concat([d, df], axis=1)

def cycling_weather():
    #wh = pd.read_csv("part05-e13_cycling_weather_continues/src/kumpula-weather-2017.csv")
    wh = pd.read_csv("src/kumpula-weather-2017.csv")
    bike = split_date_continues()
    bike = bike.groupby(['Year', 'Month', 'Day']).sum().reset_index()
    print(bike.info())
    result = pd.merge(wh, bike, left_on=["Year", "m", "d"], right_on=["Year", "Month", "Day"])
    result = result.fillna(method='ffill')
    return result.drop(['m', 'd', 'Time', 'Time zone'], axis=1)


def cycling_weather_continues(station):
    df = cycling_weather()
    X = df[['Precipitation amount (mm)', 'Snow depth (cm)', 'Air temperature (degC)']]
    Y = df[station]

    model = LinearRegression(fit_intercept=True).fit(X, Y)
    return ((model.coef_), model.score(X,Y))
    
def main():
    station = 'Merikannontie'
    coefs, s = cycling_weather_continues(station)

    print('Measuring station:', station)
    print("Regression coefficient for variable 'precipitation': {:.1f}".format(coefs[0]))
    print("Regression coefficient for variable 'snow depth': {:.1f}".format(coefs[1]))
    print("Regression coefficient for variable 'temperature': {:.1f}".format(coefs[2]))
    print("Score: {:.2f}".format(s))




if __name__ == "__main__":
    main()
