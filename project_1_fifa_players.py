# JUMPlus Data Project 1: Fifa Players
# Tristan Kilper

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import dataset
df = pd.read_csv('JUMPlus/Project1FifaPlayers/players_20.csv')

# top 5 records
print(df.head(5))

# show all column names
for col in df.columns:
    print(col)

# show number of rows and columns in the dataset
print(f'Number of rows in dataset: {len(df)}')
print(f'Number of columns in dataset: {len(df.columns)}')

# show top 10 number of players per country
players_by_country = df.groupby(['nationality']).count().sort_values(['sofifa_id'], ascending=False)
print(players_by_country.head(10))
print(players_by_country.head(5).index)

# bar chart of top 5 countries by players
"""x_pos = players_by_country.head(5).index

plt.bar(x_pos, players_by_country.head(5)['sofifa_id'], color='green')
plt.xlabel("Nationality")
plt.ylabel("Number of Players")
plt.title("Top 5 Countries by Number of Players")

plt.xticks(x_pos, players_by_country.head(5)['sofifa_id'])

plt.show()"""