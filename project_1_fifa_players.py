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

#