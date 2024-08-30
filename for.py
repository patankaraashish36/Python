# for i in enumerate(['a','t','o']):
#     print(i)

# print("xyyzxyzxzxyy".count('xyy',2,11))

# k = "python"
# print(k[5:9])

# LIST COMPRAHENTION 

# variable=[exprition for exp.variable in range()]

movies=[("hello",2010),("avengers",2012),("endgame",2019),("kantara",2022)]
movielist=[title for title,years in movies if years >2010 ]

print(movielist)

arr = [-2, 3, -4, 0, 4, 1]

count_positive = ([num for num in arr if num > 0])
count_negative = ([num for num in arr if num < 0])
count_zero = ([num for num in arr if num == 0])

total = len(arr)

if total > 0:  # prevent division by zero
    ratio_positive = 3 / total
    ratio_negative = len(count_negative )/ total
    ratio_zero = 1/ total
else:
    ratio_positive = 0
    ratio_negative = 0
    ratio_zero = 0

print("Ratio of positive integers: {:.6f}".format(ratio_positive))
print("Ratio of negative integers: {:.6f}".format(ratio_negative))
print("Ratio of zero integers: {:.6f}".format(ratio_zero))



number = 2.5
result = number / 5


print(result)

arr = [-4, 3, -9, 0, 4, 1]

count_positive = 0  # initialize a counter for positive integers

for num in arr:
    if num >=0:  # Check if the number is positive
        count_positive += 1  # Increment the counter

print("Number of positive integers in the list:", count_positive)