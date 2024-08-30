a=int(input("enter number:"))
for i in range(6):
    for j in range(i):
        print(a,end="")
    print()
    # 
# file=open("fhandling.text","w") #create a file 
# file.write("this program is file hanadling ")# write a file when you created
# file.close()#close your file if no operation perform
# file.write("hyy")#show error
# file=open("fhandling.text","w") #open your created file
# file.write("hello")
# file.write("helo")
# 
# file.close()
# file=open("fhandling.text","w") 
# file.write("helo")
# file.close()
# file=open("fhandling.text","r") 
# print(file.read())      #   reading the file 

f=open("hello.py","w")
f.write("hello world")
f.close()
f=open("hello.py","r")
# print(f.read())
# for i in f:
    # print(i + "hyy") #print the file writed


while True :
    data=f.read()
    if not data :
     break
    print(data,"while")

# read the binary file like pdf
# rd to read and wd to write and some as above

with open("hello.py") as f:
    for line in f:
       print(line,f.read(),"with ap")
  