salary=int(input("Enter Salary "))
service=int(input("Enter Service "))
if service>10:
    bonus=salary*10/100
elif service>=6 and service<=10:
    bonus=salary*8/100
else:
    bonus=salary*5/100

print(f'Salary {salary}')
print(f'Bonus {bonus}')
