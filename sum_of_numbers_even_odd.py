def sum_of_numbers(list_of_num,filter_func=None):
    if filter_func is None:
        return sum(list_of_num)
    else:
        return sum(filter_func(list_of_num))

def even(data):
    even_list = []
    for i in data:
        if ((i % 2) == 0):
            even_list.append(i)
    return even_list
def odd(data):
    odd_list = []
    for i in data:
        if ((i % 2) != 0):
            odd_list.append(i)
    return odd_list

sample_data = range(1,11)

print(sum_of_numbers(sample_data,odd))
# data = [1,3,5,2,6,7,8,10,14,18]
# print(odd(data))
# print(even(data))

print("+"*50)

def sum_of_numbers(list_of_num,filter_func=None):
    if filter_func is None:
        return sum(list_of_num)
    else:
        return sum(filter_func(list_of_num))

def even(data):
    return  [ num for num in data if num % 2 == 0]
def odd(data):
    return  [ num for num in data if num % 2 != 0]

sample_data = range(1,11)

print(sum_of_numbers(sample_data,odd))
# data = [1,3,5,2,6,7,8,10,14,18]
# print(odd(data))
# print(even(data))