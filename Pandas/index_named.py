import pandas as pd 
data ={
    'Name':["Asit ","Amit","Akash"],
    "Age": [33,44,22]
}
pf =pd.DataFrame(data,index=["day1","day2","day3"])
print(pf)
print(pf.loc["day2"])
