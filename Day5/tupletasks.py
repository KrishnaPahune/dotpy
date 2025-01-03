tup1 = ("apple","banana","cherry")
print(tup1)
tup2=(1,2,3)
print(tup2)

print(tup1[1])

print(len(tup1))

print(tup1+tup2)

tup3=(1,2,3,4,5)
tup4=tup3[1:-1]
print(tup4)

tup5=("apple","banana","cherry","apple")
print(tup5.index("apple"))

tup6=(1,2,3,4)
if 3 in tup6:
    print(True)

tup7=("apple","banana","cherry")
print(tup7)
(a,b,c)=tup7
print(f"A: {a}\nB: {b}\nC: {c}")