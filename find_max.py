def find_max(num1, num2):
    max_num=[]
    digit_sum = 0
    if num1 >= num2 :
        return -1
    else:
        for num in range(num1, (num2+1)):
            digit_sum = sum(int(i) for i in str(num)) 
            if (digit_sum % 3 == 0) and len(str(num)) == 2 and (num % 5 ==0 ):
                max_num.append(num)
    if not max_num:
        return -1
    else:
        return max(max_num)

#Provide different values for num1 and num2 and test your program.
max_num=find_max(10,15)
print(max_num)



'''# 1. Always num1 should be less than num2

# 2. Consider each number from num1 to num2 (num2 inclusive). Populate the number into a list, if the below conditions are satisfied

#       a. Sum of the digits of the number is a multiple of 3

#       b. Number has only two digits

#       c. Number is a multiple of 5

# 3. Display the maximum element from the list

# In case of any invalid data or if the list is empty, display -1.'''