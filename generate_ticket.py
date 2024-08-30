
def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    for i in range(no_of_passengers+1):
        info = airline + ":" +  source[0:3] + ":" + destination[0:3] + ":10"+ str(i)
        ticket_number_list.append(info)
    if no_of_passengers <=5:
        return ticket_number_list
    else:
        return ticket_number_list[-5:]
#Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI","Bangalore","Sydney",3))


# def generate_ticket(airline, source, destination, no_of_passengers):
#     ticket_number_list = []
#     for i in range(1, no_of_passengers + 1):
#         ticket_number = f"{airline}:{source[:3]}:{destination[:3]}:{i + 100}"
#         ticket_number_list.append(ticket_number)
    
#     if no_of_passengers <= 5:
#         return ticket_number_list
#     else:
#         return ticket_number_list[-5:]

# # Test the program with different passenger counts
# ticket_numbers_1 = generate_ticket("AI", "Bangalore", "London", 3)
# ticket_numbers_2 = generate_ticket("AI", "Bangalore", "London", 8)

# print("Ticket numbers for less than 5 passengers:", ticket_numbers_1)
# print("Ticket numbers for more than 5 passengers:", ticket_numbers_2)

