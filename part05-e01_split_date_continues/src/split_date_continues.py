#!/usr/bin/env python3

import pandas as pd

def split_date_continues():
    #cycling_data = pd.read_csv("part04-e16_split_date/src/Helsingin_pyorailijamaarat.csv", sep=';')
    cycling_data = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=';')

    # clean empty rows and columns
    cycling_data = cycling_data.dropna(how='all').dropna(axis=1, how='all')
    
    # split column Päivämäärä into separate columns
    date = cycling_data['Päivämäärä'].str.split(expand=True)

    # rename columns
    date = date.rename(columns={0: 'Weekday', 1: 'Day', 2: 'Month', 3: 'Year', 4: 'Hour'})

    # map weekdays
    date.Weekday = date['Weekday'].map(
            {'ma' : 'Mon', 'ti' : 'Tue', 'ke' : 'Wed', 'to' : 'Thu', 'pe' : 'Fri', 'la' : 'Sat', 'su' : 'Sun'})

    # map months
    date.Month = date.Month.map({
        'tammi' : 1, 'helmi' : 2, 'maalis' : 3, 'huhti' : 4, 'touko' : 5,
        'kesä' : 6, 'heinä' : 7, 'elo' : 8, 'syys' : 9, 'loka' : 10,
        'marras' : 11, 'joulu' : 12})

    # split Hour, get hour and map to int
    date.Hour = date.Hour.str.rsplit(':', 1).str[0]
    
    # drop column 'Päivämäärä'
    cycling_data = cycling_data.drop(columns='Päivämäärä')

    # concat date and cycling-data
    cycling_data = pd.concat([date, cycling_data], axis=1)
    
    # set column types
    cycling_data = cycling_data.astype(
            {"Weekday": object, "Day": int, "Month": int,
                "Year": int, "Hour": int})
   
    return cycling_data

def main():
    df = split_date_continues()
    print("Shape:", df.shape)
    print("Column names:\n", df.columns)
    print(df.head())


if __name__ == "__main__":
    main()
