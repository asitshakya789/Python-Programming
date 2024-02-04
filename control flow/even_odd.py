num = int(input("Enter any number:="))
conut = 0
while num>0:
    r = num %10
    if r%2 ==0:
        conut = conut+1
    else:
        conut = conut+1
    num = num //10
print(f'even count digits {conut}')
print(f'odd count digit {conut}')