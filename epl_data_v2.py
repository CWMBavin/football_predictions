import urllib
import csv
import requests
import pdb
import math

link = "https://www.football-data.co.uk/mmz4281/2021/E0.csv"
response = urllib.request.urlopen(link)
lines = [line.decode('utf-8') for line in response.readlines()]


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


teams = {
    'Arsenal': ('Arsenal', 'ars'),
    'Aston Villa': ('Aston Villa', 'ast'),
    'Brighton': ('Brighton', 'bri'),
    'Burnley': ('Burnley', 'bur'),
    'Chelsea': ('Chelsea', 'che'),
    'Crystal Palace': ('Crystal Palace', 'cry'),
    'Everton': ('Everton', 'eve'),
    'Fulham': ('Fulham', 'ful'),
    'Leeds': ('Leeds', 'lee'),
    'Leicester': ('Leicester', 'lei'),
    'Liverpool': ('Liverpool', 'liv'),
    'Man United': ('Man United', 'mun'),
    'Man City': ('Man City', 'mci'),
    'Newcastle': ('Newcastle', 'new'),
    'Sheffield': ('Sheffield United', 'she'),
    'Southampton': ('Southampton', 'sou'),
    'Tottenham': ('Tottenham', 'tot'),
    'West Brom': ('West Brom', 'wbr'),
    'West Ham': ('West Ham', 'whu'),
    'Wolves': ('Wolves', 'wol')
}


def referees(ref):
    epl_data = csv.reader(lines)
    yellow = []
    red = []
    for row in epl_data:
        if row[11] == str(ref):
            y = int(row[20]) + int(row[21])
            yellow.append(y)
            r = int(row[22]) + int(row[23])
            red.append(r)
    yellow_mean = mean(yellow)
    red_mean = mean(red)

    return yellow_mean, red_mean


def mean_data():
    epl_data = csv.reader(lines)
    home_goals = []
    away_goals = []
    yellow = []
    red = []
    home_shots = []
    away_shots = []
    home_shots_target = []
    away_shots_target = []
    for row in epl_data:
        if row[0] == 'E0':
            home_goals.append(int(row[5]))
            away_goals.append(int(row[6]))
            y = int(row[20]) + int(row[21])
            yellow.append(y)
            r = int(row[22]) + int(row[23])
            red.append(r)
            home_shots.append(int(row[12]))
            away_shots.append(int(row[13]))
            home_shots_target.append(int(row[14]))
            away_shots_target.append(int(row[15]))
    home_goals_mean = mean(home_goals[-120:])
    away_goals_mean = mean(away_goals[-120:])
    yellow_mean = mean(yellow)
    red_mean = mean(red)
    home_shots_mean = mean(home_shots[-120:])
    away_shots_mean = mean(away_shots[-120:])
    home_shots_target_mean = mean(home_shots_target[-120:])
    away_shots_target_mean = mean(away_shots_target[-120:])
    return home_goals_mean, \
           away_goals_mean, \
           yellow_mean, \
           red_mean, \
           home_shots_mean, \
           away_shots_mean, \
           home_shots_target_mean, \
           away_shots_target_mean


def team_ranking():
    ranking = {}
    for team in teams.values():
        epl_data = csv.reader(lines)
        home_goals = []
        home_conc = []
        away_goals = []
        away_conc = []
        for row in epl_data:
            if row[0] == 'E0':
                if row[3] == team[0]:
                    home_goals.append(int(row[5]))
                    home_conc.append(int(row[6]))
                elif row[4] == team[0]:
                    away_goals.append(int(row[6]))
                    away_conc.append(int(row[5]))
                else:
                    pass
            else:
                pass

        home_att = math.sqrt((mean(home_goals[-6:])))/mean_data()[0]
        home_def = math.sqrt((mean(home_conc[-6:])))/mean_data()[1]
        away_att = math.sqrt((mean(away_goals[-6:])))/mean_data()[1]
        away_def = math.sqrt((mean(away_conc[-6:])))/mean_data()[0]
        ranking[team[0]] = (home_att, home_def, away_att, away_def)
    return ranking
 

def home_data(team):
    """

    :param team:
    :return:
    """
    epl_data = csv.reader(lines)
    goals = []
    conc = []
    home_goals = []
    home_conc = []
    yellow = []
    yellow_against = []
    red = []
    red_against = []
    home_shots = []
    home_shots_conc = []
    home_shots_target = []
    home_shots_target_conc = []
    for row in epl_data:
        if row[0] == 'E0':
            if row[3] == teams[team][0]:
                goals.append(int(row[5]))
                conc.append(int(row[6]))
                home_goals.append(int(row[5])/(team_ranking()[row[4]][3]))
                home_conc.append(int(row[6])/(team_ranking()[row[4]][2]))
                yellow.append(int(row[20]))
                yellow_against.append(int(row[21]))
                red.append(int(row[22]))
                red_against.append(int(row[23]))
                home_shots.append(int(row[12]))
                home_shots_conc.append(int(row[13]))
                home_shots_target.append(int(row[14]))
                home_shots_target_conc.append(int(row[15]))
            elif row[4] == teams[team][0]:
                goals.append(int(row[6]))
                conc.append(int(row[5]))
                yellow.append(int(row[21]))
                yellow_against.append(int(row[20]))
                red.append(int(row[23]))
                red_against.append(int(row[22]))

    goals_mean = mean(goals[-6:])
    conc_mean = mean(conc[-6:])
    home_goals_mean = mean(home_goals[-6:])
    home_conc_mean = mean(home_conc[-6:])
    yellow_mean = mean(yellow)
    yellow_against_mean = mean(yellow_against)
    red_mean = mean(red)
    red_against_mean = mean(red_against)
    home_shots_mean = mean(home_shots[-6:])
    home_shots_conc_mean = mean(home_shots_conc[-6:])
    home_shots_target_mean = mean(home_shots_target[-6:])
    home_shots_target_conc_mean = mean(home_shots_target_conc[-6:])

    return goals_mean, \
           conc_mean, \
           home_goals_mean, \
           home_conc_mean, \
           yellow_mean, \
           yellow_against_mean, \
           red_mean, \
           red_against_mean, \
           home_shots_mean, \
           home_shots_conc_mean, \
           home_shots_target_mean, \
           home_shots_target_conc_mean


def away_data(team):
    epl_data = csv.reader(lines)
    goals = []
    conc = []
    away_goals = []
    away_conc = []
    yellow = []
    yellow_against = []
    red = []
    red_against = []
    away_shots = []
    away_shots_conc = []
    away_shots_target = []
    away_shots_target_conc = []
    for row in epl_data:
        if row[0] == 'E0':
            if row[3] == teams[team][0]:
                goals.append(int(row[5]))
                conc.append(int(row[6]))
                yellow.append(int(row[20]))
                yellow_against.append(int(row[21]))
                red.append(int(row[22]))
                red_against.append(int(row[23]))
            elif row[4] == teams[team][0]:
                goals.append(int(row[6]))
                conc.append(int(row[5]))
                away_goals.append(int(row[6])/(team_ranking()[row[4]][1]))
                away_conc.append(int(row[5])/(team_ranking()[row[4]][0]))
                yellow.append(int(row[21]))
                yellow_against.append(int(row[20]))
                red.append(int(row[23]))
                red_against.append(int(row[22]))
                away_shots.append(int(row[13]))
                away_shots_conc.append(int(row[12]))
                away_shots_target.append(int(row[15]))
                away_shots_target_conc.append(int(row[14]))

    goals_mean = mean(goals[-6:])
    conc_mean = mean(conc[-6:])
    away_goals_mean = mean(away_goals[-6:])
    away_conc_mean = mean(away_conc[-6:])
    yellow_mean = mean(yellow)
    yellow_against_mean = mean(yellow_against)
    red_mean = mean(red)
    red_against_mean = mean(red_against)
    away_shots_mean = mean(away_shots[-6:])
    away_shots_conc_mean = mean(away_shots_conc[-6:])
    away_shots_target_mean = mean(away_shots_target[-6:])
    away_shots_target_conc_mean = mean(away_shots_target_conc[-6:])

    return goals_mean, \
           conc_mean, \
           away_goals_mean, \
           away_conc_mean, \
           yellow_mean, \
           yellow_against_mean, \
           red_mean, \
           red_against_mean, \
           away_shots_mean, \
           away_shots_conc_mean, \
           away_shots_target_mean, \
           away_shots_target_conc_mean
