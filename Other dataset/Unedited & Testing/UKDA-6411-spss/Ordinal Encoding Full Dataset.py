import pandas as pd
import numpy as np

#df=pd.read_csv("MergedDatasets.csv",usecols=lambda c: not c.startswith('Unnamed:'))
#map=pd.DataFrame()
#count=0
#for feature in df.columns:
#    potentialItems = []
#    print(feature)
#    if feature !="Id":
#        currentFeature=df[feature]
#        for item in currentFeature:
#            if (item not in potentialItems):
#                potentialItems.append(item)
#        print(potentialItems)
#        map.insert(count,str(feature),pd.Series(potentialItems))
#        count+=1
#map.to_csv("Ordinal Encoding.csv")

df=pd.read_csv("MergedDatasets.csv",usecols=lambda c: not c.startswith('Unnamed:'))
map={"Sex":{"Male":1,"Female":2},
     "LikeMusic7":{"I like it a bit":1,"I like it a lot":2,"I don't like it":3},
     "LikeTV7":{"I like it a bit":1,"I like it a lot":2,"I don't like it":3},
     "LikeDrawing7":{"I like it a bit":1,"I like it a lot":2,"I don't like it":3},
     "LikeComputer7":{"I like it a bit":1,"I like it a lot":2,"I don't like it":3},
     "LikeOutSport7":{"I like it a bit":1,"I like it a lot":2,"I don't like it":3},
     "LikeInSport7":{"I like it a bit":1,"I like it a lot":2,"I don't like it":3},
     "FriendCount7":{"Not many":1,"Some":2,"Lots":3},
     "LikeFriendPlay7":{"I like it a bit":1,"I like it a lot":2,"I don't like it":3},
     "LikeAlone7":{"Never":1,"Some of the time":2,"All of the time":3},
     "FunFamily7":{"Never":1,"Some of the time":2,"All of the time":3},
     "LikeSchool7":{"I like it a bit":1,"I like it a lot":2,"I don't like it":3},
     "SadSchool7":{"Never":1,"Some of the time":2,"All of the time":3},
     "TiredSchool7":{"Never":1,"Some of the time":2,"All of the time":3},
     "FedSchool7":{"Never":1,"Some of the time":2,"All of the time":3},
     "FriendTalk7":{"Never":1,"Some of the time":2,"All of the time":3},
     "Bullied7":{"Never":1,"Some of the time":2,"All of the time":3},
     "BullyOthers7":{"Never":1,"Some of the time":2,"All of the time":3},
     "ChildLeftOut7":{"Never":1,"Some of the time":2,"All of the time":3},
     "EverHomeless17":{"No":1,"Yes":2},
     "CurrHomeless17":{"No":1,"Yes":2},
     "MumCont17":{"No":1,"Yes":2,"No â€“ she has died":3},
     "MumSee17":{"Once or twice a week":1,"Every day":2,"Less often but at least once a month":3,"In holiday times only":4,
                 "Less often than once a month":5,"5-6 times a week":6,"3-4 times a week":7,"Never":8},
     "MumSpeak17":{"Once or twice a week":1,"Every day":2,"Less often but at least once a month":3,"3-4 times a week":4,
                   "5-6 times a week":5,"Less often than once a month":6,"Never":7},
     "DadCont17":{"No":1,"Yes":2},
     "DadSee17":{"3-4 times a week":1,"Less often than once a month":2,"Once or twice a week":3,"5-6 times a week":4,
                 "Less often but at least once a month":5,"In holiday times only":6,"Every day":7,"Never":8},
     "DadSpeak17":{"3-4 times a week":1,"Less often but at least once a month":2,"Once or twice a week":3,"5-6 times a week":4,
                   "Every day":5,"Less often than once a month":6,"Never":7},
     "agg_score17":{"No":1,"Yes":2},
     "DeprsTreatCurr17":{"No":1,"Yes":2},
     "DeprsTreat17":{"No":1,"Yes":2},
     "FirstAlchAge17":{"No":1,"Yes":2},
     "AlchDrinkYr17":{"10-19 times":1,"6-9 times":2,"1-2 times":3,"40 or more times":4,"20-39 times":5,"3-5 times":6,
                      "Never":7},
     "AlchDrinkMon17":{"1-2 times":1,"Never":2,"40 or more times":3,"3-5 times":4,"20-39 times":5,"10-19 times":6,
                       "6-9 times":7},
     "AlchDrinkExcs17":{"No":1,"Yes":2},
     "AlchDrinkExcsNum17":{"1-2 times":1,"3-5 times":2,"10 or more times":3,"6-9 times":4,"Never":5},
     "AcidY/N17":{"No":1,"Yes":2},
     "EcstasyY/N17":{"No":1,"Yes":2},
     "SpeedY/N17":{"No":1,"Yes":2},
     "SemeronY/N17":{"No":1,"Yes":2},
     "KetamineY/N17":{"No":1,"Yes":2},
     "MephedroneY/N17":{"No":1,"Yes":2},
     "PsychoactiveY/N17":{"No":1,"Yes":2},
     "SpeedY/N17.1":{"At least once a week":1,"Most days":2,"Several times a year":3,"At least once a month":4,
                     "Once a year  or less":5,"Never or almost never":6},
     "FriendSpend17":{"1 hour to less than 2 hours":1,"5 hours to less than 7 hours":2,"2 hours to less than 3 hours":3,
                      "3 hours to less than 5 hours":4,"10 hours or more":5,"Half an hour to less than 1 hour":6,
                      "7 hours to less than 10 hours":7,"Less than half an hour":8,"None":9},
     "GamesSpend17":{"None":1,"5 hours to less than 7 hours":2,"1 hour to less than 2 hours":3,"Half an hour to less than 1 hour":4,
                     "7 hours to less than 10 hours":5,"3 hours to less than 5 hours":6,"Less than half an hour":7,
                     "10 hours or more":8,"2 hours to less than 3 hours":9},
     "SocialmedSpend17":{"Half an hour to less than 1 hour":1,"5 hours to less than 7 hours":2,"3 hours to less than 5 hours":3,
                         "2 hours to less than 3 hours":4,"10 hours or more":5,"1 hour to less than 2 hours":6,
                         "7 hours to less than 10 hours":7,"Less than half an hour":8,"None":9},
     "SocialmedAddict17":{"Disagree":1,"Agree":2,"Strongly agree":3,"Strongly disagree":4},
     "ParentsDiv7":{"Married, 1st and only marriage":1,"Divorced":2,"Remarried, 2nd or later marriage":3,
                    "Single never married":4,"Widowed":5,"Legally separated":6},
     "Parentsdiv17":{"Legally separated":1,"Married, 1st and only marriage":2,"Married, 2nd or later marriage":3,
                     "Divorced":4,"Single, never married and never in a Civil Partnership":5,"Widowed":6,
                     "Civil Partner in a legally recognised Civil Partnership":7,"Former Civil Partner (Civil Partnership legally dissolved)":8,
                     "Surviving Civil Partner (Civil Partner has died)":9},
     "FightChildTeach7":{"Not true":1,"Somewhat true":2,"Certainly true":3},
     "UpsetTeach7":{"Not true":1,"Somewhat true":2,"Certainly true":3},
     "ChildBullyTeach7":{"Not true":1,"Somewhat true":2,"Certainly true":3},
     "DepressionTeach7":{"No":1,"Yes":2}
}


for feature in map:
    currentFeatureMap=map[feature]
    currentFeature=df[feature]
    currentFeature=currentFeature.replace(currentFeatureMap)
    df[feature]=currentFeature


df.to_csv("MergedDatasetsEncoded.csv",index=False,encoding='utf-8',na_rep='NaN')