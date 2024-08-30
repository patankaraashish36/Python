class Complex:
    def __init__(self,x,j):
        self.x=x
        self.j=j
        # self.y=input("Enter")
        
    def cmpx(self):
        return f"{self.x}X + {self.j}"
    
    def __add__(self,y):
        return complex(self.x + y.x ,self.j + y.j)
    
obj=Complex(3,4)
print(obj.cmpx())

ob=Complex(7,5)
print(ob.cmpx())

add=obj+ob
print(add)
print(type(obj+ob))
 