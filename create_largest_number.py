# def create_largest_number(number_list):
#     sort_list = sorted(number_list,reverse=True)
#     larg_num = 0
#     for num in range((len(sort_list))):
#         larg_num =  str(larg_num) + str(sort_list[num]) 
#     return int(larg_num[1:])
# number_list=[23,4,456,5,67]
# largest_number=create_largest_number(number_list)
# print(largest_number)

def create_largest_number(number_list):
    sort_list_str = [str(num) for num in number_list]
    sort_list = sorted(sort_list_str, reverse=True)
    larg_num = ''.join(sort_list_str)
    return larg_num

number_list=[23,4,456,5,67]
largest_number=create_largest_number(number_list)
print(largest_number)



def create_largest_number(numbers):
    # Convert numbers to strings
    num_strings = [str(num) for num in numbers]
    
    # Custom sorting function: Sort in descending order based on concatenated forms
    num_strings.sort(reverse=True)
    
    # Join the sorted strings to form the largest number
    largest_number = ''.join(num_strings)
    
    return largest_number

# Test the function
numbers = [23, 45, 67, 89, 12]
largest = create_largest_number(numbers)
print("Largest number:", largest)  # Output: 8967452312



# strings = [1, '2', '1']

# # Join the list into a single string using space as separator
# result = ''.join(strings)
# print(result)  # Output: Hello World Python



