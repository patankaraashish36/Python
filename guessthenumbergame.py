# MATCHE NUMBER AND SCORE
from colorama import Fore
import random
a=random.randrange(10)

 #IF YOU WANT TO CHECK A RANDOM NUMBER PLEASE UNCOMMENT

# print(a)
for j in range(11):
   # for k in range(100):

     
    try:
     i=int((input(Fore.LIGHTMAGENTA_EX+"Enter a number b/w 0 to 10: ")))
    
     if (i ==a):
        print(Fore.BLUE+"you win: yeppi")
        print(Fore.GREEN +"you Done in",j+1,"chance")
        print(Fore.YELLOW +"your Percenteg", (10+((100*(10-(j+1)))/10)),"%")
        break
     elif (j+1)>=4:
        print(Fore.RED +"you lost your all terms")
        print(Fore.CYAN+"sorry you are elemineted from game, well try")
        print("The winning guess number:",a)
        break
     else:
        print(Fore.LIGHTRED_EX +"try again") 
    except:
      
       print(Fore.LIGHTCYAN_EX+ "Please Enter an number value:\nIF you enter non number value you get only 9 chance to enter an integer value")
          