dic = {
    1:'Krishna',
    2:'Jay',
    3:'Yash',
    4:'Aniket'
}
print(dic)
print(dic[1])
# print(dic[9]) #throws error if 9 is not present in dictionary
print(dic.get(9)) #prints None. Do not shows error

for names in dic.values():
    print(names)


for key in dic.keys():
    print(dic[key])

print(dic.keys())
print(dic.values())

for key in dic.keys():
    print(f"The value corresponding to {key} is {dic[key]}")

print(dic.items())

for key,value in dic.items():
    print(f"The value corresponding to {key} is {value}")

'''Dictionary Methods'''
#update method and clear method - same as sets

#pop and popitem
dic.pop(4)
print(dic)
dic.popitem() #deletes last item
print(dic)

#del keyword - it can delete entire dictionary or a specified item
del dic[2]
print(dic)
# del dic
# print(dic)

dic.clear()
print(dic)

dic.update({1:"Krishna",2:"Shivendra",3:"Rugved"})
print(dic)