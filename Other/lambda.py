def double1(x):
    return x*2
print(double1(5))

double2 = lambda x: x*2
cube = lambda x: x**3
avg = lambda x,y: (x+y)/2

print(double2(5))
print(cube(5))
print(avg(5,15))

def appl(fun,value):
    return 6 + fun(value)

print(appl(cube,2))

'''lambda is mainly used for passing function as arguement to a function'''

print(appl(lambda x: x*2,5))