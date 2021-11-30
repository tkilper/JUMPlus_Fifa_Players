# JUMPlus Data Project 1: Fifa Players
# Tristan Kilper

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Import dataset
df = pd.read_csv('JUMPlus/Project1FifaPlayers/JUMPlus_Fifa_Players/players_20.csv')

# top 5 records
print(df.head(5))

# show all column names
for col in df.columns:
    print(col)

# show number of rows and columns in the dataset
print(f'Number of rows in dataset: {len(df)}')
print(f'Number of columns in dataset: {len(df.columns)}')

# show top 10 number of players per country
players_by_country = df.groupby(['nationality'], as_index=False).count().sort_values(['sofifa_id'], ascending=False)
print(players_by_country.head(10))

# bar chart of top 5 countries by players
pbcbar = players_by_country[['nationality','sofifa_id']].head(5)
pbcbar.columns = ['Nationality', 'Number of Players']
sns.barplot(x='Nationality', y='Number of Players', data=pbcbar, color="green")
plt.show()

# show top 5 players' short names and wages
dfsnw = df[['short_name', 'wage_eur']]
top5snw = dfsnw.head(5)
print(top5snw)
# sorting by highest wages
top5snwbywage = dfsnw.sort_values(['wage_eur'], ascending=False).head(5)
print(top5snwbywage)

# bar chart of top 5 players by wage
top5snwbywage.columns = ['Name', 'Wage in Euros']
sns.barplot(x='Name', y='Wage in Euros', data=top5snwbywage)
plt.show()

# Top 10 German Players
gers = df[df['nationality'] == 'Germany']
top10ger = gers.head(10)
print(top10ger)

# Top 5 German Players by height, weight, and wages
# - height
top5gerbyhei = gers.sort_values(['height_cm'], ascending=False).head(5)
print(top5gerbyhei)
# - weight
top5gerbywei = gers.sort_values(['weight_kg'], ascending=False).head(5)
print(top5gerbywei)
# - wages
top5gerbywag = gers.sort_values(['wage_eur'], ascending=False).head(5)
print(top5gerbywag)

# short names and wages of top 5 german players
top5gershortnam_wag = gers[['short_name','wage_eur']].head(5)
print(top5gershortnam_wag)

# short names of top 5 players by shooting
top5bysho_shortnam = df.sort_values(['shooting'], ascending=False).head(5)['short_name']
print(top5bysho_shortnam)

# short name, defending, nationality, club of top 5 players by defending
top5bydef = df.sort_values(['defending'], ascending=False).head(5)[['short_name','defending','nationality','club']]
print(top5bydef)

# Top 5 Real Madrid players
top5rm = df[df['club'] == 'Real Madrid'].head(5)
# - wages
top5rm_wage = top5rm[['wage_eur']]
print(top5rm_wage)
# - shooting
top5rm_sho = top5rm[['shooting']]
print(top5rm_sho)
# - defending
top5rm_def = top5rm[['defending']]
print(top5rm_def)
# - nationality
top5rm_nat = top5rm[['nationality']]
print(top5rm_nat)

# *********************************************
# Bonus
# **********************************************

# All players 23 and over with less than once year on their contract
over_23_low_con = df[df['contract_valid_until'] == 2020]
over_23_low_con = over_23_low_con[over_23_low_con['age'] >= 23]
print(over_23_low_con)