num = int (input("Enter the number:-"))
lastdigit = num %10
print(f'last digit of {num} of digit{lastdigit}')
if(num%2==0):
    print("Number is even")
else:
    print("Number is odd")