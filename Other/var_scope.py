'''local variables can be accessed within a function and cannot be accessed outside a function
    a global variable can be used anywhere.
    You cannot change a global variable permanantly in a function.
    To change a global variable permenantly in a function, use the "global" keyword'''
x=10
def var():
    global x
    y=5
    x=7
    print(y)
    print(x)
print(x)
var()
print(x)

