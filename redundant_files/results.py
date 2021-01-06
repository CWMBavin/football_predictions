# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 14:47:54 2020

@author: CWMBavin

The goals and goals conceded lists are no longer used so will no longer be updated (21/12/20)
"""

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

# last updated 18/12/20


ars_goals = [3, 2, 1, 2, 0, 0, 1, 0, 0, 1, 0, 0, 1, ]
ast_goals = [1, 3, 7, 1, 0, 3, 3, 1, 1, 1, 0, ]
bri_goals = [1, 3, 2, 2, 1, 1, 1, 0, 2, 1, 1, 0, 0, ]
bur_goals = [2, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, ]
che_goals = [3, 0, 3, 4, 3, 0, 3, 4, 2, 0, 3, 0, 1, ]
cry_goals = [1, 3, 1, 0, 1, 2, 0, 4, 0, 0, 5, 1, 1, ]
eve_goals = [1, 5, 2, 4, 2, 0, 1, 1, 3, 0, 1, 1, 2, ]
ful_goals = [0, 3, 0, 0, 1, 1, 2, 0, 2, 2, 0, 1, 0, ]
lee_goals = [3, 4, 1, 1, 0, 3, 1, 1, 0, 1, 1, 1, 5, ]
lei_goals = [3, 4, 5, 0, 0, 1, 4, 1, 0, 1, 2, 3, 0, ]
liv_goals = [4, 2, 3, 2, 2, 2, 2, 1, 3, 1, 4, 1, 2, ]
mci_goals = [3, 2, 1, 1, 1, 1, 1, 0, 5, 2, 0, 1, ]
mun_goals = [1, 3, 1, 4, 0, 0, 3, 1, 3, 3, 0, 3, ]
new_goals = [2, 0, 1, 3, 1, 1, 2, 0, 0, 2, 2, 2, ]
she_goals = [0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 2, ]
sou_goals = [0, 2, 1, 2, 3, 2, 4, 2, 1, 2, 2, 3, ]
tot_goals = [0, 5, 1, 6, 3, 1, 2, 1, 2, 0, 2, 1, 1, ]
wba_goals = [0, 2, 3, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, ]
whu_goals = [0, 1, 4, 3, 3, 1, 1, 1, 1, 2, 1, 2, 1, ]
wol_goals = [2, 1, 0, 1, 1, 1, 2, 0, 1, 2, 0, 0, 2, ]

ars_conc = [0, 1, 3, 1, 1, 1, 0, 3, 0, 2, 2, 1, 1, ]
ast_conc = [0, 0, 2, 0, 3, 4, 0, 2, 2, 0, 0, ]
bri_conc = [3, 0, 3, 4, 1, 1, 2, 0, 1, 1, 2, 3, 0, ]
bur_conc = [4, 1, 3, 0, 1, 3, 0, 0, 5, 1, 0, 0, ]
che_conc = [1, 2, 3, 0, 3, 0, 0, 1, 0, 0, 1, 1, 2, ]
cry_conc = [0, 1, 2, 4, 1, 1, 2, 1, 1, 2, 1, 1, 1, ]
eve_conc = [0, 2, 1, 2, 2, 2, 2, 3, 2, 1, 1, 0, 0, ]
ful_conc = [3, 4, 3, 1, 1, 2, 0, 1, 3, 1, 2, 1, 0, ]
lee_conc = [4, 3, 0, 1, 1, 0, 4, 4, 0, 0, 3, 2, 2, ]
lei_conc = [0, 2, 2, 3, 1, 0, 1, 0, 3, 2, 1, 0, 2, ]
liv_conc = [3, 0, 1, 7, 2, 1, 1, 1, 0, 1, 0, 1, 1, ]
mci_conc = [1, 5, 1, 0, 1, 0, 1, 2, 0, 0, 0, 1, ]
mun_conc = [3, 2, 6, 1, 0, 1, 1, 0, 2, 1, 0, 2, ]
new_conc = [0, 3, 1, 1, 4, 1, 1, 2, 2, 0, 1, 5, ]
she_conc = [2, 1, 1, 2, 1, 2, 1, 4, 1, 1, 2, 3, 3, ]
sou_conc = [1, 5, 0, 0, 3, 0, 3, 0, 1, 3, 1, 0, 1, ]
tot_conc = [1, 2, 1, 1, 3, 0, 1, 0, 0, 0, 0, 1, 2, ]
wba_conc = [3, 5, 3, 2, 0, 1, 2, 1, 1, 0, 5, 2, 1, ]
whu_conc = [2, 2, 0, 0, 3, 1, 2, 0, 0, 1, 3, 1, 1, ]
wol_conc = [0, 3, 4, 0, 0, 1, 0, 1, 1, 1, 4, 1, 1, ]

ars_xG = [2.16, 1.33, 1.18, 0.67, 0.84, 0.74, 1.00, 1.39, 0.71, 1.12, 0.60, 1.85, 0.66, ]
ast_xG = [0.81, 2.03, 3.08, 0.87, 1.50, 2.45, 1.99, 1.77, 2.39, 1.27, 1.81, ]
bri_xG = [1.44, 1.88, 2.98, 1.17, 1.09, 0.55, 0.32, 1.59, 1.50, 2.31, 2.03, 0.79, 0.46, ]
bur_xG = [1.52, 0.35, 0.44, 1.09, 0.95, 0.41, 0.33, 1.75, 0.42, 0.73, 0.82, 0.32, ]
che_xG = [1.27, 0.90, 2.36, 2.51, 1.99, 0.22, 1.23, 2.88, 1.82, 0.97, 4.89, 1.01, 1.57, ]
cry_xG = [1.40, 1.91, 0.44, 0.10, 0.76, 2.81, 0.80, 1.30, 1.28, 0.53, 1.69, 1.84, 1.09, ]
eve_xG = [1.27, 4.16, 2.27, 2.34, 1.36, 0.29, 1.22, 0.38, 2.25, 1.29, 2.28, 1.22, 1.51, ]
ful_xG = [0.13, 1.56, 0.53, 0.97, 1.36, 1.05, 1.62, 1.85, 1.87, 2.04, 0.29, 1.73, 1.00, ]
lee_xG = [0.27, 1.45, 1.47, 2.57, 1.08, 2.38, 1.75, 0.85, 1.96, 3.11, 1.03, 1.57, 2.95, ]
lei_xG = [2.96, 0.99, 2.87, 0.46, 0.67, 0.74, 3.08, 2.05, 1.98, 1.28, 1.39, 1.64, 0.84, ]
liv_xG = [3.15, 2.25, 2.74, 1.66, 2.49, 2.40, 1.56, 1.19, 3.77, 0.28, 1.59, 1.82, 1.22, ]
mci_xG = [2.08, 1.45, 1.42, 1.43, 0.89, 1.90, 1.58, 1.66, 2.26, 3.26, 1.28, 2.59, ]
mun_xG = [1.10, 1.58, 0.87, 2.22, 0.65, 0.39, 1.60, 2.43, 2.48, 1.79, 0.59, 1.79, ]
new_xG = [1.66, 0.52, 0.94, 1.96, 0.87, 0.25, 2.63, 0.18, 0.37, 1.28, 0.90, 1.44, ]
she_xG = [0.95, 0.85, 1.53, 0.14, 1.66, 1.40, 0.69, 0.74, 0.69, 3.37, 0.29, 0.22, 1.24, ]
sou_xG = [1.26, 2.28, 0.71, 0.95, 1.42, 0.74, 1.00, 0.99, 1.08, 0.50, 1.35, 2.28, 1.11, ]
tot_xG = [0.82, 2.28, 3.19, 3.30, 1.78, 0.80, 1.97, 1.87, 0.76, 0.23, 0.39, 1.41, 1.52, ]
wba_xG = [0.35, 0.32, 0.91, 0.16, 0.73, 0.30, 0.48, 0.80, 0.44, 1.72, 0.57, 0.57, 0.21, ]
whu_xG = [0.86, 2.06, 3.06, 2.03, 1.50, 0.26, 0.27, 1.43, 2.11, 0.57, 2.53, 1.79, 0.45, ]
wol_xG = [1.61, 0.73, 0.39, 0.89, 0.62, 0.76, 1.35, 0.58, 1.57, 2.01, 0.36, 1.14, 0.68, ]

ars_xG_conc = [0.13, 2.06, 2.74, 0.14, 1.43, 0.74, 0.39, 1.99, 1.96, 2.01, 0.27, 0.39, 0.82, 1.11, ]
ast_xG_conc = [0.85, 0.53, 1.66, 0.67, 2.38, 1.00, 1.39, 1.50, 0.57, 1.14, 0.32, ]
bri_xG_conc = [1.27, 0.52, 1.58, 2.34, 0.76, 0.30, 1.97, 0.33, 1.77, 0.28, 1.35, 1.64, 1.00, ]
bur_xG_conc = [0.99, 0.71, 1.96, 0.73, 0.80, 1.23, 1.59, 1.28, 2.26, 2.28, 1.85, 1.81, ]
che_xG_conc = [1.44, 2.25, 0.91, 0.10, 1.42, 0.65, 0.41, 0.74, 0.37, 0.23, 1.03, 1.22, 0.68, ]
cry_xG_conc = [1.23, 1.10, 2.27, 2.51, 1.09, 1.05, 1.35, 0.85, 1.75, 1.25, 0.57, 1.41, 0.45, ]
eve_xG_conc = [0.82, 0.32, 0.44, 1.17, 2.49, 0.74, 2.63, 1.60, 1.87, 3.11, 0.73, 1.01, 0.84, ]
ful_xG_conc = [2.16, 1.45, 2.03, 0.89, 1.66, 2.81, 0.48, 1.43, 2.25, 1.28, 3.26, 1.82, 0.46, ]
lee_xG_conc = [3.15, 1.56, 1.53, 1.42, 0.62, 1.50, 3.08, 1.30, 0.71, 1.29, 4.89, 1.79, 1.44, ]
lei_xG_conc = [0.35, 1.52, 1.45, 2.03, 0.87, 0.74, 1.75, 0.58, 3.77, 2.04, 0.29, 0.79, 1.51, ]
liv_xG_conc = [0.27, 0.90, 1.18, 3.08, 1.36, 1.40, 0.27, 1.58, 1.98, 2.31, 0.36, 1.73, 1.52, ]
mci_xG_conc = [0.73, 2.87, 2.57, 0.84, 0.26, 0.69, 1.19, 0.76, 0.42, 0.29, 0.59, 0.21, ]
mun_xG_conc = [1.91, 2.98, 3.30, 0.87, 0.22, 1.00, 0.38, 0.44, 0.50, 2.53, 1.28, 1.24, ]
new_xG_conc = [0.86, 1.88, 3.19, 0.44, 2.22, 0.76, 1.22, 0.99, 1.82, 0.53, 0.57, 2.95, ]
she_xG_conc = [1.61, 0.81, 1.47, 0.67, 1.36, 2.40, 1.90, 2.88, 2.11, 1.72, 1.39, 2.28, 1.79, ]
sou_xG_conc = [1.40, 2.28, 0.35, 0.16, 1.99, 0.29, 2.45, 0.18, 1.57, 2.48, 2.03, 0.22, 0.66, ]
tot_xG_conc = [1.27, 2.28, 0.94, 0.87, 1.50, 0.95, 0.32, 0.80, 1.66, 0.97, 0.60, 1.84, 1.22, ]
wba_xG_conc = [2.96, 4.16, 2.36, 0.95, 1.09, 0.55, 1.62, 1.87, 2.43, 3.37, 1.69, 0.90, 2.59, ]
whu_xG_conc = [1.66, 1.33, 0.39, 0.46, 1.78, 0.89, 1.56, 1.85, 0.69, 2.39, 1.79, 1.57, 1.09, ]
wol_xG_conc = [0.95, 2.08, 3.06, 0.97, 1.08, 0.25, 0.80, 2.05, 1.08, 1.12, 1.59, 1.27, 1.57, ]

ars_goals_mean = mean(ars_goals)
ast_goals_mean = mean(ast_goals)
bri_goals_mean = mean(bri_goals)
bur_goals_mean = mean(bur_goals)
che_goals_mean = mean(che_goals)
cry_goals_mean = mean(cry_goals)
eve_goals_mean = mean(eve_goals)
ful_goals_mean = mean(ful_goals)
lee_goals_mean = mean(lee_goals)
lei_goals_mean = mean(lei_goals)
liv_goals_mean = mean(liv_goals)
mci_goals_mean = mean(mci_goals)
mun_goals_mean = mean(mun_goals)
new_goals_mean = mean(new_goals)
she_goals_mean = mean(she_goals)
sou_goals_mean = mean(sou_goals)
tot_goals_mean = mean(tot_goals)
wba_goals_mean = mean(wba_goals)
whu_goals_mean = mean(whu_goals)
wol_goals_mean = mean(wol_goals)

ars_conc_mean = mean(ars_conc)
ast_conc_mean = mean(ast_conc)
bri_conc_mean = mean(bri_conc)
bur_conc_mean = mean(bur_conc)
che_conc_mean = mean(che_conc)
cry_conc_mean = mean(cry_conc)
eve_conc_mean = mean(eve_conc)
ful_conc_mean = mean(ful_conc)
lee_conc_mean = mean(lee_conc)
lei_conc_mean = mean(lei_conc)
liv_conc_mean = mean(liv_conc)
mci_conc_mean = mean(mci_conc)
mun_conc_mean = mean(mun_conc)
new_conc_mean = mean(new_conc)
she_conc_mean = mean(she_conc)
sou_conc_mean = mean(sou_conc)
tot_conc_mean = mean(tot_conc)
wba_conc_mean = mean(wba_conc)
whu_conc_mean = mean(whu_conc)
wol_conc_mean = mean(wol_conc)

ars_xG_mean = mean(ars_xG)
ast_xG_mean = mean(ast_xG)
bri_xG_mean = mean(bri_xG)
bur_xG_mean = mean(bur_xG)
che_xG_mean = mean(che_xG)
cry_xG_mean = mean(cry_xG)
eve_xG_mean = mean(eve_xG)
ful_xG_mean = mean(ful_xG)
lee_xG_mean = mean(lee_xG)
lei_xG_mean = mean(lei_xG)
liv_xG_mean = mean(liv_xG)
mci_xG_mean = mean(mci_xG)
mun_xG_mean = mean(mun_xG)
new_xG_mean = mean(new_xG)
she_xG_mean = mean(she_xG)
sou_xG_mean = mean(sou_xG)
tot_xG_mean = mean(tot_xG)
wba_xG_mean = mean(wba_xG)
whu_xG_mean = mean(whu_xG)
wol_xG_mean = mean(wol_xG)

ars_xG_conc_mean = mean(ars_xG_conc)
ast_xG_conc_mean = mean(ast_xG_conc)
bri_xG_conc_mean = mean(bri_xG_conc)
bur_xG_conc_mean = mean(bur_xG_conc)
che_xG_conc_mean = mean(che_xG_conc)
cry_xG_conc_mean = mean(cry_xG_conc)
eve_xG_conc_mean = mean(eve_xG_conc)
ful_xG_conc_mean = mean(ful_xG_conc)
lee_xG_conc_mean = mean(lee_xG_conc)
lei_xG_conc_mean = mean(lei_xG_conc)
liv_xG_conc_mean = mean(liv_xG_conc)
mci_xG_conc_mean = mean(mci_xG_conc)
mun_xG_conc_mean = mean(mun_xG_conc)
new_xG_conc_mean = mean(new_xG_conc)
she_xG_conc_mean = mean(she_xG_conc)
sou_xG_conc_mean = mean(sou_xG_conc)
tot_xG_conc_mean = mean(tot_xG_conc)
wba_xG_conc_mean = mean(wba_xG_conc)
whu_xG_conc_mean = mean(whu_xG_conc)
wol_xG_conc_mean = mean(wol_xG_conc)