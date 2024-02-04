n = int (input("Enter how many values "))
list1 =[]
for i in range(n):
    value = int (input("Enter the value"))
    list1.append(value)
print(f'before shorting values{list1}')
for i in range (n):
    for j in range(0,n-1):
        if list1[j]>list1[j+1]:
            temp = list1[j]
            list1[j] = list1[j+1] 
            list1[j+1]= temp
        

print(f'after sorting {list1}')