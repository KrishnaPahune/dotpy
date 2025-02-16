class Employee:
    company = "Apple"

    def show(self):
        print(f"{self.name} works in {self.company}")
   
    def changeCompany(self,newCompany):
        self.company=newCompany

e1=Employee()
e1.name="Harry"
e1.show()
e1.changeCompany("Mahindra")
e1.show()               # shows Mahindra
print(Employee.company) # prints Apple bcoz the changeCompany() method did change the instance variable but not the class variable
    
class Employee:
    company = "Apple"

    def show(self):
        print(f"{self.name} works in {self.company}")
    
    @classmethod                            
    def changeCompany(cls,newCompany):  # it changes the class variable directly
        cls.company=newCompany          # here cls is same as Employee

e1=Employee()
e1.name="Harry"
e1.show()
e1.changeCompany("Mahindra")
e1.show()               # shows Mahindra
print(Employee.company) # prints Mahindra. Class variable is now changed 