'''Enumerate() allows you to loop over a sequence such as list tuple or string
and get the value and index of each element in the sequenceat the same time'''

numbers=[7,8,9,44,5,6,11,22,3]
for index,value in enumerate(numbers):
    print(value)
    if(index==2):
        print("nooo")

'''the defaul indexing in ennumerate starts from 0 but we can set it manually 
using start parameter'''

numbers=[7,8,9,44,5,6,11,22,3]
for index,value in enumerate(numbers,start=2):
    print(value)
    if(index==2):
        print("nooo")
