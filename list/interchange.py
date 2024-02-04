list1 =[1,23,4,5,6]
x= list1[0]
list1[0] = list1[-1]
list1[-1 ] = x
print(f'after swapping {list1}')
