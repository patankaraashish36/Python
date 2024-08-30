''''Python While Loop is used to execute a block of statements repeatedly until a given condition is satisfied. And when the condition becomes false, the line immediately after the loop in the program is executed.'''

# While loop falls under the category of indefinite iteration. Indefinite iteration means that the number of times the loop is executed isn’t specified explicitly in advance. 


i = 0
# j=0
while(i<5):
    print('This is i : ',i)
    i= i+1 


# ---- Single Statement While loop ----
a=[1,2,3,4]
while a : print(a.pop())
 

c=0
while c<5: print('This is c : ',c) ; c=c+1

j=0
while j<6:
    if j==3:
        j=j+1
        continue
    print(j)
    
    if j >5:
        break
    j+=1

    
  
