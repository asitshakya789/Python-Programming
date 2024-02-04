cost = int (input("Enter the bike price:-"))
if cost>100000:
    tax = cost *15/100
elif cost>50000 and cost<100000:
    tax = cost*10/100
elif cost<=50000:
    tax = cost*5/100
print(tax)