import pandas as pd 
data = {
    "Name":['asit','amit','asits'],
    "age":[33,44,555]
}
my = pd.DataFrame(data)
print(my)
print(my.loc[0])
print(my.loc[[0,1]])