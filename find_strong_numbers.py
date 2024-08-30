def factorial(number):
   if (number == 0) or (number == 1):
       return 1
   else:
       fact = number * factorial(number - 1)
       return fact
def find_strong_numbers(num_list):
    new_list =[]
    for num in num_list:
        temp = num
        sum = 0
        while (temp):
            rem = temp % 10
            sum += factorial(rem)
            temp = temp//10 
            if num == sum :
                new_list.append(sum)
    return new_list
    
num_list=[0,145,375,100,2,10]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)