import  pandas as pd 
weight = {"day1":46,"day2":67,"day3":86}
# my= pd.Series(weight)
# print(my)
my = pd.Series(weight,index = ["day1","day2"])

print(my)


