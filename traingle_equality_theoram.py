#lex_auth_012693802383794176153

def form_triangle(num1,num2,num3):
    #Do not change the messages provided below
    success="Triangle can be formed"
    failure="Triangle can't be formed"

    #Write your logic here
    if (num1 + num2 > num3) and (num1 + num3 > num2) and (num2 + num3 > num1):
        return success
    else:
        return failure


    #Use the following messages to return the result wherever necessary
    
    

#Provide different values for the variables, num1, num2, num3 and test your program
num1=2
num2=4
num3=5
x = form_triangle(num1, num2, num3)
print(x)