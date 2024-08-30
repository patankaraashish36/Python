def human_pyramid(no_of_people):
    if(no_of_people==1):
        return 50
    else:
        return  no_of_people*50 + human_pyramid(no_of_people-2)
    

def find_maximum_people(max_weight):
    #write your logic here. You may invoke recursive function human_pyramid() wherever applicable
    no_of_people = 0
    if max_weight < 50:
        return 0 
    elif max_weight == 50:
        return  1
    else:
    
        return 1 + find_maximum_people(max_weight - 50*3)

#Provide different values for max_weight and test your program
max_people=find_maximum_people(500)
print(max_people)



  


# ticket_list = ["AI567", "AI077", "BA896", "SI267", "AI077", "SI267","AI567"]
# def get_ticket_data():  #function to return the ticket_list
#     return ticket_list

#  print(get_ticket_data())



# import pandas as pd
# x = pd.Series([1,2,3,4,5,6,7,8])
# print(x)
# x[0]= 100
# print(x)
# x[2:4] = [100,100]
# print(x)