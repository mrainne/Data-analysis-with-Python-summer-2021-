#!/usr/bin/env python3

import pandas as pd


def cycling_weather():
    #cycling_data = pd.read_csv("part05-e02_cycling_weather/src/Helsingin_pyorailijamaarat.csv", sep=';')
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
    
    # set column types
    date = date.astype(
            {"Weekday": object, "Day": int, "Month": int,
                "Year": int, "Hour": int})
    
    # concatenate data and cycling_data 
    cycling_data = pd.concat([date, cycling_data], axis=1)

    # read weather data
    #weather_data = pd.read_csv("part05-e02_cycling_weather/src/kumpula-weather-2017.csv", sep=',')
    weather_data = pd.read_csv("src/kumpula-weather-2017.csv", sep=',')

    # merge dataframes
    cycling_weather = pd.merge(cycling_data, weather_data, left_on=['Year', 'Month', 'Day'], right_on=['Year', 'm', 'd']).drop(columns=['m', 'd', 'Time', 'Time zone'])
    return cycling_weather

def main():
    print(cycling_weather().head)

if __name__ == "__main__":
    main()
