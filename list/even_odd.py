list = [33,55,6,4,22,33,66,77,44,32,55,64,73,88,354]
a = len(list)
even = 0
odd = 0
for i in range (a):
    if i %2 ==0:
        even = even +1
    else:
        odd=odd +1
print(f'total even{even}')
print(f'total odd {odd}')