import pandas as pd
from IPython.display import display


df = pd.read_spss('mcs4_proxy_partner_interview.sav')
display(df)

cols=[]
for col in df.columns:
    cols.append(col)

print(cols)
