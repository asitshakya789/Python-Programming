list1=[]
n=int(input("Enter how many values?"))
for i in range(n):
    value=int(input("Enter value"))
    list1.append(value)

print(f'Before deleting values {list1}')
value=int(input("Enter value to delete "))
found=False
while True:
    if value in list1:
        i=list1.index(value)
        del list1[i]
        found=True
    else:
        break

if found==True:
    print(f'After deleting values {list1}')
else:
    print(f'{value} not exists in list')
