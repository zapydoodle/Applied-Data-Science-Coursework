import pandas as pd
import numpy as np
filename=input("filename:")
file=pd.read_csv(filename+".csv")
df=file.copy()
potentialItems=[] #What each feature could contain

print("All features can be seen below")
print(df.keys())
feature=input("What feature would you like to change?")
featureName=feature
feature=df[feature]
for item in feature:
    if(item not in potentialItems):
        potentialItems.append(item)
map={}#mapping for items to numbers
nanEncountered=False
for item in potentialItems:
    if item not in map.values():
        if pd.isna(item) and nanEncountered==False:#need clause for nan as needs to be the same across all maps
            map[np.nan]=0
            nanEncountered =True
        if pd.isna(item)==False: #if item is not nan, user asked what they want the item to map to
            print("what would you like ",item," to map to?")
            mapValue=int(input(":"))
            map[item]=mapValue
print("Feature map:")
print(map)
feature=feature.replace(map)
print(feature)#Prints new features after map is applied

df[featureName]=feature
df.to_csv(filename+"Modified.csv",index=False,encoding='utf-8')
#maps-synthetic-data-v1.1