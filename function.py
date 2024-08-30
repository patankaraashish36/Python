def listd(a,b):
    print(a*b)
    print(a/b)
c=8
d=6
listd(c,d) #DEFAULT ARGUMNENT


def greaterorlesser(a,b):
    if(a>b):
        print("a greater")
    else:
      print("b grater or equal")
greaterorlesser(c,d)


# --- TYPES of function ---

# The two main type of function in python are :

# 1. built-in function 
# 2.user defineed function


def add(a,b):
    print( a,b)
add('a','b')


def add(a,b):
    return ( a,b)    # Return a tuple
a=add('a','b')
print(a)