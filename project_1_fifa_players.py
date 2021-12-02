# JUMPlus Data Project 1: Fifa Players
# Tristan Kilper

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Import dataset
print('1) Load the csv and show the top 5 records')
print('****************************************************')
df = pd.read_csv('JUMPlus/Project1FifaPlayers/JUMPlus_Fifa_Players/players_20.csv')

# top 5 records
print(df.head(5))
print('****************************************************')
print(' ')

# show all column names
print('2) Show all column names')
print('****************************************************')
for col in df.columns:
    print(col)
print('****************************************************')
print(' ')

# show number of rows and columns in the dataset
print('3) Show the number of rows and columns in the dataset')
print('****************************************************')
print(f'Number of rows in dataset: {len(df)}')
print(f'Number of columns in dataset: {len(df.columns)}')
print('****************************************************')
print(' ')

# show top 10 number of players per country
print('4,5) Show the records of the top 10 countries by number of players')
print('****************************************************')
players_by_country = df.groupby(['nationality'], as_index=False).count().sort_values(['sofifa_id'], ascending=False)
print(players_by_country.head(10))
print('****************************************************')
print(' ')

# bar chart of top 5 countries by players
print('6) Create a bar plot of top 5 countries by number of players with green bars')
print('****************************************************')
pbcbar = players_by_country[['nationality','sofifa_id']].head(5)
pbcbar.columns = ['Nationality', 'Number of Players']
sns.barplot(x='Nationality', y='Number of Players', data=pbcbar, color="green")
plt.show()
print('****************************************************')
print(' ')

# show top 5 players' short names and wages
print('7) Show the top 5 players\' short names and wages')
print('****************************************************')
dfsnw = df[['short_name', 'wage_eur']]
top5snw = dfsnw.head(5)
print(top5snw)
print('****************************************************')
print(' ')
# sorting by highest wages
print('8) Show the short names and wages of the top 5 players by salary')
print('****************************************************')
top5snwbywage = dfsnw.sort_values(['wage_eur'], ascending=False).head(5)
print(top5snwbywage)
print('****************************************************')
print(' ')

# bar chart of top 5 players by wage
print('9) Create a bar plot of the top 5 players by wage')
print('****************************************************')
top5snwbywage.columns = ['Name', 'Wage in Euros']
sns.barplot(x='Name', y='Wage in Euros', data=top5snwbywage)
plt.show()
print('****************************************************')
print(' ')

# Top 10 German Players
print('10) Show the top 10 records of players with German nationality')
print('****************************************************')
gers = df[df['nationality'] == 'Germany']
top10ger = gers.head(10)
print(top10ger)
print('****************************************************')
print(' ')

# Top 5 German Players by height, weight, and wages
print('11) Show top 5 German players by height, weight, and wages')
print('****************************************************')
# - height
print('Height:')
top5gerbyhei = gers.sort_values(['height_cm'], ascending=False).head(5)
print(top5gerbyhei)
# - weight
print('Weight:')
top5gerbywei = gers.sort_values(['weight_kg'], ascending=False).head(5)
print(top5gerbywei)
# - wages
print('Wages:')
top5gerbywag = gers.sort_values(['wage_eur'], ascending=False).head(5)
print(top5gerbywag)
print('****************************************************')
print(' ')

# short names and wages of top 5 german players
print('12) Show the short names and wages of the top 5 German players')
print('****************************************************')
top5gershortnam_wag = gers[['short_name','wage_eur']].head(5)
print(top5gershortnam_wag)
print('****************************************************')
print(' ')

# short names of top 5 players by shooting
print('13) Show the short names of the top 5 players by shooting')
print('****************************************************')
top5bysho_shortnam = df.sort_values(['shooting'], ascending=False).head(5)['short_name']
print(top5bysho_shortnam)
print('****************************************************')
print(' ')

# short name, defending, nationality, club of top 5 players by defending
print('14) Show the short name, defending, nationality, and club of the top 5 players by defending')
print('****************************************************')
top5bydef = df.sort_values(['defending'], ascending=False).head(5)[['short_name','defending','nationality','club']]
print(top5bydef)
print('****************************************************')
print(' ')

# Top 5 Real Madrid players
top5rm = df[df['club'] == 'Real Madrid'].head(5)
# - wages
print('15) Show the wages of the top 5 players on Real Madrid')
print('****************************************************')
top5rm_wage = top5rm[['wage_eur']]
print(top5rm_wage)
print('****************************************************')
print(' ')
# - shooting
print('16) Show the shooting of the top 5 players on Real Madrid')
print('****************************************************')
top5rm_sho = top5rm[['shooting']]
print(top5rm_sho)
print('****************************************************')
print(' ')
# - defending
print('17) Show the defending of the top 5 players on Real Madrid')
print('****************************************************')
top5rm_def = top5rm[['defending']]
print(top5rm_def)
print('****************************************************')
print(' ')
# - nationality
print('18) Show the nationality of the top 5 players on Real Madrid')
print('****************************************************')
top5rm_nat = top5rm[['nationality']]
print(top5rm_nat)
print('****************************************************')
print(' ')

# *********************************************
# Bonus
# **********************************************

# All players 23 and over with less than once year on their contract
print('Bonus) Show players 23 and over with less than one year on their contract')
print('****************************************************')
over_23_low_con = df[df['contract_valid_until'] == df['contract_valid_until'].min()]
over_23_low_con = over_23_low_con[over_23_low_con['age'] >= 23]
print(over_23_low_con[['short_name','age','player_positions','overall','potential','wage_eur']])
print('****************************************************')