l1=list(range(15))
l2=list(range(15))
print(l1)
print(l2)
x=[(x+y) for x,y in zip(l1,l2)]
print(x)
l3=[(x+y) for x,y in l1]
# print(l1,l2)