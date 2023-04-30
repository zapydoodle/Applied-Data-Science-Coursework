import pandas as pd
from IPython.display import display

features="MCSID,DCMCS4AGE,DCCSEX00,DCSC0001,DCSC0002,DCSC0003,DCSC0004,DCSC0005,DCSC0006,DCSC0007,DCSC0010,DCSC0015,DCSC0019,DCSC0021,DCSC0032,DCSC0033,DCSC0034,DCSC0035,DCSC0036,DCSC0037,DCSC0038,GCHOMS00,GCHOSS00,GCCOMO00,GCSEMA00,GCPHMA00,GCCOFA00,GCSEFA00,GCPHPA00,GCDEAN00,GCDAGE00,GCTRDE00,GCTRDV00,GCAGSM00,GCALCD00,GCALAG00,GCALCN00,GCALNF00,GCALFV00,GCAGFV00,GCALFN00,GCDRUA00,GCDRUB00,GCDRUC00,GCDRUD00,GCDRUL00,GCDRUS00,GCDRUI00,GCDRUJ00,GCDRUK00,GCSPFD00,GCTVHO00,GCCOMH00,GCSOME00,GCSOCM00,DQ2182,DQ2183,DQ2189,DQ2340,DPFCIN00,GPFCIN00"
featuresList=features.split(",")
featuresRenamed="Id,Age,Sex,LikeMusic7,LikeTV7,LikeDrawing7,LikeComputer7,LikeOutSport7,LikeInSport7,FriendCount7,LikeFriendPlay7,LikeAlone7,FunFamily7,LikeSchool7,SadSchool7,TiredSchool7,FedSchool7,FriendTalk7,Bullied7,BullyOthers7,ChildLeftOut7,EverHomeless17,CurrHomeless17,MumCont17,MumSee17,MumSpeak17,DadCont17,DadSee17,DadSpeak17,agg_score17,AgeDepDiag17,DeprsTreatCurr17,DeprsTreat17,FirstCigAge17,FirstAlchAge17,FirstAlchDrinkAge17,AlchDrinkYr17,AlchDrinkMon17,AlchDrinkExcs17,AlchDrinkExcsAge17,AlchDrinkExcsNum17,CannabisY/N17,CocaineY/N17,AcidY/N17,EcstasyY/N17,SpeedY/N17,SemeronY/N17,KetamineY/N17,MephedroneY/N17,PsychoactiveY/N17,SpeedY/N17,FriendSpend17,GamesSpend17,SocialmedSpend17,SocialmedAddict17,FightChildTeach7,UpsetTeach7,ChildBullyTeach7,DepressionTeach7,ParentsDiv7,Parentsdiv17"
featuresRenamedList=featuresRenamed.split(",")
featuresMap=dict(zip(featuresList,featuresRenamedList))

age7child = pd.read_spss('mcs4_cm_interview - test.sav')
age17child =pd.read_spss('mcs7_cm_interview - test.sav')
age7teach=pd.read_spss('mcs4_cm_teacher_survey.sav')
age7parent=pd.read_spss('mcs4_parent_interview.sav')
age17parent=pd.read_spss('mcs7_parent_interview.sav')

age7child.drop(age7child.columns.difference(featuresList),1,inplace=True)
age7child.rename(columns=featuresMap,inplace=True)


age17child.drop(age17child.columns.difference(featuresList),1,inplace=True)
age17child.rename(columns=featuresMap,inplace=True)


age7teach.drop(age7teach.columns.difference(featuresList),1,inplace=True)
age7teach.rename(columns=featuresMap,inplace=True)


age7parent.drop(age7parent.columns.difference(featuresList),1,inplace=True)
age7parent.rename(columns=featuresMap,inplace=True)


age17parent.drop(age17parent.columns.difference(featuresList),1,inplace=True)
age17parent.rename(columns=featuresMap,inplace=True)


df1=pd.merge(age7child,age17child,on="Id")
df1.drop(columns=['CannabisY/N17', 'CocaineY/N17'],inplace=True)

df2=pd.merge(age7parent,age17parent,on="Id")

df3=pd.merge(df1,df2,on="Id")

df=pd.merge(df3,age7teach,on="Id")


cols=[]
for feature in df.columns:
    cols.append(feature)
print(cols)
filename="MergedDatasets.csv"
#df.drop_duplicates(subset="Id",keep=False, inplace=True)
df.to_csv(filename)
