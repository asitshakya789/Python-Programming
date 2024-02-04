for num in range(2,21): # 2 3 4 5 6 7 8 9 10 11 12 13 ... 20
    c=0
    for i in range(1,num+1):
        if num%i==0:
            c=c+1
    if c==2:
        print(f'{num} is prime')
