import pandas as pd 
a = [1,3,5]
my = pd.Series(a,index = ["x","y","z"])
print(my)
print(my["y"])

