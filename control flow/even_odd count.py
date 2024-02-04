num = int (input ("Enter the number="))

ocount = 0
ecount =0
while num >0:

    division = num %10
    num = num//10
    if division%2 ==2:
        ecount = ecount+1
    else:
        ocount = ocount+1
print(f'event {ecount} odd {ocount}')