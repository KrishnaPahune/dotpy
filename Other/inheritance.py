class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def show(self):
        print(f"The name of Employee: {self.id} is {self.name}")

class Programmer(Employee):
    def __init__(self, name, id,pid,language):
        super().__init__(name, id)
        self.pid=pid
        self.language=language
    
    def info(self):
        print(f"The language of the programmer {self.pid} is {self.language}")

p = Programmer("Ravi",101,12,"python")
p.show()
p.info()