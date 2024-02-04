
list1=[1,2,3,4,5]
a=len(list1)
if a%2!=0:
    mid=len(list1)//2
    print(f"Median {list1[mid]}")
else:
    mid=len(list1)//2
    print(f"Median {(list1[mid]+list1[mid-1])/2}")
