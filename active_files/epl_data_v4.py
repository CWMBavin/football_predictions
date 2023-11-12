import pandas as pd
import math
import tkinter as tk
from tkinter import messagebox
import statistics
from datetime import datetime
import os

path = "C:\\Users\\cwmba\\OneDrive\\Pictures\\Desktop"
os.makedirs(path, exist_ok=True)

#df = pd.read_csv("https://www.football-data.co.uk/mmz4281/2324/E0.csv")
#df = df.iloc[:, :-82]

class FootballStatistics:
    @staticmethod
    def two_decimals(i):
        return float("{:.2f}".format(i))

    @staticmethod
    def calculate_mean(self):
        return FootballStatistics.two_decimals(statistics.mean(self))

    @staticmethod
    def extract_last_120_data(self):
        return self[-120:]

    @staticmethod
    def calculate_stats(df):
        ext = 'E0'
        link = "https://www.football-data.co.uk/mmz4281/2223/" + ext + ".csv"
        df = pd.read_csv(link)
        df = df.iloc[:, :-82]

        teams = sorted(list(set(df['HomeTeam'].tolist() + df['AwayTeam'].tolist())))
        refs = sorted(list(set(df['Referee'].tolist())))
        refs.insert(0, 'N/A')

        home_goals = FootballStatistics.calculate_mean(df['FTHG'])
        away_goals = FootballStatistics.calculate_mean(df['FTAG'])
        yellow_mean = FootballStatistics.calculate_mean(df['HY'].tolist() + df['AY'].tolist())
        red_mean = FootballStatistics.calculate_mean(df['HR'].tolist() + df['AR'].tolist())
        home_shots_mean = FootballStatistics.calculate_mean(df['HS'].tolist())
        away_shots_mean = FootballStatistics.calculate_mean(df['AS'].tolist())
        home_shots_target_mean = FootballStatistics.calculate_mean(df['HST'].tolist())
        away_shots_target_mean = FootballStatistics.calculate_mean(df['AST'].tolist())
        home_corners_mean = FootballStatistics.calculate_mean(df['HC'].tolist())
        away_corners_mean = FootballStatistics.calculate_mean(df['AC'].tolist())

        ref_stats = {}
        for ref in refs:
            yellow = []
            red = []
            for i in df.index:
                if df['Referee'][i] == ref:
                    y = df['HY'][i] + df['AY'][i]
                    yellow.append(y)
                    r = df['HR'][i] + df['AR'][i]
                    red.append(r)
            yellow_mean = FootballStatistics.calculate_mean(yellow) if yellow else 0
            red_mean = FootballStatistics.calculate_mean(red) if red else 0
            ref_stats[ref] = {'yellow_mean': yellow_mean, 'red_mean': red_mean}

        return {
            'teams': teams,
            'refs': refs,
            'home_goals': home_goals,
            'away_goals': away_goals,
            'yellow_mean': yellow_mean,
            'red_mean': red_mean,
            'home_shots_mean': home_shots_mean,
            'away_shots_mean': away_shots_mean,
            'home_shots_target_mean': home_shots_target_mean,
            'ref_stats': ref_stats}

    @staticmethod
    def team_names():
        teams = []
        teams.extend(FootballStatistics.calculate_stats().df['HomeTeam'].tolist())
        teams.extend(FootballStatistics.calculate_stats().df['AwayTeam'].tolist())
        teams = sorted(list(set(teams)))

        return teams

    @staticmethod
    def referee_names():
        refs = []
        refs.extend(FootballStatistics.calculate_stats().df['Referee'].tolist())
        refs = sorted(list(set(refs)))
        refs.insert(0, 'N/A')

        return refs

    @staticmethod
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
            for i in FootballStatistics.calculate_stats().df.index:
                home_goals.append(int(FootballStatistics.calculate_stats().df['FTHG'][i]))
                away_goals.append(int(FootballStatistics.calculate_stats().df['FTAG'][i]))
                y = int(FootballStatistics.calculate_stats().df['HY'][i]) + int(FootballStatistics.calculate_stats().df['AY'][i])
                yellow.append(y)
                r = int(FootballStatistics.calculate_stats().df['HR'][i]) + int(FootballStatistics.calculate_stats().df['AR'][i])
                red.append(r)
                home_shots.append(int(FootballStatistics.calculate_stats().df['HS'][i]))
                away_shots.append(int(FootballStatistics.calculate_stats().df['AS'][i]))
                home_shots_target.append(int(FootballStatistics.calculate_stats().df['HST'][i]))
                away_shots_target.append(int(FootballStatistics.calculate_stats().df['AST'][i]))
                home_corners.append(int(FootballStatistics.calculate_stats().df['HC'][i]))
                away_corners.append(int(FootballStatistics.calculate_stats().df['AC'][i]))
            home_goals_mean = FootballStatistics.calculate_mean(home_goals[-120:])
            away_goals_mean = FootballStatistics.calculate_mean(away_goals[-120:])
            yellow_mean = FootballStatistics.calculate_mean(yellow)
            red_mean = FootballStatistics.calculate_mean(red)
            home_shots_mean = FootballStatistics.calculate_mean(home_shots[-120:])
            away_shots_mean = FootballStatistics.calculate_mean(away_shots[-120:])
            home_shots_target_mean = FootballStatistics.calculate_mean(home_shots_target[-120:])
            away_shots_target_mean = FootballStatistics.calculate_mean(away_shots_target[-120:])
            home_corners_mean = FootballStatistics.calculate_mean(home_corners[-120:])
            away_corners_mean = FootballStatistics.calculate_mean(away_corners[-120:])

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

    @staticmethod
    def team_ranking(team):
        home_goals = []
        home_conc = []
        away_goals = []
        away_conc = []
        for i in FootballStatistics.calculate_stats().df.index:
            if FootballStatistics.calculate_stats().df['HomeTeam'][i] == team:
                home_goals.append(int(FootballStatistics.calculate_stats().df['FTHG'][i]))
                home_conc.append(int(FootballStatistics.calculate_stats().df['FTAG'][i]))
            elif FootballStatistics.calculate_stats().df['AwayTeam'][i] == team:
                away_goals.append(int(FootballStatistics.calculate_stats().df['FTAG'][i]))
                away_conc.append(int(FootballStatistics.calculate_stats().df['FTHG'][i]))
            else:
                pass
        home_att = math.sqrt((statistics.mean(home_goals[-6:])))/FootballStatistics.mean_data()[0]
        home_def = math.sqrt((statistics.mean(home_conc[-6:])))/FootballStatistics.mean_data()[1]
        away_att = math.sqrt((statistics.mean(away_goals[-6:])))/FootballStatistics.mean_data()[1]
        away_def = math.sqrt((statistics.mean(away_conc[-6:])))/FootballStatistics.mean_data()[0]
        ranking = [home_att, home_def, away_att, away_def]

        return ranking

    @staticmethod
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
        for i in FootballStatistics.calculate_stats().df.index:
            if FootballStatistics.calculate_stats().df['HomeTeam'][i] == home:
                home_goals.append(int(FootballStatistics.calculate_stats().df['FTHG'][i]) / (int(FootballStatistics.team_ranking(FootballStatistics.calculate_stats().df['AwayTeam'][i])[3]))) if int(
                    FootballStatistics.calculate_stats().df['FTHG'][i]) > 0 and int(FootballStatistics.team_ranking(FootballStatistics.calculate_stats().df['AwayTeam'][i])[3]) > 0 else home_goals.append(
                    int(FootballStatistics.calculate_stats().df['FTHG'][i]))
                home_conc.append(int(FootballStatistics.calculate_stats().df['FTAG'][i]) / (int(FootballStatistics.team_ranking(FootballStatistics.calculate_stats().df['AwayTeam'][i])[2]))) if int(
                    FootballStatistics.calculate_stats().df['FTAG'][i]) > 0 and int(FootballStatistics.team_ranking(FootballStatistics.calculate_stats().df['AwayTeam'][i])[2]) > 0 else home_conc.append(
                    int(FootballStatistics.calculate_stats().df['FTAG'][i]))
                home_yellow.append(int(FootballStatistics.calculate_stats().df['HY'][i]))
                home_yellow_against.append(int(FootballStatistics.calculate_stats().df['AY'][i]))
                home_shots.append(int(FootballStatistics.calculate_stats().df['HS'][i]))
                home_shots_conc.append(int(FootballStatistics.calculate_stats().df['AS'][i]))
                home_shots_target.append(int(FootballStatistics.calculate_stats().df['HST'][i]))
                home_shots_target_conc.append(int(FootballStatistics.calculate_stats().df['AST'][i]))
                home_corners.append(int(FootballStatistics.calculate_stats().df['HC'][i]))
                home_corners_conc.append(int(FootballStatistics.calculate_stats().df['AC'][i]))
            elif FootballStatistics.calculate_stats().df['AwayTeam'][i] == home:
                home_yellow.append(int(FootballStatistics.calculate_stats().df['AY'][i]))
                home_yellow_against.append(int(FootballStatistics.calculate_stats().df['HY'][i]))
            if FootballStatistics.calculate_stats().df['HomeTeam'][i] == away:
                away_yellow.append(int(FootballStatistics.calculate_stats().df['HY'][i]))
                away_yellow_against.append(int(FootballStatistics.calculate_stats().df['AY'][i]))
            elif FootballStatistics.calculate_stats().df['AwayTeam'][i] == away:
                away_goals.append(int(FootballStatistics.calculate_stats().df['FTAG'][i]) / (int(FootballStatistics.team_ranking(FootballStatistics.calculate_stats().df['HomeTeam'][i])[1]))) if int(
                    FootballStatistics.calculate_stats().df['FTAG'][i]) > 0 and int(FootballStatistics.team_ranking(FootballStatistics.calculate_stats().df['HomeTeam'][i])[1]) > 0 else away_goals.append(
                    int(FootballStatistics.calculate_stats().df['FTAG'][i]))
                away_conc.append(int(FootballStatistics.calculate_stats().df['FTHG'][i]) / (int(FootballStatistics.team_ranking(FootballStatistics.calculate_stats().df['HomeTeam'][i])[0]))) if int(
                    FootballStatistics.calculate_stats().df['FTHG'][i]) > 0 and int(FootballStatistics.team_ranking(FootballStatistics.calculate_stats().df['HomeTeam'][i])[0]) > 0 else away_conc.append(
                    int(FootballStatistics.calculate_stats().df['FTHG'][i]))
                away_yellow.append(int(FootballStatistics.calculate_stats().df['AY'][i]))
                away_yellow_against.append(int(FootballStatistics.calculate_stats().df['HY'][i]))
                away_shots.append(int(FootballStatistics.calculate_stats().df['AS'][i]))
                away_shots_conc.append(int(FootballStatistics.calculate_stats().df['HS'][i]))
                away_shots_target.append(int(FootballStatistics.calculate_stats().df['AST'][i]))
                away_shots_target_conc.append(int(FootballStatistics.calculate_stats().df['HST'][i]))
                away_corners.append(int(FootballStatistics.calculate_stats().df['AC'][i]))
                away_corners_conc.append(int(FootballStatistics.calculate_stats().df['HC'][i]))

        home_goals_mean = statistics.mean(home_goals[-6:])
        home_conc_mean = statistics.mean(home_conc[-6:])
        home_yellow_mean = statistics.mean(home_yellow)
        home_yellow_against_mean = statistics.mean(home_yellow_against)
        home_shots_mean = statistics.mean(home_shots[-6:])
        home_shots_conc_mean = statistics.mean(home_shots_conc[-6:])
        home_shots_target_mean = statistics.mean(home_shots_target[-6:])
        home_shots_target_conc_mean = statistics.mean(home_shots_target_conc[-6:])
        home_corners_mean = statistics.mean(home_corners[-6:])
        home_corners_conc_mean = statistics.mean(home_corners_conc[-6:])

        away_goals_mean = statistics.mean(away_goals[-6:])
        away_conc_mean = statistics.mean(away_conc[-6:])
        away_yellow_mean = statistics.mean(away_yellow)
        away_yellow_against_mean = statistics.mean(away_yellow_against)
        away_shots_mean = statistics.mean(away_shots[-6:])
        away_shots_conc_mean = statistics.mean(away_shots_conc[-6:])
        away_shots_target_mean = statistics.mean(away_shots_target[-6:])
        away_shots_target_conc_mean = statistics.mean(away_shots_target_conc[-6:])
        away_corners_mean = statistics.mean(away_corners[-6:])
        away_corners_conc_mean = statistics.mean(away_corners_conc[-6:])

        home_att = home_goals_mean / FootballStatistics.mean_data()[0]
        home_def = home_conc_mean / FootballStatistics.mean_data()[1]
        away_att = away_goals_mean / FootballStatistics.mean_data()[1]
        away_def = away_conc_mean / FootballStatistics.mean_data()[0]

        home_g = FootballStatistics.two_decimals(home_att * away_def * FootballStatistics.mean_data()[0])
        away_g = FootballStatistics.two_decimals(away_att * home_def * FootballStatistics.mean_data()[1])

        home_s = home_shots_mean / FootballStatistics.mean_data()[4]
        home_s_conc = home_shots_conc_mean / FootballStatistics.mean_data()[5]
        home_sot = home_shots_target_mean / FootballStatistics.mean_data()[6]
        home_sot_conc = home_shots_target_conc_mean / FootballStatistics.mean_data()[7]
        away_s = away_shots_mean / FootballStatistics.mean_data()[5]
        away_s_conc = away_shots_conc_mean / FootballStatistics.mean_data()[4]
        away_sot = away_shots_target_mean / FootballStatistics.mean_data()[7]
        away_sot_conc = away_shots_target_conc_mean / FootballStatistics.mean_data()[6]

        home_xs = FootballStatistics.two_decimals(home_s * away_s_conc * FootballStatistics.mean_data()[4])
        home_xsot = FootballStatistics.two_decimals(home_sot * away_sot_conc * FootballStatistics.mean_data()[6])
        away_xs = FootballStatistics.two_decimals(away_s * home_s_conc * FootballStatistics.mean_data()[5])
        away_xsot = FootballStatistics.two_decimals(away_sot * home_sot_conc * FootballStatistics.mean_data()[7])

        home_xc = FootballStatistics.two_decimals((home_corners_mean / FootballStatistics.mean_data()[8]) *
                                                  (away_corners_conc_mean / FootballStatistics.mean_data()[8]) *
                                                  (FootballStatistics.mean_data()[8]))
        away_xc = FootballStatistics.two_decimals((away_corners_mean / FootballStatistics.mean_data()[9]) *
                                                  (home_corners_conc_mean / FootballStatistics.mean_data()[9]) *
                                                  (FootballStatistics.mean_data()[9]))

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


data = FootballStatistics.calculate_stats(df)
football_stats = FootballStatistics()

time_now = datetime.now().strftime('%d-%m-%Y_%H-%M-%S')

# teams = FootballStatistics.calculate_stats.teams()
# refs = FootballStatistics.calculate_stats.referees()

file1 = open(f"{path}\\epl_{time_now}.txt", "w")

while True:
    app = tk.Tk()
    app.title('Pick variables for football model')
    app.geometry('400x200')

    variable1 = tk.StringVar(app)
    variable1.set(data['teams'][0])
    variable2 = tk.StringVar(app)
    variable2.set(data['teams'][0])
    variable3 = tk.StringVar(app)
    variable3.set(data['refs'][0])

    home_team = tk.OptionMenu(app, variable1, *data['teams'])
    home_team.config(width=90, font=('Helvetica', 22))
    home_team.pack()

    away_team = tk.OptionMenu(app, variable2, *data['teams'])
    away_team.config(width=90, font=('Helvetica', 22))
    away_team.pack()

    referee = tk.OptionMenu(app, variable3, *data['refs'])
    referee.config(width=90, font=('Helvetica', 22))
    referee.pack()

    app.mainloop()

    team1 = variable1.get()
    team2 = variable2.get()
    try:
        # Home and Away Goals
        home_goals = football_stats.team_data(team1, team2)[0]
        away_goals = football_stats.team_data(team1, team2)[1]
        home_shots = football_stats.team_data(team1, team2)[2]
        home_shots_target = football_stats.team_data(team1, team2)[3]
        away_shots = football_stats.team_data(team1, team2)[4]
        away_shots_target = football_stats.team_data(team1, team2)[5]
        home_corners = football_stats.team_data(team1, team2)[10]
        away_corners = football_stats.team_data(team1, team2)[11]

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
            home_perc_prob = football_stats.two_decimals((home_prob * 100))
            draw_perc_prob = football_stats.two_decimals((draw_prob * 100))
            away_perc_prob = football_stats.two_decimals((away_prob * 100))

            home_odds = football_stats.two_decimals((100/home_perc_prob)-1)
            draw_odds = football_stats.two_decimals((100/draw_perc_prob)-1)
            away_odds = football_stats.two_decimals((100/away_perc_prob)-1)
        except ZeroDivisionError:
            continue

        file1.write(
              f"{team1} {football_stats.two_decimals(home_goals)} - {football_stats.two_decimals(away_goals)} {team2}\n"
              f"\n"
              f"{team1} Win: , {home_perc_prob} %, {home_odds}/1\n"
              f"Draw: {draw_perc_prob} %, {draw_odds}/1\n"
              f"{team2} Win: {away_perc_prob} %, {away_odds}/1\n"
              f"\n"
              f"{team1} Shots: {home_shots}\n"
              f"{team1} SOTs: {home_shots_target}\n"
              f"{team2} Shots: {away_shots}\n"
              f"{team2} SOTs: {away_shots_target}\n"
              f"\n"
              f"{team1} Corners: {home_corners}\n"
              f"{team2} Corners: {away_corners}\n"
              f"\n")

        print(f"\n"
              f"        {team1} {football_stats.two_decimals(home_goals)} - {football_stats.two_decimals(away_goals)} {team2}\n"
              f"\n"
              f"        {team1} Win: {home_perc_prob} %, {home_odds}/1\n"
              f"        Draw: {draw_perc_prob} %, {draw_odds}/1\n"
              f"        {team2} Win: {away_perc_prob} %, {away_odds}/1\n"
              f"\n"
              f"        {team1} Shots: {home_shots}\n"
              f"        {team1} SOTs: {home_shots_target}\n"
              f"        {team2} Shots: {away_shots}\n"
              f"        {team2} SOTs: {away_shots_target}\n"
              f"\n"
              f"        {team1} Corners: {home_corners}\n"
              f"        {team2} Corners: {away_corners}\n"
              f"        ")

        # Home and Away Cards
        ref = variable3.get()
        if ref == 'N/A':
            pass
        else:
            try:
                mean_yellow = football_stats.mean_data()[2] / 2
                ref_yellow = data['ref_stats'][0] / 2
                home_yellow = football_stats.team_data(team1, team2)[6]
                home_yellow_against = football_stats.team_data(team1, team2)[7]
                away_yellow = football_stats.team_data(team1, team2)[8]
                away_yellow_against = football_stats.team_data(team1, team2)[9]

                home_y = home_yellow / mean_yellow
                home_y_a = home_yellow_against / mean_yellow
                away_y = away_yellow / mean_yellow
                away_y_a = away_yellow_against / mean_yellow
                ref_y = ref_yellow / mean_yellow

                home_yellow_overall = football_stats.two_decimals(home_y * away_y_a * ref_y * mean_yellow)
                away_yellow_overall = football_stats.two_decimals(away_y * home_y_a * ref_y * mean_yellow)

                file1.write(f"{team1} Yellows: {home_yellow_overall}\n"
                            f"{team2} Yellows: {away_yellow_overall}\n"
                            f"\n"
                            f"\n")

                print(f"        {team1} Yellows: {home_yellow_overall}\n"
                      f"        {team2} Yellows: {away_yellow_overall}\n"
                      f"")

            except ZeroDivisionError:
                pass

        another_match = messagebox.askquestion(title='Continue?', message='Do you want to add another match?')
        if another_match == 'yes':
            continue
        else:
            break

    except KeyError:
        print('Try again')
        continue

file1.close()