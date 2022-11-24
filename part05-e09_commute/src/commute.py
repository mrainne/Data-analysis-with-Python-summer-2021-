#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

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
    #df = pd.read_csv("part05-e09_commute/src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = df.dropna(axis=0, how="all").dropna(axis=1, how="all")
    d = split_date(df)
    df = df.drop("Päivämäärä", axis=1)
    result = pd.concat([d, df], axis=1)

    return result

def bicycle_timeseries():
    cycling_data = split_date_continues()

    cycling_data['Päivämäärä'] = pd.to_datetime(
            cycling_data[['Day', 'Month', 'Year', 'Hour']])

    cycling_data = cycling_data.set_index('Päivämäärä')
    return cycling_data

def commute():
    cycling_timeseries = bicycle_timeseries()
    r = pd.date_range("2017-08-01 00:00:00", "2017-08-31 23:00:00", freq='H')
    cycling_timeseries = cycling_timeseries.loc[r,:].set_index('Weekday').groupby(r.weekday+1).apply(sum).drop(columns=['Day', 'Month', 'Year', 'Hour'])
    return cycling_timeseries
    
def main():
    weekdays="x mon tue wed thu fri sat sun".title().split()
    commute_data = commute()
    print(commute_data)
    plt.gca().set_xticklabels(weekdays)
    plt.plot(commute_data)
    plt.show()



if __name__ == "__main__":
    main()
