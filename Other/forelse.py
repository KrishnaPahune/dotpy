'''The else statement is executed after successful completion of all iteration of a loop.
If the loop is terminated by break statement then else statement is not executed'''

for i in range(1,5):
    print(f"iteration {i}")
else:
    print("All iterations completed")

print("Loop Over")

for i in range(1,5):
    if i == 3:
        break
    print(f"iteration {i}")
else:
    print("All iterations completed") #Not executed

print("Loop Over") #executed

