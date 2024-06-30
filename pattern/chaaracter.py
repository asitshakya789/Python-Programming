p = 65
n = int(input("Enter the number:-"))
for i in range(n):
    for j in range (i+1):
        print(chr(p),end='')
    p=p+1
    print()