class Person:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    
    @classmethod
    def from_string(cls,string):
        name,age=string.split(",")
        return cls(name,int(age))

string="Krishna,22000"    
person = Person.from_string(string)
print(person.name,person.salary)

p=Person("harry",22000)
print(p.name,p.salary)