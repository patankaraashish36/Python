from cgi import print_arguments


class lvr:
    def __init__(self,name, name2):
        print("plv")
        self.name=name
        self.name2=name2
    def lvy(self):
        print(f"{self.name} {self.name2} plv") 
a=lvr("plv","ash")
a.lvy()
print("___________________________________\n")

#  program to add two numbers

class addnum:
    def __init__(self , n1, n2):
        self.n1=n2
        self.n2=n1
    def sum(self):
        print(f"The sum of {self.n1} and {self.n2} is =", self.n1 +self.n2)       
b=addnum(7,9)
b.sum()

print("___________________________________\n")

# Find The Element In List

class lists:
    def __init__(self):
        self.list1=[1,4,5,6,8,9]
        a= int(input("Enter the number you find in list :"))
        if a in self.list1:
             print(f"Your number is {a} and their index number is {self.list1.index(a)}")
        else :
              print("data is not available")


# constructor print the any value no need to crate object

class Constructor:
    def __init__(self) -> None:
        print("hello AP")

    def normalfunc(self):
        print('Hello PA')
c=Constructor()
c.normalfunc()

