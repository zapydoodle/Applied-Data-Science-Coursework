import pandas as pd
import numpy as np

df = pd.read_csv("maps-synthetic-data-v1.1.csv")

def mixing2(list_1, list_2, name):
    unique_combinations = []

    for i in range(len(list_1)):
        for j in range(len(list_2)):
            unique_combinations.append((list_1[i], list_2[j]))

    df = pd.DataFrame(unique_combinations)
    df.to_csv(name + '.csv')
    # print(unique_combinations)
    return df

def mixing3(list_1, list_2, list_3, name):
    unique_combinations = []

    for i in range(len(list_1)):
        for j in range(len(list_2)):
            for k in range(len(list_3)):
                unique_combinations.append((list_1[i], list_2[j], list_3[k]))

    df = pd.DataFrame(unique_combinations)
    df.to_csv(name + '.csv')
    # print(unique_combinations)
    return df

def mixing4(list_1, list_2, list_3, list_4, name):
    unique_combinations = []

    for i in range(len(list_1)):
        for j in range(len(list_2)):
            for k in range(len(list_3)):
                for l in range(len(list_4)):
                    unique_combinations.append((list_1[i], list_2[j], list_3[k], list_4[l]))

    df = pd.DataFrame(unique_combinations)
    df.to_csv(name+'.csv')
    # print(unique_combinations)
    return df

def mixing5(list_1, list_2, list_3, list_4, list_5, name):
    unique_combinations = []

    for i in range(len(list_1)):
        for j in range(len(list_2)):
            for k in range(len(list_3)):
                for l in range(len(list_4)):
                    for m in range (len(list_5)):
                        unique_combinations.append((list_1[i], list_2[j], list_3[k], list_4[l], list_5))

    df = pd.DataFrame(unique_combinations)
    df.to_csv(str(name))
    # print(unique_combinations)
    return df



# comp_games_bed = mixing2(df["comp_bed_9"].unique(),df["comp_games"].unique(), "comp_games_bed")
# alone = mixing2(df["alon_week"].unique(), df["alon_wend"].unique(), "alone")
# computer = mixing2(df["comp_week"].unique(), df["comp_wend"].unique(), "computer")
# draw = mixing2(df["draw_week"].unique(), df["draw_wend"].unique(), "draw")
abuse = mixing2(df["emot_cruel"].unique(), df["phys_cruel"].unique(), "abuse")
# fam_tv =  mixing3(df["fam_tv_aft"].unique(), df["fam_tv_eve"].unique(), df["fam_tv_mor"].unique(), "fam_tv")
# mother_anxiety = mixing4(df["mat_anx_0m"].unique(), df["mat_anx_1"].unique(), df["mat_anx_18m"].unique(), df["mat_anx_8m"].unique(), "mother_anxiety")
# music = mixing2(df["musi_week"].unique(), df["musi_wend"].unique(), "music")
# outside = mixing4(df["out_sum_week"].unique(), df["out_sum_wend"].unique(), df["out_win_week"].unique(), df["out_win_wend"].unique(), "outside")
# phone = mixing2(df["phone_14_week"].unique(), df["phone_14_wend"].unique(), "phone")
# play = mixing2(df["play_week"].unique(), df["play_wend"].unique(), "play")
# read = mixing2(df["read_week"].unique(), df["read_wend"].unique(), "read")
# talk_mob = mixing2(df["talk_mob_week"].unique(), df["talk_mob_wend"].unique(), "talk_mob")
# talk_phone = mixing2(df["talk_phon_week"].unique(), df["talk_phon_wend"].unique(), "talk_phone")
# text = mixing2(df["text_week"].unique(), df["text_wend"].unique(), "text")
# transport = mixing2(df["tran_week"].unique(), df["tran_wend"].unique(), "transport")
# tv = mixing2(df["tv_week"].unique(), df["tv_wend"].unique(), "tv")
# work = mixing2(df["work_week"].unique(), df["work_wend"].unique(), "work")


