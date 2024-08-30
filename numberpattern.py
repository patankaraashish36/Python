class pattern: 

    # Problem 1 
    def firstAppr(self,n):              #1
        for i in range(n):              #11
            for j in range(i+ 1):       #111
                print(1,end="")         #1111
            print()  
        print("___________________________________")

    def secondAppr(self,n):
        for i in range(1,(n+1)):
             print(i*"1")
        print("___________________________________")

    def thirdAppr(self,n):
        s="1"
        for i in range(n):
            print(s)
            s=s+"1"
        print("___________________________________")


    # Problem 2
    def antPat(self,n):
        for i in range(n):                       #1234
            for j in range(1,(n-i)+1):           #123 
                print(j,end="")                  #12
            print()                              #1
        print("___________________________________")

    # Problem 3                           #1
    def thirdpatt(self,n):                #23
        for i in range(n):                 #345
           for j in range(n):
               print(j,end="")
               
           print()
n=4

p=pattern()
p.firstAppr(n)
p.secondAppr(n)
p.thirdAppr(n)
p.antPat(n)
p.thirdpatt(n)