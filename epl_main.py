import epl_data_v2 as data
import math
import pdb

while True:
    team1 = input('\n'
                  'Home Team: ')
    team2 = input('Away Team: ')
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

        home_perc_prob = data.two_decimals((home_prob * 100))
        draw_perc_prob = data.two_decimals((draw_prob * 100))
        away_perc_prob = data.two_decimals((away_prob * 100))

        home_odds = data.two_decimals((100/home_perc_prob)-1)
        draw_odds = data.two_decimals((100/draw_perc_prob)-1)
        away_odds = data.two_decimals((100/away_perc_prob)-1)

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
        ref = input('Referee: ')
        try:
            mean_yellow = data.mean_data()[2]/2
            ref_yellow = data.referees(ref)[0]/2
            home_yellow = data.team_data(team1, team2)[6]
            home_yellow_against = data.team_data(team1, team2)[7]
            away_yellow = data.team_data(team1, team2)[8]
            away_yellow_against = data.team_data(team1, team2)[9]

            home_y = home_yellow/mean_yellow
            home_y_a = home_yellow_against/mean_yellow
            away_y = away_yellow/mean_yellow
            away_y_a = away_yellow_against/mean_yellow
            ref_y = ref_yellow/mean_yellow

            home_yellow_overall = data.two_decimals(home_y * away_y_a * ref_y * mean_yellow)
            away_yellow_overall = data.two_decimals(away_y * home_y_a * ref_y * mean_yellow)

            print(f"\n"
                  f"        {team1} Yellows: {home_yellow_overall}\n"
                  f"        {team2} Yellows: {away_yellow_overall}\n"
                  f"        ")

        except ZeroDivisionError:
            pass

        again = input('Another match? Y/N: ')
        if again == 'Y':
            continue
        elif again == 'N':
            break
        break

    except KeyError:
        print('Try again')
        continue