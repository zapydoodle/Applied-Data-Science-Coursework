import pandas as pd

abuse = pd.read_csv("lists/abuse.csv")
alone = pd.read_csv("lists/alone.csv")
comp_games_bed = pd.read_csv("lists/comp_games_bed.csv")
computer = pd.read_csv("lists/computer.csv")
draw = pd.read_csv("lists/draw.csv")
fam_tv = pd.read_csv("lists/fam_tv.csv")
mother_anxiety = pd.read_csv("lists/mother_anxiety.csv")
music = pd.read_csv("lists/music.csv")
outside = pd.read_csv("lists/outside.csv")
phone = pd.read_csv("lists/phone.csv")
play = pd.read_csv("lists/play.csv")
read = pd.read_csv("lists/read.csv")
talk_mob = pd.read_csv("lists/talk_mob.csv")
talk_phone = pd.read_csv("lists/talk_phone.csv")
text = pd.read_csv("lists/text.csv")
transport = pd.read_csv("lists/transport.csv")
tv = pd.read_csv("lists/tv.csv")
work = pd.read_csv("lists/work.csv")

data = pd.read_csv("maps-synthetic-data-v1.1.csv")
features = pd.read_csv("Ranking features.csv")


def combine2(feature1, feature2, df):
    list = []
    for i in range(len(data)):
        variable1 = data.loc[i, feature1]
        variable2 = data.loc[i, feature2]
        newVariable = df[(df.Feature1 == str(variable1)) & (df.Feature2 == str(variable2))]
        newVariable = newVariable['Combine'].tolist()
        if not newVariable:
            list.append('Nan')
        else:
            list.extend(newVariable)
    data.drop([feature1, feature2], axis=1, inplace=True)
    data[get_df_name(df)] = list

def combine3(feature1, feature2, feature3, df):
    list = []
    for i in range(len(data)):
        variable1 = data.loc[i, feature1]
        variable2 = data.loc[i, feature2]
        variable3 = data.loc[i, feature3]
        newVariable = df[(df.Feature1 == str(variable1)) & (df.Feature2 == str(variable2)) & (df.Feature3 == str(variable3))]
        newVariable = newVariable['Combine'].tolist()
        if not newVariable:
            list.append('Nan')
        else:
            list.extend(newVariable)
    data.drop(columns=[feature1, feature2, feature3], inplace=True)
    data[get_df_name(df)] = list

def combine4(feature1, feature2, feature3, feature4, df):
    list = []
    for i in range(len(data)):
        variable1 = data.loc[i, feature1]
        variable2 = data.loc[i, feature2]
        variable3 = data.loc[i, feature3]
        variable4 = data.loc[i, feature4]
        newVariable = df[(df.Feature1 == str(variable1)) & (df.Feature2 == str(variable2)) & (df.Feature3 == str(variable3))& (df.Feature4 == str(variable4))]
        newVariable = newVariable['Combine'].tolist()
        if not newVariable:
            list.append('Nan')
        else:
            list.extend(newVariable)
    data.drop(columns=[feature1, feature2, feature3, feature4], inplace=True)
    data[get_df_name(df)] = list

def get_df_name(df):
    name =[x for x in globals() if globals()[x] is df][0]
    return name


drop_list = features.loc[features["Rank"]<=2]
drop_list = drop_list['Variable name'].tolist()
print(drop_list)
data.drop(drop_list, axis=1, inplace=True)
data.drop(['Unnamed: 0'], axis=1, inplace=True)


# combine2("comp_bed_9", "comp_games", comp_games_bed)
# combine2("alon_week", "alon_wend",alone)
# combine2("comp_week", "comp_wend", computer)
# combine2("draw_week", "draw_wend", draw)
# combine2("emot_cruel", "phys_cruel", abuse)
# combine2("musi_week", "musi_wend", music)
# combine4("out_sum_week", "out_sum_wend", "out_win_week", "out_win_wend", outside)
# combine2("phone_14_week", "phone_14_wend", phone)
# combine2("play_week", "play_wend", play)
# combine2("read_week", "read_wend", read)
# combine2("talk_mob_week", "talk_mob_wend", talk_mob)
# combine2("talk_phon_week", "talk_phon_wend", talk_phone)
# combine2("text_week", "text_wend", text)
# combine2("tv_week", "tv_wend", tv)
# combine2("work_week", "work_wend", work)
# combine3("fam_tv_aft", "fam_tv_eve", "fam_tv_mor", fam_tv)
# combine4("mat_anx_0m", "mat_anx_1", "mat_anx_18m", "mat_anx_8m", mother_anxiety)

print(data)

data.to_csv("Combined_features.csv")


