# Function caching is a technique used to store the results of expensive function calls and reuse them when the same inputs occur again.
# This speeds up programs significantly when dealing with recursive or repeated computations.

from functools import lru_cache
import time

@lru_cache(maxsize=None)

def expensive_function(n):
    time.sleep(5)
    return n*5

print(expensive_function(10))
print(expensive_function(20))
print(expensive_function(30))
print(expensive_function(40))
print(expensive_function(50))

print(expensive_function(10))
print(expensive_function(20))
print(expensive_function(30))
print(expensive_function(40))
print(expensive_function(50))
