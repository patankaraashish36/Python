# x = int(input("2"))
# y = int(input("2"))
# z = int(input("2"))
# n = int(input("2"))
# x2=[num for num in range(x+1)]
# y2=[num for num in range(y+1)]
# z2=[num for num in range(z+1)]

# liscom=[[i,j,k] for i in x2 for j in y2 for k in z2 ]
# print(liscom)



# massage="hello"
# a,b,c,d,e="hello"
# print(a,b)
# print(c,d,e)
# massage=89
# massage=67.9
# massage=True
# print(massage)

# word = "Machine Learning"
# text = word.split()
# print(text)
# print(type("".join([i[0].upper() for i in text])))
# print("".join([i[0].upper() for i in text]))

# name=[input(":")]
# print(type(name),name)
# hello=int(input(":"))
# l=[[num ,hello] for num in name]
# l2=sorted(l)
# print(l2)
# print(l2[1][1])
# for i in range(len(l)):
#     if l[i][1]>30:
#         print(l[i][1])
# print(l)


# [1, 2, 3, 4, 5, 6, 7, 8, 9]


# def sortOddEven(nums):
#     # Write your code here.
#     even_l = []
#     odd_l = []
#     for i in nums:
#         if  i % 2 == 0:
#             even_l.append(i)
#         else:
#             odd_l.append(i)

#     even_l.sort()    
#     odd_l.sort(reverse=True)

#     return [odd_l + even_l]


def sortOddEven(nums ):
    # Write your code here.
    even_l = []
    odd_l = []
    for i in nums:
        if  i % 2 == 0:
            even_l.append(i)
        else:
            odd_l.append(i)

    for j in range(len(even_l)-1):
        if even_l[j] > even_l[j+1]:
            even_l[j+1]  = even_l[j]

    for k in range(len(odd_l)-1):
        if odd_l[k] < odd_l[k+1]:
            odd_l[k+1] = odd_l[k]

    result = even_l  + odd_l

    return result

print(sortOddEven([2,4,7,8,4,9,1]))
