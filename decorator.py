# def hello(func):
#   def hyy():
#     print("hyy i am aashish")
#     func()
#     print("nothing how are you fine na yar")
#   return hyy
  
# @hello
# def ap(): 
#   print("how are you doing")

''' calculate the fuction execution time.'''

# import time
# def count_execution_time(func):
#     def wrapper(*args):
#         st = time.time()
#         func(*args)
#         print('Excution Time of : ', func.__name__, time.time() -  st)
#     return wrapper

# @count_execution_time
# def square(a):
#     time.sleep(1)
#     print(a**a)
  
# square(4)


# Check sanity data-type.

def sanity_check(data_type):
    def outer_wrapper(func):
        def inner_wrapper(*args):
            if type(args[0]) == data_type:
                func(*args)
                print("Are tune to ise run kar liya re")
            else:
                raise TypeError("Chal Nikal yaha se, Tere bas ki bat nhi.")
        return inner_wrapper
    return outer_wrapper


@sanity_check(int)
def power(a):
    print(a**a)

power(5)

print(type((1)))
