import pandas as pa
# list = ['asit kumar','amit kumar','akash kumar','nikhil kumar']
# df = pa.DataFrame(list)
# print(df)



mtdataset = {
    'cars' :["bmw","volvo","ford"],
    'passing':[3,4,6]
    
}
mycar = pa.DataFrame(mtdataset)
print(mycar)