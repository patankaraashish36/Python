class hello:
    def __init__(self,name, rollno,age,marks,empcode):
        self.name=name
        self.rollno=rollno
        self.age=age
        self.marks=marks
        self.empcode=empcode
    def details(self):
        print(self.name)
        print(self.rollno)
        print(self.age)
        print(self.marks)
        print(self.empcode)
# hello("a",5,6,7,8)    
# a=hello("aashish","D06",20,80,404)
# print(a)
# a.details()

def hello(byy):
  def hyy():
    print("hyy i am aashish")
    byy()
    print("hello i am aashish ")
    print("i")
  return hyy
  
@hello
def byy():
  print("i ")

# hello(byy())
# same work both 
byy()


def myfunc(a):
  a = a + 2
  a = a * 2
  return a

print(myfunc(2))