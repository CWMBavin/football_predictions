# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 17:30:51 2020

@author: CWMBavin
"""
from redundant_files import results as res
import math
from redundant_files.results import mean
from redundant_files.results import two_decimals


overall = {
    'Arsenal': [res.ars_goals_mean, res.ars_conc_mean, res.ars_xG_mean, res.ars_xG_conc_mean],
    'Aston Villa': [res.ast_goals_mean, res.ast_conc_mean, res.ast_xG_mean, res.ast_xG_conc_mean],
    'Brighton': [res.bri_goals_mean, res.bri_conc_mean, res.bri_xG_mean, res.bri_xG_conc_mean],
    'Burnley': [res.bur_goals_mean, res.bur_conc_mean, res.bur_xG_mean, res.bur_xG_conc_mean],
    'Chelsea': [res.che_goals_mean, res.che_conc_mean, res.che_xG_mean, res.che_xG_conc_mean],
    'Crystal Palace': [res.cry_goals_mean, res.cry_conc_mean, res.cry_xG_mean, res.cry_xG_conc_mean],
    'Everton': [res.eve_goals_mean, res.eve_conc_mean, res.eve_xG_mean, res.eve_xG_conc_mean],
    'Fulham': [res.ful_goals_mean, res.ful_conc_mean, res.ful_xG_mean, res.ful_xG_conc_mean],
    'Leeds': [res.lee_goals_mean, res.lee_conc_mean, res.lee_xG_mean, res.lee_xG_conc_mean],
    'Leicester': [res.lei_goals_mean, res.lei_conc_mean, res.lei_xG_mean, res.lei_xG_conc_mean],
    'Liverpool': [res.liv_goals_mean, res.liv_conc_mean, res.liv_xG_mean, res.liv_xG_conc_mean],
    'Man City': [res.mci_goals_mean, res.mci_conc_mean, res.mci_xG_mean, res.mci_xG_conc_mean],
    'Man United': [res.mun_goals_mean, res.mun_conc_mean, res.mun_xG_mean, res.mun_xG_conc_mean],
    'Newcastle': [res.new_goals_mean, res.new_conc_mean, res.new_xG_mean, res.new_xG_conc_mean],
    'Sheffield': [res.she_goals_mean, res.she_conc_mean, res.she_xG_mean, res.she_xG_conc_mean],
    'Southampton': [res.sou_goals_mean, res.sou_conc_mean, res.sou_xG_mean, res.sou_xG_conc_mean],
    'Tottenham': [res.tot_goals_mean, res.tot_conc_mean, res.tot_xG_mean, res.tot_xG_conc_mean],
    'West Brom': [res.wba_goals_mean, res.wba_conc_mean, res.wba_xG_mean, res.wba_xG_conc_mean],
    'West Ham': [res.whu_goals_mean, res.whu_conc_mean, res.whu_xG_mean, res.whu_xG_conc_mean],
    'Wolves': [res.wol_goals_mean, res.wol_conc_mean, res.wol_xG_mean, res.wol_xG_conc_mean]
    }

if __name__ == '__main__':
    for x, y in overall.items():
        print(x, '- ', y)

goal_list = []
conc_list = []
xG_list = []
xG_conc_list = []

for v in overall.values():
    goal_list.append(v[0])

for v in overall.values():
    conc_list.append(v[1])

for v in overall.values():
    xG_list.append(v[2])

for v in overall.values():
    xG_conc_list.append(v[3])

mean_goals = mean(goal_list)
mean_conc = mean(conc_list)
mean_xG = mean(xG_list)
mean_xG_conc = mean(xG_conc_list)

mean_att = ((mean_goals+mean_xG)/2)
mean_def = ((mean_conc+mean_xG_conc)/2)

# print(f'Mean xG - {[mean_goals, mean_conc, mean_xG, mean_xG_conc]}')

while True:
    team1 = input('Home Team: ')
    team2 = input('Away Team: ')
    try:
        home_att = two_decimals(((overall[team1][0]+overall[team1][2])/2)/mean_att)
        home_def = two_decimals(((overall[team1][1]+overall[team1][3])/2)/mean_def)
        away_att = two_decimals(((overall[team2][0]+overall[team2][2])/2)/mean_att)
        away_def = two_decimals(((overall[team2][1]+overall[team2][3])/2)/mean_def)
        home_goals = two_decimals(home_att * away_def * mean_att)
        away_goals = two_decimals(away_att * home_def * mean_att)

        # home_xG_att = two_decimals(overall[team1][2]/m
        # ean_xG)
        # home_xG_def = two_decimals(overall[team1][3]/mean_xG_conc)
        # away_xG_att = two_decimals(overall[team2][2]/mean_xG)
        # away_xG_def = two_decimals(overall[team2][3]/mean_xG_conc)
        # home_xG = two_decimals(home_xG_att * away_xG_def * mean_xG)
        # away_xG = two_decimals(away_xG_att * home_xG_def * mean_xG)

        e = 2.71828
        home_prob = 0
        draw_prob = 0
        away_prob = 0
        for h in range(0, 10):
            for a in range(0, 10):
                # P(x; μ) = (e^-μ) (μ^x) / x!
                if h > a:
                    h_prob = ((e**(-1*home_goals))*((home_goals**h)/(math.factorial(h)))) * \
                             ((e**(-1*away_goals))*((away_goals**a)/(math.factorial(a))))
                    home_prob += h_prob
                elif h == a:
                    d_prob = ((e**(-1*home_goals))*((home_goals**h)/(math.factorial(h)))) * \
                             ((e**(-1*away_goals))*((away_goals**a)/(math.factorial(a))))
                    draw_prob += d_prob
                else:
                    a_prob = ((e**(-1*home_goals))*((home_goals**h)/(math.factorial(h)))) * \
                             ((e**(-1*away_goals))*((away_goals**a)/(math.factorial(a))))
                    away_prob += a_prob

        home_perc_prob = two_decimals((home_prob * 100))
        draw_perc_prob = two_decimals((draw_prob * 100))
        away_perc_prob = two_decimals((away_prob * 100))

        home_odds = two_decimals((100/home_perc_prob)-1)
        draw_odds = two_decimals((100/draw_perc_prob)-1)
        away_odds = two_decimals((100/away_perc_prob)-1)

        print(f"\n"
              f"        {team1} {home_goals} - {away_goals} {team2}\n"
              f"\n"
              f"        {team1} Win: {home_perc_prob} %, {home_odds}/1\n"
              f"        Draw: {draw_perc_prob} %, {draw_odds}/1\n"
              f"        {team2} Win: {away_perc_prob} %, {away_odds}/1\n"
              f"        ")

        again = input('Another match? Y/N: ')
        if again == 'Y':
            continue
        elif again == 'N':
            break
        break
    except KeyError:
        print('Try again')
        continue
