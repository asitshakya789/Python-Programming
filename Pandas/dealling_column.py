import pandas as pd 
data = {'Name' : ['Asit','Amit','Akash'],
        'Qualification': ['graduate','employe','student'],
        'age': [19,28,20]
}
df= pd.DataFrame(data)
print(df[['Name','Qualification']])