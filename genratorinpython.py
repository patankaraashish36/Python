import math as m
import time
def genrator():
    for i in range(1,51):
        yield f"i {i} times"

gen = genrator()
print(next(gen))
# j=time.time()
# print(j)
# time.sleep(4)
# k=time.time()
# print(k)
# print(k-j)

list1=[4,2,4,33,54,546,56,6,2,54,4254,23,32,42,2,532,432,423,43,43,45,324,3,53,45,32,54,3,4532,523,543,64,43,543,43,43,45,345,3,4,2,42,5,353,54,34,34,24]

def gen():
    for i in list1:
        j=m.factorial(i)
        yield i
        print(j)
    
g=gen()

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))