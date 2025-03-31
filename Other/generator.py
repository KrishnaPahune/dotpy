# Generators are defined using functions with the yield keyword instead of return.
# When yield is encountered, the function's state is saved, and execution resumes from that point when next() is called.
# meaning it generates values one at a time as needed instead of storing them in memory.

def generator():
    for i in range(5):
        yield i

gen = generator()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# Or 

for g in gen:
    print(g)