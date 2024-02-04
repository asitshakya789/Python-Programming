list1=[]
n=int(input("How many values ?"))
for i in range(n):
    value=int(input("Enter any value "))
    list1.append(value)

print(f'Before Swaping {list1}')
pos1=int(input("Enter Pos1 "))
pos2=int(input("Enter Pos2 "))
temp=list1[pos1-1]
list1[pos1-1]=list1[pos2-1]
list1[pos2-1]=temp

print(f'After Swaping {list1}')
