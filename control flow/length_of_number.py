num = int(input("Enter the number:="))
c=0
if num == 0:
    c=1
else:
    while num>0:
        num = num //10
        c=c+1
print(f'cout of digit {c}')