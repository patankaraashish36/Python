# def check_double(number):
#     num_set = set(str(number))
#     double_set = set(str(number * 2))
#     if len(str(number)) == len(str(number * 2)) and num_set == double_set:
#         return True
#     else:
#         return False
# #Provide different values for number and test your program
# print(check_double(10))


# a = int(input("a :"))
# b = int(input("b :"))
# c = a
# a = b
# b = c

# print("a = :",a,"b = :",b)


# a ,b = map(int,input().split())
# a, b = b, a
# print(a)
# print(b)

# a = input()
# b = a.split()
# print(b)

# a = int(input())
# temp = a
# s = ""
# while (temp > 0):
#     rem = temp % 10
#     s = s + str(rem)
#     temp = temp//10
# print(int(s))


a = int(input())
temp = a
s = ""
while (temp > 0):
    rem = temp % 10
    s = s + str(rem)
    temp = temp//10
if int(s) == a:
    print("Palindrome")
else:
    print("Not Palindrome")