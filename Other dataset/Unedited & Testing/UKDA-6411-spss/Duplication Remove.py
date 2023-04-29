import pandas as pd
df=pd.read_csv("MergedDatasetsEncoded.csv")

#IdList=[]
#for Id in df["Id"]:
#    if Id in IdList:
#        continue
#        #print("dupe")
#    else:
#        IdList.append(Id)
#
#
#df.drop_duplicates(subset="Id",keep=False, inplace=True)
#print("dropped")
#IdList=[]
#for Id in df["Id"]:
#    if Id in IdList:
#        print("dupe")
#    else:
#        IdList.append(Id)
#print(IdList)


dupesRemoved=pd.DataFrame(columns=df.columns)
count=1
indexes=[]
for Id in df["Id"]:
    index=df.index[df["Id"]==Id].tolist()
    if index[0] not in indexes:
        indexes.append(index[0])

#print(indexes)
#print(df.loc[[indexes[1]]])
count=1
for index in indexes:
    #print(df.loc[[index]])
    entry=df.loc[[index]]
    dupesRemoved=dupesRemoved.append([entry])
    count+=1

dupesRemoved.to_csv("MergedDatasetsEncodedDuplicatesRemoved.csv",index=False,encoding='utf-8',na_rep='NaN')