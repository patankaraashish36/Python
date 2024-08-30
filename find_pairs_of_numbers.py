def find_pairs_of_numbers(num_list,n):
    numbers = set(num_list)
    count = 0

    for num in num_list:
       need = n - num 

       if need in numbers :
            # numbers.discard(num)
            count += 1

    return count - 1



num_list=[1, 2, 4, 5, 6]
n=6
print(find_pairs_of_numbers(num_list,n))