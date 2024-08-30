def pa(x,y):
    print(x+y)
pa(4,6)


# LOCAL AND GLOBAL VARABALE

def ap():
    x=4 # local variable
    global y
    y=5 # global variable This variable can access out of the function 
    print(x+y)

ap()
print(y) # Global variable
# print(x) # Local variable  GENRATE ERROR


