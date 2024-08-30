# a=int(input("Enter"))
# b=int(input("Enter"))
# def gcd(a,b):
#     if a>b:
#         small =b
#     else:
#         small = a

#     for i in range(1,small+1):
#         if ((a % i == 0) and (b % i == 0)):
#             gcd=i
#     print(gcd)
    
# gcd(a,b)


# def gcd(x,y):
#     if y == 0:
#         return (x)
#     else:
#         return gcd(y,x % y)

# print(gcd(48,60))
a=48
b=66

while b:   #  run untill it becomes zero

    a,b=b,a%b
print(a)

a=6
print("This is ++a :",++a)  # not give error but return 6 value 
# print(a++) syntax error python has not ++ or -- python have += and -= 






        
