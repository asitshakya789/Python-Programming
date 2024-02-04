list = [1,3,5,-3,5,-6,-7,7,32,4,2,-5,-6]
print(f'Negative value of list')
a = len(list)
for i in range(a):
    if list[i]<0:
        print(list[i],end=" ")
    print()
print(f'positive value of list')
for i in range(a):
    if list[i]>=0:
        print(list[i],end=" ")
    print()