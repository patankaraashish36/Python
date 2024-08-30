t = tuple(map(int, input().split()))
print(t)
print(type(t[0]))
print(hash(t))

t = map(tuple, input().split())
print(t)
# print(type(t[0]))
print(hash(t))