def checkprime(no):
    i = 2 
    while i <= no/2:
        if no % i == 0:
            break
        i += 1
        return i == no //2+1
    num = int(input("Enter a no :"))
    fnum = 2
    while fnum <=num:
        if(checkprime(fnum) == True):
            print(fnum)
            fnum +=1 