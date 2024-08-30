def lonelyinteger(a):
    # Write your code here
    for el in a : 
        if a.count(el)<=1 : 
            return el 
a =lonelyinteger([1,1,2,2,2])
print(a)