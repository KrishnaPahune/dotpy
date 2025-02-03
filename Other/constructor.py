class Person:

    def __init__(self,n,o):
        print("Hey i am a person")
        self.name=n
        self.occupation=o

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a=Person("Krishna","Liutenant")
b=Person("Prasad","Captain")
a.info()
b.info()
a.occupation="squadron leader"
a.info()

class Student:
    def __init__(self,a,w):
        self.age=a
        self.weight=w
    def info(self):
        print(self.age,self.weight)

s=Student(10,35)
s.age=50
s.info()
        