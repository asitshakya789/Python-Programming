list1 = [1,2,3,4,5,6]
print(list1)
# list1[::] = list1[::-1]
# print(list1)



#second methos
list1 = [10,20,30,40,50]
list1[:4] = list1[:-6:-1]
print(list1)