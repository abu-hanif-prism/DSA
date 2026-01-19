import time
import math
import timeit
#Is n a prime number?
#Brute Force
# n / 2->n-1  [odd numbers]
def BruteForce(n):
    if n <=  1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
        
    return True

# let n=a.b where a -> (2,n-a)
# let b <= a
# b.a <= a**2 >>>> n <=a**2 >>> a>= sqrt(n)

def SquareRoot1(n):
    if  n  <= 1:
        return  False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return  True 

def SquareRoot2(n):
    if n <= 1:
        return False
    for  i  in range(2,int(n**0.5)+1):
        if n  % i == 0:
            return False
    return True

n = 10**80+3
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
start = time.perf_counter()
print("Brute Force:" ,BruteForce(n))
print("Time:",time.perf_counter()-start)

start = time.perf_counter()
print("SQRT1" ,SquareRoot1(n))
print("Time:",time.perf_counter()-start)

start = time.perf_counter()
print("SQRT2" ,SquareRoot2(n))
print("Time:",time.perf_counter()-start)


print("###############################################")

print("Brute Force:",timeit.timeit("BruteForce(n)",globals = globals(),number = 3))
print("sqrt1",timeit.timeit("BruteForce(n)",globals = globals(),number = 3))
print("sqrt2",timeit.timeit("BruteForce(n)",globals = globals(),number = 3))