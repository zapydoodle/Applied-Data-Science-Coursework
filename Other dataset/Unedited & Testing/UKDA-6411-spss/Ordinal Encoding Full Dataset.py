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
map={"Sex":{"Male":1,"Female":2}
}


for feature in map:
    currentFeatureMap=map[feature]
    currentFeature=df[feature]
    currentFeature=currentFeature.replace(currentFeatureMap)
    df[feature]=currentFeature


df.to_csv("MergedDatasetsEncoded.csv",index=False,encoding='utf-8',na_rep='NaN')