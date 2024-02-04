m=int(input("enter value of m")) # 5
n=int(input("enter value of n")) # 20
for num in range(m,n+1): # start=5,stop=21,step=1 --> 5 6 7 8 9 10 ... 20
    if num%2==0:
        print(num)
