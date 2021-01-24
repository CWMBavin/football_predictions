import tkinter as tk
from tkinter import ttk
import epl_data_v2 as data

teams = data.team_names()
refs = data.referee_names()

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

print(variable1.get())
print(variable2.get())
print(variable3.get())
