# MATCHE NUMBER AND SCORE
import random
a=random.randrange(10)

#IF YOU WANT TO CHECK A RANDOM NUMBER PLEASE UNCOMMENT
# print(a)

for j in range(1,11):
   # for k in range(100):   
   # if j<5:
   i=int((input("Enter a number b/w 1 to 10: ")))
   try:
     
    
     if (i ==a):
        print("you win : yeppi \nyou Done in",j,"chance \nyour Percenteg is ", (((100*(10-j))/10))+10, "%") 
        break
     elif j>=4:
        print("you lost your all terms \nsorry you are elemineted from game, well try \nThe winning guess number is:",a)
        break
     else:
        print("try again") 
   except:
      if j<5:
         print("Please Enter an number value:\nIF you enter non number value you get only 4 chance to enter an number value")
          