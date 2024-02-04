
# Variable are contain for storing data values,
   
x = 23
y = 'asit'
print(x)
print(y)

#casting
#want to specify the data typs of a variable
#  x = str(3)  '3'
# y = int(3)     3
# z = float(3)   3.0


#Get the tpye of variable

x = 5
y = 'asit'
print(type(x))
print(type(y))



#many values to multiple variable\


x,y,z = 'asit','amit','asit kumar'
print(x)
print(y)
print(z)



#one value to multiple variable

x=y=z = 'asit kumar'
print(x,y,z)



name = ['asit','dheeraj','amit']
x,y,z = name
print(z)
print(x)
print(y)



#globle variables:-outside the function

x = 'Asit kumar'
def myfunction():
    print("My name "+x)
myfunction()
    



X = 'asit'
def myfunction():
    x = 'kumar'
    print("My name is "+x)
myfunction()

