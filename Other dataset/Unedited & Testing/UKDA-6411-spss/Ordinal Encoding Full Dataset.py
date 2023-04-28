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


