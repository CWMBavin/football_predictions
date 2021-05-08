import urllib
import csv
import requests
import pdb
import math
import pandas as pd

ext = 'E0'
link = "https://www.football-data.co.uk/mmz4281/2021/" + ext + ".csv"
df = pd.read_csv(link)
df = df.iloc[:,:-82]



def two_decimals(i):
    """
    Returns a floating point to two decimal places
    """

    return float("{:.2f}".format(i))


def mean(i):
    """
    Outputs the mean of list, i
    """
    mean_i = sum(i) / len(i)

    return two_decimals(mean_i)


def team_names():
    teams = []
    teams.extend(df['HomeTeam'].tolist())
    teams.extend(df['AwayTeam'].tolist())
    teams = sorted(list(set(teams)))

    return teams


def referee_names():
    refs = []
    refs.extend(df['Referee'].tolist())
    refs = sorted(list(set(refs)))
    refs.insert(0, 'N/A')

    return refs


def referees(ref):
    yellow = []
    red = []
    for i in df.index:
        if df['Referee'][i] == ref:
            y = df['HY'][i] + df['AY'][i]
            yellow.append(y)
            r = df['HR'][i] + df['AR'][i]
            red.append(r)
    yellow_mean = mean(yellow)
    red_mean = mean(red)

    return yellow_mean, red_mean


def mean_data():
    home_goals = []
    away_goals = []
    yellow = []
    red = []
    home_shots = []
    away_shots = []
    home_shots_target = []
    away_shots_target = []
    home_corners = []
    away_corners = []
    for i in df.index:
        home_goals.append(int(df['FTHG'][i]))
        away_goals.append(int(df['FTAG'][i]))
        y = int(df['HY'][i]) + int(df['AY'][i])
        yellow.append(y)
        r = int(df['HR'][i]) + int(df['AR'][i])
        red.append(r)
        home_shots.append(int(df['HS'][i]))
        away_shots.append(int(df['AS'][i]))
        home_shots_target.append(int(df['HST'][i]))
        away_shots_target.append(int(df['AST'][i]))
        home_corners.append(int(df['HC'][i]))
        away_corners.append(int(df['AC'][i]))
    home_goals_mean = mean(home_goals[-120:])
    away_goals_mean = mean(away_goals[-120:])
    yellow_mean = mean(yellow)
    red_mean = mean(red)
    home_shots_mean = mean(home_shots[-120:])
    away_shots_mean = mean(away_shots[-120:])
    home_shots_target_mean = mean(home_shots_target[-120:])
    away_shots_target_mean = mean(away_shots_target[-120:])
    home_corners_mean = mean(home_corners[-120:])
    away_corners_mean = mean(away_corners[-120:])

    return [home_goals_mean,
            away_goals_mean,
            yellow_mean,
            red_mean,
            home_shots_mean,
            away_shots_mean,
            home_shots_target_mean,
            away_shots_target_mean,
            home_corners_mean,
            away_corners_mean]


def team_ranking(team):
    home_goals = []
    home_conc = []
    away_goals = []
    away_conc = []
    for i in df.index:
        if df['HomeTeam'][i] == team:
            home_goals.append(int(df['FTHG'][i]))
            home_conc.append(int(df['FTAG'][i]))
        elif df['AwayTeam'][i] == team:
            away_goals.append(int(df['FTAG'][i]))
            away_conc.append(int(df['FTHG'][i]))
        else:
            pass
    home_att = math.sqrt((mean(home_goals[-6:])))/mean_data()[0]
    home_def = math.sqrt((mean(home_conc[-6:])))/mean_data()[1]
    away_att = math.sqrt((mean(away_goals[-6:])))/mean_data()[1]
    away_def = math.sqrt((mean(away_conc[-6:])))/mean_data()[0]
    ranking = [home_att, home_def, away_att, away_def]

    return ranking


def team_data(home, away):
    """
    :param home: home team
    :param away: away team
    :return: goals, shots, yellows, corners
    """
    home_goals = []
    home_conc = []
    away_goals = []
    away_conc = []
    home_yellow = []
    home_yellow_against = []
    away_yellow = []
    away_yellow_against = []
    home_shots = []
    home_shots_conc = []
    home_shots_target = []
    home_shots_target_conc = []
    away_shots = []
    away_shots_conc = []
    away_shots_target = []
    away_shots_target_conc = []
    home_corners = []
    home_corners_conc = []
    away_corners = []
    away_corners_conc = []
    for i in df.index:
        if df['HomeTeam'][i] == home:
            home_goals.append(int(df['FTHG'][i])/(int(team_ranking(df['AwayTeam'][i])[3]))) if int(df['FTHG'][i])>0 and int(team_ranking(df['AwayTeam'][i])[3])>0 else home_goals.append(int(df['FTHG'][i]))
            home_conc.append(int(df['FTAG'][i])/(int(team_ranking(df['AwayTeam'][i])[2]))) if int(df['FTAG'][i])>0 and int(team_ranking(df['AwayTeam'][i])[2])>0 else home_conc.append(int(df['FTAG'][i]))
            home_yellow.append(int(df['HY'][i]))
            home_yellow_against.append(int(df['AY'][i]))
            home_shots.append(int(df['HS'][i]))
            home_shots_conc.append(int(df['AS'][i]))
            home_shots_target.append(int(df['HST'][i]))
            home_shots_target_conc.append(int(df['AST'][i]))
            home_corners.append(int(df['HC'][i]))
            home_corners_conc.append(int(df['AC'][i]))
        elif df['AwayTeam'][i] == home:
            home_yellow.append(int(df['AY'][i]))
            home_yellow_against.append(int(df['HY'][i]))
        if df['HomeTeam'][i] == away:
            away_yellow.append(int(df['HY'][i]))
            away_yellow_against.append(int(df['AY'][i]))
        elif df['AwayTeam'][i] == away:
            away_goals.append(int(df['FTAG'][i])/(int(team_ranking(df['HomeTeam'][i])[1]))) if int(df['FTAG'][i])>0 and int(team_ranking(df['HomeTeam'][i])[1])>0 else away_goals.append(int(df['FTAG'][i]))
            away_conc.append(int(df['FTHG'][i])/(int(team_ranking(df['HomeTeam'][i])[0]))) if int(df['FTHG'][i])>0 and int(team_ranking(df['HomeTeam'][i])[0])>0 else away_conc.append(int(df['FTHG'][i]))
            away_yellow.append(int(df['AY'][i]))
            away_yellow_against.append(int(df['HY'][i]))
            away_shots.append(int(df['AS'][i]))
            away_shots_conc.append(int(df['HS'][i]))
            away_shots_target.append(int(df['AST'][i]))
            away_shots_target_conc.append(int(df['HST'][i]))
            away_corners.append(int(df['AC'][i]))
            away_corners_conc.append(int(df['HC'][i]))

    home_goals_mean = mean(home_goals[-6:])
    home_conc_mean = mean(home_conc[-6:])
    home_yellow_mean = mean(home_yellow)
    home_yellow_against_mean = mean(home_yellow_against)
    home_shots_mean = mean(home_shots[-6:])
    home_shots_conc_mean = mean(home_shots_conc[-6:])
    home_shots_target_mean = mean(home_shots_target[-6:])
    home_shots_target_conc_mean = mean(home_shots_target_conc[-6:])
    home_corners_mean = mean(home_corners[-6:])
    home_corners_conc_mean = mean(home_corners_conc[-6:])

    away_goals_mean = mean(away_goals[-6:])
    away_conc_mean = mean(away_conc[-6:])
    away_yellow_mean = mean(away_yellow)
    away_yellow_against_mean = mean(away_yellow_against)
    away_shots_mean = mean(away_shots[-6:])
    away_shots_conc_mean = mean(away_shots_conc[-6:])
    away_shots_target_mean = mean(away_shots_target[-6:])
    away_shots_target_conc_mean = mean(away_shots_target_conc[-6:])
    away_corners_mean = mean(away_corners[-6:])
    away_corners_conc_mean = mean(away_corners_conc[-6:])

    home_att = home_goals_mean / mean_data()[0]
    home_def = home_conc_mean / mean_data()[1]
    away_att = away_goals_mean / mean_data()[1]
    away_def = away_conc_mean / mean_data()[0]

    home_g = two_decimals(home_att * away_def * mean_data()[0])
    away_g = two_decimals(away_att * home_def * mean_data()[1])

    home_s = home_shots_mean / mean_data()[4]
    home_s_conc = home_shots_conc_mean / mean_data()[5]
    home_sot = home_shots_target_mean / mean_data()[6]
    home_sot_conc = home_shots_target_conc_mean / mean_data()[7]
    away_s = away_shots_mean / mean_data()[5]
    away_s_conc = away_shots_conc_mean / mean_data()[4]
    away_sot = away_shots_target_mean / mean_data()[7]
    away_sot_conc = away_shots_target_conc_mean / mean_data()[6]

    home_xs = two_decimals(home_s * away_s_conc * mean_data()[4])
    home_xsot = two_decimals(home_sot * away_sot_conc * mean_data()[6])
    away_xs = two_decimals(away_s * home_s_conc * mean_data()[5])
    away_xsot = two_decimals(away_sot * home_sot_conc * mean_data()[7])

    home_xc = two_decimals((home_corners_mean / mean_data()[8]) *
                           (away_corners_conc_mean / mean_data()[8]) *
                           (mean_data()[8]))
    away_xc = two_decimals((away_corners_mean / mean_data()[9]) *
                           (home_corners_conc_mean / mean_data()[9]) *
                           (mean_data()[9]))

    return [home_g,
            away_g,
            home_xs,
            home_xsot,
            away_xs,
            away_xsot,
            home_yellow_mean,
            home_yellow_against_mean,
            away_yellow_mean,
            away_yellow_against_mean,
            home_xc,
            away_xc]
