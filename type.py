a="Aashish patankar"
print(a,type(a))

print(type([]) is list)
print(type({}) is not dict)
print(type({}) is dict)

# Types of Type of Convertion --------

''' There are two types of Type Conversion in Python:

1.Implicit Type Conversion
2.Explicit Type Conversion   '''

'''                         Implicit Type Conversion

In Implicit type conversion of data types in Python, the Python interpreter automatically converts one data type to another without any user involvement. To get a more clear view of the topic sees the below examples.'''
# Example ---
a=10
b=10.6
c=a+b
print(a+b,type(a+b))
print(c , type(c))


'''                             Explicit Type Conversion
In Explicit Type Conversion in Python, the data type is manually changed by the user as per their requirement. With explicit type conversion, there is a risk of data loss since we are forcing an expression to be changed in some specific data type.  Various forms of explicit type conversion are explained below:
 

1. int(a, base): This function converts any data type to an integer. ‘Base’ specifies the base in which the string is if the data type is a string.
2. float(): This function is used to convert any data type to a floating-point number. '''

# Example-----
a='1010'
b=10.6
f=float(a)
c=int(a,2)
print(c)
print(f)


def function():
    pass

print(type(function()))

a=1//2
b=1.0/2  # == 1/2
print(a+b)
print(a)
print(b)
