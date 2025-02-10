'''in python there is no concept of public, private and protected. but using name mangling we can resemble a variable as private'''

class Person:
    def __init__(self):
        self.__name="Harry" # private a variable using ('__')
    
p = Person()
print(p._Person__name) # accessing private variables 