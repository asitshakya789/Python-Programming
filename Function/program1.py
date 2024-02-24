def removekth (s,k):
    str = ""
    for i in range (len(s)):
        if i!=k:
            str +str +s[i]
    return str
print(removekth('Python',1))
print(removekth('Python',3))