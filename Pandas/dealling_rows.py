import pandas as pd 
data = pd.read_csv("D:\Python 3.8\Pandas\nba.csv",index_col="Name")
first= data.loc["Asit kumar"]
second = data.loc["Amit kumar"]
print(first,"\n\n\n",second)