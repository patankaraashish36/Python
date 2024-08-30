#  MAPE 

lis=[11,3,5]
print(list(map(lambda x : x*x, lis)))

# FILTER 

print(list(filter(lambda a: a>5, lis)))

# REDUCE ( FOR USE RESUSE WE NEED TO IMPORT THE REDUCE)

from functools import reduce
print(reduce(lambda x,y: x*y, lis))

# import functools
# print(dir(functools))