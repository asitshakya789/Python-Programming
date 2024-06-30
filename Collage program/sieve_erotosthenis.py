def prime_erotosthenis(n):
    prime_list = []
    for i in range(2,n+1):
        if i not in prime_list:
            print(i)
        for j in range(i*i,n+1,i):
            print(list.append(j))
print(prime_erotosthenis(100))