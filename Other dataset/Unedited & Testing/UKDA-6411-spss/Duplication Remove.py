import pandas as pd
df=pd.read_csv("MergedDatasetsEncoded.csv")

IdList=[]
for Id in df["Id"]:
    if Id in IdList:
        continue
        #print("dupe")
    else:
        IdList.append(Id)


df.drop_duplicates(subset="Id",keep=False, inplace=True)
print("dropped")
IdList=[]
for Id in df["Id"]:
    if Id in IdList:
        print("dupe")
    else:
        IdList.append(Id)
print(IdList)
df.to_csv("MergedDatasetsEncodedDuplicatesRemoved.csv",index=False,encoding='utf-8',na_rep='NaN')