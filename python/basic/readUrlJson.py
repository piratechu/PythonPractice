#%%
import urllib.request as req
from matplotlib.pyplot import axes
from matplotlib import rcParams
import pandas as pd
import json

#每月國際主要股價指數
#提供每月底國際主要股價指數
#download
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Microsoft JhengHei']

url = "https://apiservice.mol.gov.tw/OdService/download/A17030000J-000050-1oj"

with req.urlopen(url) as result:
    data = json.load(result)

#%%
df = pd.DataFrame(data)

df = df.set_index('月別')

df
#print(data)

# %%
#print(df)
df1 = df.astype(int).pct_change()
df1.style.format("{:.2%}")
#df.info()


# %%

df1.plot(kind='line', figsize=(14,6))

# %%
