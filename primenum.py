def prime(n):
    if n==1:
        print('Number is not prime')
    elif (n>1):
        for i in range(2,n):
            if (n % i)==0:
                print('Number is not prime')
                break
        else:
            print('Number is prime')
    else:
        print('Number is not prime')

prime(int(input('Enter the number : ')))





