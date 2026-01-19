def prime_factorization(n):
    list1 = []
    d=2
    ### from previous math n = a.b
    while d*d <=n:
        count = 0

        while n%d == 0:
            n = n//d
            count+=1

        if count > 0:
            list1.append((d,count))
        d+=1
    if n > 1:
        list1.append((n, 1))

    return list1

print(prime_factorization(67893278923457897354893724))
print(prime_factorization(8434324233))
print(prime_factorization(8442767))