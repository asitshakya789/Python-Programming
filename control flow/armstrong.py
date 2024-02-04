num=int(input("Enter any number "))
num1=num
s=0
while num>0:
    r=num%10
    s=s+(r**3)
    num=num//10

if  s==num1:
    print(f'{num1} armstrong')
else:
    print(f'{num1} is not armstrong')