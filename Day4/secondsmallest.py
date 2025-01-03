li=[4,5,6,100,2,3,7,8,9]
smallest=li[0]

for i in li:
    if i<smallest:
        smallest=i
    i += 1

print(f"Smallest is {smallest}")
li.sort()
print(li)
k=1
while k < len(li):
    if li[k]==smallest:
        k += 1
    if li[k] > smallest:
        print(f"Second smallest is {li[k]}")
        break

