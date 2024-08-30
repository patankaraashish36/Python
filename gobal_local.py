x = 5
def add(y):
    if (y != 10):
        x = y+y  # Error 
        print( "x is ",x)
        print("Global Variable x =",x)
print(x)
add(5)
# print("Global Variable x =",x)

# def add(y):
#     x = 10
#     z = x+y
#     print(z)
#     print("Local Variable x =",x)

# add(5)
# print("Global Variable x =",x)



# def add(y):
#     global x 
#     x =10
#     z = x+y
#     print(z)
#     print(x)

# add(5)
# print("Global Variable x =",x)



result=0
def find_sum(num1,num2):
    if(num1==num2):
        result=num1+num2
    else:
        result=2*(num1+num2)
find_sum(3,4)
print(result)
find_sum(5,5)
print(result)



def find_avg(list_num):
    result_sum=0
    for num in list_num:
        result_sum+=num
    result_avg=result_sum/len(list_num)
find_avg([5,8,5])
print(result_avg)
 