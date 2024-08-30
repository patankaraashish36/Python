for i in range(100):
    num = int(input("Enter the Number if you to check number is prime or not. : "))
    if num == 1:
        print("Number is not prime.")
    elif (num > 1):
        for i in range(2, num):
            if num % i == 0:
                print("Number is not prime.")
                break
        else:
            print("Number is prime.")
    else:
        print("Number is not prime.")

    year = int(input("Enter the year you want to check leap yes or not. : "))
    if (year % 400 == 0) and (year % 100 == 0):
        print("Year is LeapYear")
    else:
        print("Year is not LeapYear")