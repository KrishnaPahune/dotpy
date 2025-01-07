class student:
    company="sumago"
    def info(self,name,course):
        print("Name: ",name)
        print("Course: ",course)
    marathi=50
    hindi=50
    def marks(self):
        print("Marathi: ",self.marathi)
        print("Hindi: ",self.hindi)
obj1=student()
print("Name of company is: ",obj1.company)
obj1.info("krishna","Python")
obj1.info("shivendra","Python")
obj1.marks()