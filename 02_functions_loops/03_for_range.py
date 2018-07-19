numbers = range(1, 100)
primes = []

for i in numbers:
    isprime = True
    for j in range(2, i):
        if i % j == 0:
            isprime = False
    if isprime:
        primes.append(i)
        

print(f"primes: {primes} {len(primes)}")
