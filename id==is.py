x=4
y=10
# print(x==y)
# print(id(x))
# print(id(y))
# z=10
# print(id(z))
# print(x is y)
print(x|y)


# [on_true] if [expression] else [on_false] 
print("XX" if x>y else "YY" )


a, b = 10, 5

print ("Both a and b are equal" if a == b  else "a is greater than b"  if a > b else "b is greater than a")


# The above approach can be written as: 

if a == b:
    print("Both a and b are equal")
else:
    if a > b:
        print("a is greater than b")
    else:
        print("b is greater than a")


# Python program to demonstrate ternary operator
a, b = 100, 20

# Use tuple for selecting an item
# (if_test_false,if_test_true)[test]
# if [a<b] is true it return 1, so element with 1 index will print
# else if [a<b] is false it return 0, so element with 0 index will print
print( 'tuple',(b, a) [a < b] )

# Use Dictionary for selecting an item
# if [a < b] is true then value of True key will print
# else if [a<b] is false then value of False key will print 
print('Dictionaries',{1: a, 0: b} [a < b])

# lambda is more efficient than above two methods
# because in lambda  we are assure that
# only one expression will be evaluated unlike in
# tuple and Dictionary
print('lambda',(lambda: b, lambda: a)[a < b]())



'''When condition becomes true, expression [on_false]
   is not executed and value of "True and [on_true]"
   is returned.  Else value of "False or [on_false]"
   is returned.
   Note that "True and x" is equal to x. 
   And "False or x" is equal to x. '''
# [expression] and [on_true] or [on_false] 

# Program to demonstrate conditional operator
a, b = 10, 20

# If a is less than b, then a is assigned
# else b is assigned (Note : it doesn't 
# work if a is 0.
#  Note that "True and x" is equal to x. 
#    And "False or x" is equal to x.
min = a < b and a or b

print('and AND or',min)

'''The reason for that is if the expression is true, the interpreter will check for the on_true, if that will be zero or false, that will force the interpreter to check for on_false to give the final result of the whole expression.

'''

