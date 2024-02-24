def factor (num):
    flist = []
    if num>1:
        for i in range(1,num+1):
            if num%i==0:
                flist.append(i)
        return flist
print(factor(4))