from active_files import epl_data_v3 as data
import math
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import time
import pdb

time_now = datetime.now().strftime('%d-%m-%Y_%H-%M-%S')

teams = data.team_names()
refs = data.referee_names()

file1 = open(f"C:\\Users\\cwmba\\OneDrive\\Pictures\\Desktop\\epl_" + time_now + ".txt", "w")

while True:
    app = tk.Tk()
    app.title('Pick variables for football model')
    app.geometry('400x200')

    variable1 = tk.StringVar(app)
    variable1.set(teams[0])
    variable2 = tk.StringVar(app)
    variable2.set(teams[0])
    variable3 = tk.StringVar(app)
    variable3.set(refs[0])

    home_team = tk.OptionMenu(app, variable1, *teams)
    home_team.config(width=90, font=('Helvetica', 22))
    home_team.pack()

    away_team = tk.OptionMenu(app, variable2, *teams)
    away_team.config(width=90, font=('Helvetica', 22))
    away_team.pack()

    referee = tk.OptionMenu(app, variable3, *refs)
    referee.config(width=90, font=('Helvetica', 22))
    referee.pack()

    app.mainloop()

    team1 = variable1.get()
    team2 = variable2.get()
    try:
        # Home and Away Goals
        home_goals = data.team_data(team1, team2)[0]
        away_goals = data.team_data(team1, team2)[1]
        home_shots = data.team_data(team1, team2)[2]
        home_shots_target = data.team_data(team1, team2)[3]
        away_shots = data.team_data(team1, team2)[4]
        away_shots_target = data.team_data(team1, team2)[5]
        home_corners = data.team_data(team1, team2)[10]
        away_corners = data.team_data(team1, team2)[11]

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

        file1.write(
              f"{team1} {data.two_decimals(home_goals)} - {data.two_decimals(away_goals)} {team2}\n"
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
              f"        {team1} {data.two_decimals(home_goals)} - {data.two_decimals(away_goals)} {team2}\n"
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
                mean_yellow = data.mean_data()[2] / 2
                ref_yellow = data.referees(ref)[0] / 2
                home_yellow = data.team_data(team1, team2)[6]
                home_yellow_against = data.team_data(team1, team2)[7]
                away_yellow = data.team_data(team1, team2)[8]
                away_yellow_against = data.team_data(team1, team2)[9]

                home_y = home_yellow / mean_yellow
                home_y_a = home_yellow_against / mean_yellow
                away_y = away_yellow / mean_yellow
                away_y_a = away_yellow_against / mean_yellow
                ref_y = ref_yellow / mean_yellow

                home_yellow_overall = data.two_decimals(home_y * away_y_a * ref_y * mean_yellow)
                away_yellow_overall = data.two_decimals(away_y * home_y_a * ref_y * mean_yellow)

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