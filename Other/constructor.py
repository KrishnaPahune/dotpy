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