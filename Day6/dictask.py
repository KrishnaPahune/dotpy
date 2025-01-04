empty_dict={}
print(f"Empty_dict: {empty_dict}")
food_stock={'Apple':10,'Banana':15,'Oranges':8}
print(f"Food stock: {food_stock}")
banana=food_stock.get('Banana')
print(f"Amount of banana is {banana}")
food_stock.update({'grapes':20})
print(f"Food stock: {food_stock}")
if 'Apple' in food_stock:
    print(f"Aplle is present in food stock with quantity {food_stock.get('Apple')}")
else:
    print("Apple is not present in food stock")
keys=food_stock.keys()
print(f"keys in food stock are {keys}")
values=food_stock.values()
print(f"keys in food stock are {values}")
food_stock.update({'Oranges':12})
print(f"Food stock: {food_stock}")
print(f"length of foodstock is: {len(food_stock)}")

