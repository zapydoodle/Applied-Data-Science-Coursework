import pandas as pd
from IPython.display import display


df = pd.read_spss('mcs4_cm_interview.sav')
#display(df)

print(df.shape[0])

cols=[]
for col in df.columns:
    cols.append(col)

print(cols)
