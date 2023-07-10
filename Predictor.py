##etc



#import
import pandas as pd


#read our data
matches= pd.read_csv("data_21_23.csv")

# test case:
##print(matches.head())##

#intial exploration: find the mean number of goals by city last two seasons##
total_goals=0
def calculate_avg_goals_per_game(df, team_name):
    
    home_matches = df[(df['HomeTeam'] == team_name)]
    away_matches=df[(df['AwayTeam'] == team_name)]
    total_goals = home_matches['FTHG'].sum() + away_matches['FTAG'].sum()
    total_matches = home_matches.shape[0] +away_matches.shape[0]
    avg_goals_per_game = total_goals / total_matches
    return avg_goals_per_game

avg_goals = calculate_avg_goals_per_game(matches, "Man City")
print(avg_goals)
