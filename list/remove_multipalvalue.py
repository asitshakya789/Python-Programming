
list1=[4,9,2,3,5,1,11,13,17,23,8,12,16,18,20,22]

print(f'Before Deleting values {list1}')
i=0
l=len(list1)
while i<l:
    if list1[i]%2==0:
        del list1[i]
        l=l-1
        continue
    i=i+1
        

print(f'After Deleting values {list1}')
