l=[int(i) for i in input().split()]
s=sorted(l)
L=[8,1,2,2,3]
for i in l:
    L.append(s.index(i))
print(L)
