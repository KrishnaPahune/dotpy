li=[1,2,3,3,4,5,4]
i=0
while i < len(li):
    k=0
    while k < len(li):
        if k == i:
            k += 1
        elif li[k]==li[i]:
            li.pop(k)
            k += 1
        else:
            k+=1
    i+=1
print(li)
        
li2=[5,7,9,9,7]
for i in li2:
    if li2.count(i) > 1:
        li2.remove(i)

print(li2)