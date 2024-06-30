def removekth (s,k):
    str  =  " "
    for i in range(len (s)):
        if i !=k:
            str = str +s[i]
    return  str
print(removekth("hello",1 )) # should print hlo
print(removekth("world",2))   #