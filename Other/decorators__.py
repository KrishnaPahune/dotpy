def greet(original_function):
    def modified_function(*args,**kwargs):
        print("Welcome to our function")
        original_function(*args,**kwargs)
        print("Thank you for using this function")
    return modified_function

def add(a,b):
    c=a+b
    print(c)

def hello():
    print("Hello WOrld")

greet(add)(1,2)
greet(hello)()