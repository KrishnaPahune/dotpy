emptyset = set()
print(type(emptyset))

primes={2,3,5,7,11}
print(primes)

primes.update({13,17})
print(primes)

evens={2,4,6,8,10}
print(evens)

evenprime=primes.intersection(evens)
print(evenprime)

even_or_prime=primes.union(evens)
print(even_or_prime)

prime_minus_even=primes.difference(evens)
print(prime_minus_even)

evens.remove(4)
print(evens)

if 7 in primes:
    print("7 is present in the set")
