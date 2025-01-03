li=[1,2,3,4,5,6,7]
print(len(li))
if len(li) % 2 == 0:
    li.sort()
    mid1 = li[(int)(len(li)/2)-1]
    print(mid1)
    mid2 = li[(int)(len(li)/2)-1+1]
    print(mid2)
    median= (mid1+mid2)/2
    print(median)
else:
    li.sort()
    mid = li[(int)(len(li)/2)-1+1]
    print(mid)
