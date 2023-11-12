from redundant_files import epl_data_v3 as data
import math
# import tkinter as tk
# from tkinter import messagebox
# import pdb

def analysis(t):
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
    for i in data.df.index:
        if data.df['HomeTeam'][i] == t:
            home_goals.append(int(data.df['FTHG'][i])/(int(data.team_ranking(data.df['AwayTeam'][i])[3]))) if int(data.df['FTHG'][i])>0 and int(data.team_ranking(data.df['AwayTeam'][i])[3])>0 else home_goals.append(int(data.df['FTHG'][i]))
            home_conc.append(int(data.df['FTAG'][i])/(int(data.team_ranking(data.df['AwayTeam'][i])[2]))) if int(data.df['FTAG'][i])>0 and int(data.team_ranking(data.df['AwayTeam'][i])[2])>0 else home_conc.append(int(data.df['FTAG'][i]))
            home_yellow.append(int(data.df['HY'][i]))
            home_yellow_against.append(int(data.df['AY'][i]))
            home_shots.append(int(data.df['HS'][i]))
            home_shots_conc.append(int(data.df['AS'][i]))
            home_shots_target.append(int(data.df['HST'][i]))
            home_shots_target_conc.append(int(data.df['AST'][i]))
            home_corners.append(int(data.df['HC'][i]))
            home_corners_conc.append(int(data.df['AC'][i]))
        elif data.df['AwayTeam'][i] == t:
            home_yellow.append(int(data.df['AY'][i]))
            home_yellow_against.append(int(data.df['HY'][i]))
        if data.df['HomeTeam'][i] == t:
            away_yellow.append(int(data.df['HY'][i]))
            away_yellow_against.append(int(data.df['AY'][i]))
        elif data.df['AwayTeam'][i] == t:
            away_goals.append(int(data.df['FTAG'][i])/(int(data.team_ranking(data.df['HomeTeam'][i])[1]))) if int(data.df['FTAG'][i])>0 and int(data.team_ranking(data.df['HomeTeam'][i])[1])>0 else away_goals.append(int(data.df['FTAG'][i]))
            away_conc.append(int(data.df['FTHG'][i])/(int(data.team_ranking(data.df['HomeTeam'][i])[0]))) if int(data.df['FTHG'][i])>0 and int(data.team_ranking(data.df['HomeTeam'][i])[0])>0 else away_conc.append(int(data.df['FTHG'][i]))
            away_yellow.append(int(data.df['AY'][i]))
            away_yellow_against.append(int(data.df['HY'][i]))
            away_shots.append(int(data.df['AS'][i]))
            away_shots_conc.append(int(data.df['HS'][i]))
            away_shots_target.append(int(data.df['AST'][i]))
            away_shots_target_conc.append(int(data.df['HST'][i]))
            away_corners.append(int(data.df['AC'][i]))
            away_corners_conc.append(int(data.df['HC'][i]))

    home_goals_mean = data.mean(home_goals[-6:])
    home_conc_mean = data.mean(home_conc[-6:])
    home_yellow_mean = data.mean(home_yellow)
    home_yellow_against_mean = data.mean(home_yellow_against)
    home_shots_mean = data.mean(home_shots[-6:])
    home_shots_conc_mean = data.mean(home_shots_conc[-6:])
    home_shots_target_mean = data.mean(home_shots_target[-6:])
    home_shots_target_conc_mean = data.mean(home_shots_target_conc[-6:])
    home_corners_mean = data.mean(home_corners[-6:])
    home_corners_conc_mean = data.mean(home_corners_conc[-6:])

    away_goals_mean = data.mean(away_goals[-6:])
    away_conc_mean = data.mean(away_conc[-6:])
    away_yellow_mean = data.mean(away_yellow)
    away_yellow_against_mean = data.mean(away_yellow_against)
    away_shots_mean = data.mean(away_shots[-6:])
    away_shots_conc_mean = data.mean(away_shots_conc[-6:])
    away_shots_target_mean = data.mean(away_shots_target[-6:])
    away_shots_target_conc_mean = data.mean(away_shots_target_conc[-6:])
    away_corners_mean = data.mean(away_corners[-6:])
    away_corners_conc_mean = data.mean(away_corners_conc[-6:])

    home_att = home_goals_mean / data.mean_data()[0]
    home_def = home_conc_mean / data.mean_data()[1]
    away_att = away_goals_mean / data.mean_data()[1]
    away_def = away_conc_mean / data.mean_data()[0]

    home_g = data.two_decimals(home_att * away_def * data.mean_data()[0])
    away_g = data.two_decimals(away_att * home_def * data.mean_data()[1])

    home_s = home_shots_mean / data.mean_data()[4]
    home_s_conc = home_shots_conc_mean / data.mean_data()[5]
    home_sot = home_shots_target_mean / data.mean_data()[6]
    home_sot_conc = home_shots_target_conc_mean / data.mean_data()[7]
    away_s = away_shots_mean / data.mean_data()[5]
    away_s_conc = away_shots_conc_mean / data.mean_data()[4]
    away_sot = away_shots_target_mean / data.mean_data()[7]
    away_sot_conc = away_shots_target_conc_mean / data.mean_data()[6]

    home_xs = data.two_decimals(home_s * away_s_conc * data.mean_data()[4])
    home_xsot = data.two_decimals(home_sot * away_sot_conc * data.mean_data()[6])
    away_xs = data.two_decimals(away_s * home_s_conc * data.mean_data()[5])
    away_xsot = data.two_decimals(away_sot * home_sot_conc * data.mean_data()[7])

    home_xc = data.two_decimals((home_corners_mean / data.mean_data()[8]) *
                           (away_corners_conc_mean / data.mean_data()[8]) *
                           (data.mean_data()[8]))
    away_xc = data.two_decimals((away_corners_mean / data.mean_data()[9]) *
                           (home_corners_conc_mean / data.mean_data()[9]) *
                           (data.mean_data()[9]))

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


teams = data.team_names()
refs = data.referee_names()

while True:
    for team in teams:
        try:
            # Home and Away Goals
            home_goals = analysis(team)[0]
            away_goals = analysis(team)[1]
            home_shots = analysis(team)[2]
            home_shots_target = analysis(team)[3]
            away_shots = analysis(team)[4]
            away_shots_target = analysis(team)[5]
            home_corners = analysis(team)[10]
            away_corners = analysis(team)[11]

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
            try:
                home_perc_prob = data.two_decimals((home_prob * 100))
                draw_perc_prob = data.two_decimals((draw_prob * 100))
                away_perc_prob = data.two_decimals((away_prob * 100))

                home_odds = data.two_decimals((100/home_perc_prob)-1)
                draw_odds = data.two_decimals((100/draw_perc_prob)-1)
                away_odds = data.two_decimals((100/away_perc_prob)-1)
            except ZeroDivisionError:
                continue

            # print(f"\n"
            #       f"        {team} {data.two_decimals(home_goals)} - {data.two_decimals(away_goals)} {team}\n"
            #       f"\n"
            #       f"        {team} Win: {home_perc_prob} %, {home_odds}/1\n"
            #       f"        Draw: {draw_perc_prob} %, {draw_odds}/1\n"
            #       f"        {team} Win: {away_perc_prob} %, {away_odds}/1\n"
            #       f"\n"
            #       f"        {team} Shots: {home_shots}\n"
            #       f"        {team} SOTs: {home_shots_target}\n"
            #       f"        {team} Shots: {away_shots}\n"
            #       f"        {team} SOTs: {away_shots_target}\n"
            #       f"\n"
            #       f"        {team} Corners: {home_corners}\n"
            #       f"        {team} Corners: {away_corners}\n"
            #       f"        ")

            # # Home and Away Cards
            # ref = variable3.get()
            # if ref == 'N/A':
            #     pass
            # else:
            #     try:
            #         mean_yellow = data.mean_data()[2] / 2
            #         ref_yellow = data.referees(ref)[0] / 2
            #         home_yellow = analysis(team1, team2)[6]
            #         home_yellow_against = analysis(team1, team2)[7]
            #         away_yellow = analysis(team1, team2)[8]
            #         away_yellow_against = analysis(team1, team2)[9]
            #
            #         home_y = home_yellow / mean_yellow
            #         home_y_a = home_yellow_against / mean_yellow
            #         away_y = away_yellow / mean_yellow
            #         away_y_a = away_yellow_against / mean_yellow
            #         ref_y = ref_yellow / mean_yellow
            #
            #         home_yellow_overall = data.two_decimals(home_y * away_y_a * ref_y * mean_yellow)
            #         away_yellow_overall = data.two_decimals(away_y * home_y_a * ref_y * mean_yellow)
            #
            #         print(f"        {team1} Yellows: {home_yellow_overall}\n"
            #               f"        {team2} Yellows: {away_yellow_overall}\n"
            #               f"        ")
            #
            #     except ZeroDivisionError:
            #         pass
            #
            # another_match = messagebox.askquestion(title='Continue?', message='Do you want to add another match?')
            # if another_match == 'yes':
            #     continue
            # else:
            #     break

        except KeyError:
            print('Try again')
            continue

    break