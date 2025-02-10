'''a decorator is a function that takes another function as an arguement and returns a new function that modifies the behaviour 
of the original function'''

def greet(original_function):
    def modified_function():
        print("Welcome to our function")
        original_function()
        print("Thank you for using this function")
    
    return modified_function

@greet
def hello():
    print("Hello WOrld")

hello()

'''Another approach'''

greet(hello)()