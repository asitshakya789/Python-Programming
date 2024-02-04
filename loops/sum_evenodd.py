even_sum=0
odd_sum=0
for num in range(12,38):
    if num%2==0:
        even_sum+=num
    else:
        odd_sum+=num

print(f'Even Numbers Sum {even_sum}')
print(f'Odd Numbers Sum {odd_sum}')
