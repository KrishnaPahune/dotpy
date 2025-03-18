#Example 1
a = False
print(a)
print(a:=True)

#Example 2
numbers = [1,2,3,4,5]
while((n:=len(numbers)) != 0):
    print(numbers.pop())

#Example 3
foods = list()
while((food:=input("Enter your fav food: ")) != "quit"):
    foods.append(food)
print(foods)

#Same code uses more lines without walrus
fruits = list()
while True:
    fruit = input("Enter your fav fruit: ")
    if fruit == "quit":
        break
    fruits.append(fruit)
print(fruits)