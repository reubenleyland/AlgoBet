##etc



#import
import pandas as pd


#read our data
matches= pd.read_csv("data_21_23.csv")

# test case:
##print(matches.head())##



##standard data analysis steps:Functions of use


##A function to calculate the av goals of a team
total_goals=0
def calculate_avg_goals_per_game_scored(df, team_name):
    
    home_matches = df[(df['HomeTeam'] == team_name)]
    away_matches=df[(df['AwayTeam'] == team_name)]
    total_goals = home_matches['FTHG'].sum() + away_matches['FTAG'].sum()
    total_matches = home_matches.shape[0] +away_matches.shape[0]
    avg_goals_per_game = total_goals / total_matches
    return avg_goals_per_game


##A function to calculate the toal goals conceeded
def calculate_avg_goals_per_game_conceeded(df, team_name):
    
    home_matches = df[(df['HomeTeam'] == team_name)]
    away_matches=df[(df['AwayTeam'] == team_name)]
    total_goals = home_matches['FTAG'].sum() + away_matches['FTHG'].sum()
    total_matches = home_matches.shape[0] +away_matches.shape[0]
    avg_goals_per_game = total_goals / total_matches
    return avg_goals_per_game

 ##Over 3 goals scored in a game
def three_goal_games(df):
    high_scoring = df[(df['FTHG'] + df['FTAG']) >= 3]
    sum_high_scoring= high_scoring.shape[0]
    return sum_high_scoring

## Find number of matches played
def num_matches(df):
    return df.shape[0]

##average odds for >2.5 market
def av_high_scoring_odds(df);
    return df['AvgC>2.5'].mean()

print(three_goal_games(matches))
print(num_matches(matches))

