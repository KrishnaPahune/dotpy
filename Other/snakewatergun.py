import random

def check(user,comp):
    if user==comp:
        return 0
    if (user == 1 and comp == 0):
        return -1
    if (user == 0 and comp == 2):
        return -1
    if (user == 2 and comp == 1):
        return -1
    return 1

user = int(input("0 for snake, 1 for water, 2 for gun:\n"))
comp = random.randint(0,2)

print("User:",user)
print("COmputer:",comp)

score = check(user,comp)

if score == 0:
    print("Its a draw!")
elif score == 1:
    print("You Won")
else:
    print("You Lose")
    
    