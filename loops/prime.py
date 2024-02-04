mun = int (input("Enter thenumber:="))
c=0
for i in range(1,mun+1):
    if i%2==0:
        c=c+1
if c==2:
    print(f'{mun} is prime')
else:
    print(f'{mun} is not prime')
