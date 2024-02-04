# list1 = [1,2,3,4,5,6,7,8,9,0]
# a =iter(list1)
# n = a.__next__()
# for i in a:
#     print(i,end='')

# names_list=["naresh","ramesh","suresh","kishore"]
# a=iter(names_list)
# n1=a.__next__()
# print(n1)
# for n in a:
#     print(n,end=' ')




# list1=[10,20,30,40,50]
# a=iter(list1)
# print(list1)
# print(a)


list1 = list (range(10,110,10))
a = iter(list1)
print(list1)
print(a)




list2 = list("abc")
a =iter(list2)
b=a.__next__()
print(list2)
print(b)
