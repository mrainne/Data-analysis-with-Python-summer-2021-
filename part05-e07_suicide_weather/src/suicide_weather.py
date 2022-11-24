#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    #suicide_data = pd.read_csv("part05-e07_suicide_weather/src/who_suicide_statistics.csv")
    suicide_data = pd.read_csv("src/who_suicide_statistics.csv")

    frac_of_suicides_per_pop = suicide_data.groupby('country').apply(lambda df: (df['suicides_no']/df['population']).mean())
    frac_of_suicides_per_pop = frac_of_suicides_per_pop.rename('frac_of_suicides_per_pop')
    
    return frac_of_suicides_per_pop 

def suicide_weather():
    suicide_fracs_per_pop = suicide_fractions()
    s_fracs = suicide_fracs_per_pop.size

    #weather = pd.read_html("part05-e07_suicide_weather/src/List_of_countries_by_average_yearly_temperature.html", header=0, index_col=0)
    weather = pd.read_html("src/List_of_countries_by_average_yearly_temperature.html", header=0, index_col=0) 

    weather[0]['Average yearly temperature (1961–1990, degrees Celsius)'].str.replace('−', '-').astype(float)

    w_size = weather[0].size

    suicide_weather =  pd.merge(weather[0], suicide_fracs_per_pop, left_index=True, right_index=True)

    s_w_size = suicide_weather.shape[0]

    temperature = suicide_weather['Average yearly temperature (1961–1990, degrees Celsius)'].str.replace('\u2212', '-').astype(float)
    fracs = suicide_weather['frac_of_suicides_per_pop']

    spearman_corr = temperature.corr(fracs, method='spearman')
    return (s_fracs, w_size, s_w_size, spearman_corr)

def main():
    s_r, t_r, c_r, c = suicide_weather()
    print("Suicide DataFrame has {} rows".format(s_r))
    print("Temperature DataFrame has {} rows".format(t_r))
    print("Common DataFrame has {} rows".format(c_r))
    print("Spearman correlation: {:.1f}".format(c))

if __name__ == "__main__":
    main()
