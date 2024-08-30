def hello(*args,**kwargs):
    print(args)
    print(kwargs)

hello(1,4,55,6,6,6, [4242,44], work="coding")

def function(a):
    global b
    return a+b
def func(b):
    global a 
    return a+b
def f():
    return a+b
print(function(1), func(3,5) , f(4,6))