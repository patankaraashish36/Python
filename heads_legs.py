def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0

    #Start writing your code here
    #Populate the variables: chicken_count and rabbit_count
    # x = chicken
    # y = rabbit
    for chicken_count in range(heads+1):
        rabbit_count = heads - chicken_count
        if 2*chicken_count + 4*rabbit_count == legs:
            print(chicken_count,rabbit_count)
            break
    else:
        print(error_msg)

    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    #

#Provide different values for heads and legs and test your program
solve(150,400)