# def my_function(food):
#     for x in food:
#         print(x)
# fruits = ["Apple","Banana","Grapes"]
# my_function(fruits)



# def my_function(x):
#     print(x)
# my_function(4)
-

#  Combilne positional argument

def my_function(a,b,/,*,c,d):
    print(a+b+c+d)
my_function(5,6,c=7,d=8)

