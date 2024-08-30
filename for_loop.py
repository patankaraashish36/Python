from cgi import print_arguments


a=set(range(10)) # createing a set using range you can print list, tuple 
print(a)

#  ----For loop----
'''Python For loop is used for sequential traversal i.e. it is used for iterating over an iterable like String, Tuple, List, Set, or Dictionary.

In Python, there is no C style for loop, i.e., for (i=0; i<n; i++). There is a “for” loop which is similar to each loop in other languages. Let us learn how to use for in loop for sequential traversals

Note: In Python, for loops only implements the collection-based iteration.'''

for i in range(11):
   if i%2!=0:
       print(i)
      


# For loop with dictionaries

d={"A":1,"B":2,"C":3}

for i  in  d:
    print('This is dictionries : ',d.keys())
    print('This is dictionries : ',i,':',d[i])
    print("%s %d" %(i, d[i]))

# ----range----
'''The Python range() function returns a sequence of numbers, in a given range. The most common use of it is to iterate sequences on a sequence of numbers using Python loops'''

#  Syntax range(start,end,stop)

# For loop with break and continue statement

'''Python Continue Statement skips the execution of the program block from after the continue statement and forces the control to start the next iteration.'''


s=[1,2,3,4,5]
for i in s:
    if i ==3:
        continue
    elif i==2:
        continue
    else:
        print("else s:",s)
    print("s:",s)

