'''generating random numbers in a particular range'''
import random
def generate_random_numbers(choice):
    if choice==1:
        print("Generating numbers from zero to 50:-")
        for i in range(10):
            print(random.randint(0,50),end=" ")
    elif choice==2:
        print("Generating numbers from 50 to 75:-")
        for i in range(10):
            print(random.randint(50,75),end=" ")
    else:
        print("Generating numbers from 75 to 120:-")
        for i in range(10):
            print(random.randint(75,120),end=" ")
            

print("""Select a range:
      \n1.0-50
      \n2.50-75
      \n3.75-120""")
choice=int(input("Enter your choice: "))

generate_random_numbers(choice)
