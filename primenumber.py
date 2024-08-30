# # list1= [1,1,1,2,2,2,3,4,4,4,9,2,2,2,3,3,3,5,65,7,8,6,5,7,78,6,5,4,4,3,3]
# # print(list(set(list1)))


# for i in range(100):
#     num=int(input('Enter the number : '))
#     if num == 1 or num ==0:
#         print("number is not prime.")

#     elif num>1:
#         for i in range(2,num):
#             if num % i ==0:
#                 print("number is not prime")
#                 break
#         else:
#           print("Number is prime :")
    # else:
    #     print("number is not prime..")

# def leapyear(n):
#     if n % 400 ==0 and n % 100 == 0:
#         print("leap year")
#     else: 
#         print("not")

# leapyear(2007)

print( 1 + True + 1)   # True = 1


# num = int(input("Enter a Number : "))

# if (num == 1) or (num ==0) :
#     print("The Number is Not Prime.")
# else:
#     for i in range(2,num):
#         if (num % i) == 0 :
#             print("Number is not Prime")
#             break
#     else:
#         print("Number is Prime.")


# print(5%6)
# print(5 % 5)

year = int(input())
if (year % 4 == 0 and year % 100!= 0) or (year % 400 == 0) :
    print("Leap year") 
