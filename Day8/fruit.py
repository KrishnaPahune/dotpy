class fruits:
    def type(self,name,color):
        print("Name of the fruit is:",name)
        print("Color of fruit is:",color)
    
    def price(self,rate,quantity,name):
        print(f"Price of {name} is {rate}")
        total=rate*quantity
        print("Your total bill is",total)
obj1=fruits()
fruits.type("Mango","Red")
fruits.price(100,2,"mango")