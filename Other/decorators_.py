def greet(original_function):
    def modified_function(*args,**kwargs):
        print("Welcome to our function")
        original_function(*args,**kwargs)
        print("Thank you for using this function")
    return modified_function

@greet
def add(a,b):
    c=a+b
    print(c)
@greet
def sub(a,b):
    c=a-b
    print(c)
@greet
def hello():
    print("Hello WOrld")

add(1,2)
sub(4,5)
hello()