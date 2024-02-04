list1 = []
n = int(input("how many value:="))
for i in range (n):
    value = int(input("Enter value"))
    list1.append(value)
print(f'Before deleting  value {list1}')
value  = int (input("enter value to delet"))
if value in list1:
    i = list1.index(value)
    del list1[i]
    print(f'{value} is deleted from list')
    print(f'after deleting list is {list1}')
else:
    print(f'{value} not exist within list')
