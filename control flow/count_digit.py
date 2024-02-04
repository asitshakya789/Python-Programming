num = int (input("Enter the number:="))
c=0
while num>0:
    num=num //10
    c=c+1
print(f'The sum of digit {c}')