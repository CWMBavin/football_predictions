import epl_data_v2 as data
import math
import pdb

while True:
    team1 = input('\n'
                  'Home Team: ')
    team2 = input('Away Team: ')
    try:
        # Home and Away Goals
        home_att = data.home_data(team1)[2]/data.mean_data()[0]
        home_def = data.home_data(team1)[3]/data.mean_data()[1]
        away_att = data.away_data(team2)[2]/data.mean_data()[1]
        away_def = data.away_data(team2)[3]/data.mean_data()[0]
        home_goals = data.two_decimals(home_att * away_def * data.mean_data()[0])
        away_goals = data.two_decimals(away_att * home_def * data.mean_data()[1])
        home_s = data.home_data(team1)[8]/data.mean_data()[4]
        home_s_conc = data.home_data(team1)[9]/data.mean_data()[5]
        home_sot = data.home_data(team1)[10]/data.mean_data()[6]
        home_sot_conc = data.home_data(team1)[11]/data.mean_data()[7]
        away_s = data.away_data(team2)[8]/data.mean_data()[5]
        away_s_conc = data.away_data(team2)[9]/data.mean_data()[4]
        away_sot = data.away_data(team2)[10]/data.mean_data()[7]
        away_sot_conc = data.away_data(team2)[11]/data.mean_data()[6]
        home_shots = data.two_decimals(home_s * away_s_conc * data.mean_data()[4])
        home_shots_target = data.two_decimals(home_sot * away_sot_conc * data.mean_data()[6])
        away_shots = data.two_decimals(away_s * home_s_conc * data.mean_data()[5])
        away_shots_target = data.two_decimals(away_sot * home_sot_conc * data.mean_data()[7])

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
              f"        ")

        # Home and Away Cards
        ref = input('Referee: ')
        try:
            mean_yellow = data.mean_data()[2]/2
            mean_red = data.mean_data()[3]/2
            ref_yellow = data.referees(ref)[0]/2
            ref_red = data.referees(ref)[1]/2
            home_yellow = data.home_data(team1)[4]
            home_yellow_against = data.home_data(team1)[5]
            home_red = data.home_data(team1)[6]
            home_red_against = data.home_data(team1)[7]
            away_yellow = data.away_data(team2)[4]
            away_yellow_against = data.away_data(team2)[5]
            away_red = data.away_data(team2)[6]
            away_red_against = data.away_data(team2)[7]

            home_y = home_yellow/mean_yellow
            home_r = home_red/mean_red
            home_y_a = home_yellow_against/mean_yellow
            home_r_a = home_red_against/mean_red
            away_y = away_yellow/mean_yellow
            away_r = away_red/mean_red
            away_y_a = away_yellow_against/mean_yellow
            away_r_a = away_red_against/mean_red
            ref_y = ref_yellow/mean_yellow
            ref_r = ref_red/mean_red

            home_yellow_overall = data.two_decimals(home_y * away_y_a * ref_y * mean_yellow)
            home_red_overall = data.two_decimals(home_r * away_r_a * ref_r * mean_red)
            away_yellow_overall = data.two_decimals(away_y * home_y_a * ref_y * mean_yellow)
            away_red_overall = data.two_decimals(away_r * home_r_a * ref_r * mean_red)

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
