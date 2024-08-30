# a = int(input())
# pdm = ""
# temp = a
# while (temp > 0):
#     rem = temp % 10
#     pdm += str(rem)
#     temp = temp // 10
# if (a == int(pdm)):
#     print("Palindrome")
# else:
#     print("Not")




# num = int(input())
# for i in range(1,11):
#     print(num*i)

# num = int(input())
# for i in range(1,11):
#     print(f"{num} x {i} = ",num*i)

# num = int(input())
# diviser = int(input())

# if (num % diviser == 0):
#     print("Divisible")

# else:
#     print("Not Divisible")

# num1 = int(input())
# num2 = int(input())

# for i in range(num1, num2):
#     if (i%2 == 0):
#         print(i)

# num1 = int(input())
# num2 = int(input())

# for i in range(num1, num2):
#     if (i%2 != 0):
#         print(i)


# num = int(input())
# print(int(len(str(num))))
# print(type(num))

# num1 = int(input())
# num2 = int(input())

# print(num1**num2)

# inputNumber = 25

# # getting the square root of a number using the exponential operator**
# squareRoot = inputNumber**(1/2)

# # printing the square root of a number
# print("The square root of", inputNumber, "=", squareRoot)


# num = 25

# sqr = num ** 1/2
# print(sqr)

# a = int(input())
# sum = 0
# temp = a
# while (temp > 0):
#     rem = temp % 10
#     if (rem%2 != 0):
#         sum = sum + rem
#     temp = temp // 10
# print(sum)


# a = int(input())
# sum = 0
# temp = a
# while (temp > 0):
#     rem = temp % 10
#     sum = sum + rem
#     temp = temp // 10
# if (sum == 10):
#     print("Magic Number")
# else:
#     print("Not")


# a = int(input())
# product = 1
# temp = a
# while (temp > 0):
#     rem = temp % 10
#     product = product * rem
#     temp = temp // 10

# print(product)


# a = int(input())
# product = 1
# sum = 0 
# temp = a
# while (temp > 0):
#     rem = temp % 10
#     product = product * rem
#     sum = sum + rem
#     temp = temp // 10

# if (product == sum):
#     print("SPY Number")
# else:
#     print("Not")

# num = int(input())
# sum = 0
# product = 1
# for i in range(1,num):
#     if (num % i == 0):
#         sum = sum + i
#         product =  product * i
#         print(product)
# if (num == sum):
#     print("Perfect")
# else:
#     print("Not")


# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)

# n = int(input())

# print(factorial(n))

# n = int(input())
# if (n == 1) or (n == 0):
#     print("Not")
# else:
#     for i in range(2,n):
#         if (n % i == 0):
#             print("Not")
#             break
#     else:
#          print("Prime")


a = 7
b = 0
for i in range(a):
    b = i + b
    c = b
    print(c)

  