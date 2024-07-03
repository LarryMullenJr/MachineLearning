#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 20:47:50 2024

@author: mattdumouchel
"""

import pandas as pd

#Load the dataset
df = pd.read_csv('/Users/mattdumouchel/Downloads/results.csv')

#Check for and remove any missing values
df.dropna(inplace=True)

#Display the first few rows of the dataset
df.head()

#Count the number of tuples (rows) in the dataset
num_rows = df.shape[0]
print(f"Number of tuples in the dataset: {num_rows}")

#Count the number of unique tournament names
unique_tournaments = df['tournament'].nunique()
print(f"Number of unique tournament names: {unique_tournaments}")

#Convert the 'date' column to timestamps
df['date'] = pd.to_datetime(df['date'])

#Count the number of matches played in 2018
matches_2018 = df[df['date'].dt.year == 2018].shape[0]
print(f"Number of matches played in 2018: {matches_2018}")

#Calculate home team wins, losses, and draws
home_wins = (df['home_score'] > df['away_score']).sum()
home_losses = (df['home_score'] < df['away_score']).sum()
draws = (df['home_score'] == df['away_score']).sum()

print(f"Home team wins: {home_wins}")
print(f"Home team losses: {home_losses}")
print(f"Draws: {draws}")

import matplotlib.pyplot as plt

#Plot pie chart of wins, losses, and draws
labels = ['Wins', 'Losses', 'Draws']
sizes = [home_wins, home_losses, draws]
colors = ['#ff9999','#66b3ff','#99ff99']
explode = (0.1, 0, 0)  # explode 1st slice

plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Home Team Wins, Losses, and Draws')
plt.axis('equal')
plt.show()

#Plot pie chart of the neutral column
neutral_counts = df['neutral'].value_counts()
neutral_counts.plot.pie(autopct='%1.1f%%', shadow=True, startangle=140, colors=['#ff9999','#66b3ff'])
plt.title('Neutral Matches')
plt.axis('equal')
plt.show()

#Count the number of unique team names
unique_teams = pd.concat([df['home_team'], df['away_team']]).nunique()
print(f"Number of unique team names: {unique_teams}")