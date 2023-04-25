import pandas as pd
from IPython.display import display

features="MCSID,DCMCS4AGE,DCCSEX00,DCSC0001,DCSC0002,DCSC0003,DCSC0004,DCSC0005,DCSC0006,DCSC0007,DCSC0010,DCSC0015,DCSC0019,DCSC0021,DCSC0032,DCSC0033,DCSC0034,DCSC0035,DCSC0036,DCSC0037,DCSC0038,GCHOMS00,GCHOSS00,GCCOMO00,GCSEMA00,GCPHMA00,GCCOFA00,GCSEFA00,GCPHPA00,GCDEAN00,GCDAGE00,GCTRDE00,GCTRDV00,GCSMOK00,GCAGSM00,GCVAPE00,GCALCD00,GCALAG00,GCALCN00,GCALNF00,GCALFV00,GCAGFV00,GCALFN00,GCDRUA00,GCDRUB00,GCDRUC00,GCDRUD00,GCDRUL00,GCDRUS00,GCDRUI00,GCDRUJ00,GCDRUK00,GCSPFD00,GCTVHO00,GCCOMH00,GCSOME00,GCSOCM00"
featuresList=features.split(",")
featuresRenamed="Id,Age,Sex,LikeMusic,LikeTV,LikeDrawing,LikeComputer,LikeOutSport,LikeInSport,FriendCount,LikeFriendPlay,LikeAlone,FunFamily,LikeSchool,SadSchool,TiredSchool,FedSchool,FriendTalk,Bullied,BullyOthers,ChildLeftOut,EverHomeless,CurrHomeless,MumCont,MumSee,MumSpeak,DadCont,DadSee,DadSpeak,agg_score,AgeDepDiag,DeprsTreatCurr,DeprsTreat,FirstCigAge,FirstAlchAge,FirstAlchDrinkAge,AlchDrinkYr,AlchDrinkMon,AlchDrinkExcs,AlchDrinkExcsAge,AlchDrinkExcsNum,CannabisY/N,CocaineY/N,AcidY/N,EcstasyY/N,SpeedY/N,SemeronY/N,KetamineY/N,MephedroneY/N,PsychoactiveY/N,SpeedY/N,FriendSpend,GamesSpend,SocialmedSpend,SocialmedAddict"
featuresRenamedList=featuresRenamed.split(",")
featuresMap=dict(zip(featuresList,featuresRenamedList))

df = pd.read_spss('mcs7_cm_interview - test.sav')

cols=[]
for feature in df.columns:
    cols.append(feature)
print(cols)
df.drop(df.columns.difference(featuresList),1,inplace=True)
df.rename(columns=featuresMap,inplace=True)
cols=[]
for feature in df.columns:
    cols.append(feature)
print(cols)
filename="DateAge7"
df.to_csv(filename)
