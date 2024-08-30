class addition :
     x=1
     y=0
     z=0
     sum=0
     def __init__(self,x,y,z,):
          self.x=x
          self.y=y
          self.z=z     
     
     def add(self):
         self.sum=self.x+self.y+self.z
     def display(self):
          print("the sum is", self.sum)
obj=addition(3,3,3)
obj.add()
obj.display()
