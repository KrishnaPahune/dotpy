# try:
#     a = int(input())
#     print(f"Multiplication table of {a} is:")
#     for i in range(1,11):
#         print(f"{a} X {i} = {a*i}")
# except Exception as e:
#     print(e)

# print("Some important lines of code")
# print("End of program")

# try:
#     a = int(input())
#     print(f"Multiplication table of {a} is:")
#     for i in range(1,11):
#         print(f"{a} X {i} = {a*i}")
# except:
#     print("Invalid input")

# print("Some important lines of code")
# print("End of program")

# try:
#     b=int(input("enter a number"))
#     a = [1,2,3]
#     print(a[3])
# except IndexError:
#     print("Index chhota kr")
# except ValueError:
#     print("Invalid input")

# print("Some important lines of code")
# print("End of program")

# def fun1():
#     try:
#         a=[1,2,3]
#         i=int(input("enter a number: "))
#         print(a[i])
#         return 1
#     except:
#         print("Some error occurred")
#         return 0
#     print("always executed") #Never executed
# print(fun1())

# def fun2():
#     try:
#         a=[1,2,3]
#         i=int(input("enter a number: "))
#         print(a[i])
#         return 1
#     except:
#         print("Some error occurred")
#         return 0
#     finally:
#         print("always executed") #Always executed

# print(fun2())

# #Raising custom errors using raise keyword

# a=int(input("Enter a number between 5 and 9"))
# if a<5 or a>9:
#     raise ValueError("Value is not between 5 and 9")
while True:
    try:
        a = input("Enter a number between 5 and 9 or type ""quit"": ")
        if a=="quit":
            print("Exiting Program")
            break
        b=int(a)
        if b<5 or b>9:
            raise ValueError("Number is out of specified range")
        print("You have entered",b)
    except Exception as e:
        print(e)
