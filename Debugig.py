count=0
i=1
for baggage_weight in 29, 30, 31, 32, 28:
    if(baggage_weight>=1 and baggage_weight <=30):
        print("Passenger",i,": Proceed for baggage check.")
        count+=1
    else:
        print("Passenger",i,": Maximum baggage weight allowed is 30kg.")
    i+=1
print("No. of passengers who cleared baggage check:", count)


#PF-Tryout
'''This program is expected to display all the even numbers
between 1 and n (both inclusive)'''
i=1
n=10
while(i<=n):
    if(i%2==0):
        print(i)
        i+=1
    else:
        i+=1
    
