max_value=0
min_value=0
for i in range(10):
    num=int(input("Enter any number "))
    if i==0:
        max_value=num
        min_value=num
    else:
        if num>max_value:
            max_value=num
        elif num<min_value:
            min_value=num


print(f'Minimum Value {min_value}')
print(f'Maximum Value {max_value}')
