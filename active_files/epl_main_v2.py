import epl_data_v4 as data
import math
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import time
import pdb

data = calculate_stats()
teams = data['teams']
refs = data['refs']

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

    app.lift()
    app.attributes('-topmost', True)
    app.after_idle(app.attributes, '-topmost', False)
    app.mainloop()

    team1 = variable1.get()
    team2 = variable2.get()

    home_goals = data['home_goals_mean']
    away_goals = data['away_goals_mean']
    home_shots = data['home_shots_mean']
    home_shots_target = data['home_shots_target_mean']
    away_shots = data['away_shots_mean']