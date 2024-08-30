
# #Function to return list containing first n fibonacci numbers.
# def printFibb(n):
#     # your code here
#     if n<0:
#         return "Enter the correct input."
#     elif n==0:
#         return 0
#     elif n==1 or n==2:
#         return 1
#     else:
#         return printFibb(n-1) + printFibb(n-2)
# printFibb(5)

# def printFibbo(n):
#         # your code here
#         prevn=0
#         currentn=1
#         for i in range(1,n):
#             print(currentn)
#             prev_prevn=prevn
#             prevn=currentn
#             currentn=prev_prevn+prevn
# printFibbo(5)

class solution:
    def printFibb(self,n):
           # your code here
           self.fibolist=[0,1]
           if n==1:
               return [0]
           elif n==2:
               return self.fibolist
           elif n==0:
               return []
           else:
               for i in range(2,n):
                Fibo=self.fibolist[-1] + self.fibolist[-2]
                self.fibolist.append(Fibo)
                return self.fibolist

res=solution()
res.printFibb(0)           


def majorityElement(A, N):
        #Your code here
        ha=N/2
        num=0
        counter=0
        for i in A:
            current_fre=A.count(i)
            if counter<current_fre:
                 counter=current_fre
                 num=i
                
        if ha<num:
            print(num)
majorityElement([1,3,3,3,2],5)






        # ha=N/2
        # num=0
        # counter=0
        # for i in A:
        #     if counter==0:
        #         num=A[i]
        #     if A[i]==num:
        #         counter=counter+1
        #     else:
        #         counter=counter-1
            
        # counter2 =0
        # if A[i]==num:
        #     counter2 +=1
            
                
        # if ha<counter:
        #     return num
        # else:
        #     return -1