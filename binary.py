def print_formatted(number):
    # your code goes here
    for i in range(1, number+1):
        print(i, oct(i)[2:], hex(i)[2:].upper(), bin(i)[2:])
            
print_formatted(17)