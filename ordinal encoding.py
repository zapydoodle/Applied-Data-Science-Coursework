import pandas as pd
import numpy as np
file=pd.read_csv("maps-synthetic-data-v1.1.csv")
df=file.copy()
potentialItems=[] #What each feature could contain
feature=df["read_wend"] #Make sure to change feature
for item in feature:
    if(item not in potentialItems):
        potentialItems.append(item)
print(potentialItems)#Prints all potential items for a feature
map={np.nan:0,"Less than 1 hour":1,"1 or more hours":2,"Not at all":3}#Creates mapping for items to numbers
feature=feature.replace(map)
print(feature)#Prints new features after map is applied