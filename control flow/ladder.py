units=int(input("Enter units"))

if units<=100:
    amt=0
elif units>100 and units<=200:
    amt=(units-100)*5
else:
    amt=0+500+(units-200)*10

print(f'Amount {amt}')
