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
    
    if df[(df['HomeTeam'] == team_name):
        total_goals =total_goals+ team_matches['FTHG'].sum()
    elif (df['AwayTeam'] == team_name)]:
        total_goals = total_goals + team_matches['FTAG'].sum()
                    
    team_matches = df[(df['HomeTeam'] == team_name) | (df['AwayTeam'] == team_name)]
    total_matches = team_matches.shape[0]
    avg_goals_per_game = total_goals / total_matches
    return avg_goals_per_game

avg_goals = calculate_avg_goals_per_game(matches, "Man City")
print(avg_goals)
