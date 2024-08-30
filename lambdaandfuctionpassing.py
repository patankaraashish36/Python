cube=lambda x: x+3
print(cube(7) ," LAMBDA FUNCTION")

# function passing in function

def passing(fx,value):
    return 6+fx(value)

print(passing(cube,10), " FUNCTION PASSING")
h= lambda x : x*x

def hel(g,valu):
    return 6 + g(valu)
print(hel(h ,5))


print(0 or 1)