from os import name


def args(*args):    
    sum = 0
    for i in args:
        sum = sum + i
    print(sum)
args(1,2,3,4,5,6,7,8,9)   # tuple 

# def args(*args,name):    
#     sum = 0
#     for i in args:
#         sum = sum + i
#     print(sum)
# args(1,2,3,4,5,6,7,8,9,"Aashish")  # This gives an error becouse position argument always come first "Aashish" consider as *args argumet  Error Name -- TypeError: args() missing 1 required keyword-only argument: 'name' .



def args(name ,*args):    
    sum = 0
    for i in args:
        sum = sum + i
    print(sum)
    print(name)
args("Aashish",1,2,3,4,5,6,7,8,9)  # This code is run. first argument is associate with always name


def kwargs(**kwargs):     # The sequence is - normal argument , *args , **kwargs.
    for key, value in kwargs.items():
        print(f"{key} adore {value}")
 
info = {"Aashish" : "PLV", "PLV" : "Aashish"}
kwargs(**info)      # If you write kwargs(info) it will show error name -- TypeError: kwargs() takes 0 positional arguments but 1 was given