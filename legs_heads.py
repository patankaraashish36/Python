def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0

    #Start writing your code here
    #Populate the variables: chicken_count and rabbit_count
    for x in range(heads+1):
        y = heads - x
        if 2*x + 4*y == legs:
            chicken_count = x
            rabbit_count = y
            break
    
    if chicken_count+rabbit_count == heads:
        print(chicken_count,rabbit_count)
    else:
        print(error_msg)

    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    #print(chicken_count,rabbit_count)
    #print(error_msg)

#Provide different values for heads and legs and test your program
solve(38,131)