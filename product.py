def find_product(num1,num2,num3):
    product=0
    #write your logic here
    if num1 == 7:
        return num2 * num3
    elif num2 == 7:
        return num3
    elif num3 == 7:
        return -1
    
    else:
        return num1*num2*num3


#Provide different values for num1, num2, num3 and test your program
product=find_product(3,6,0)
print(product)