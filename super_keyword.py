#  super() keyword is use to call the parent class method in the child class.


class Boy:
    def __init__(self,name,age,village):
        self.name=name
        self.age=age
        self.village=village

    def data(self):
        return self.name,self.age,self.village
    
class Student(Boy):
    def __init__(self,name,age,village,sub,branch):
        self.sub=sub
        self.branch=branch
        super().__init__(name,age,village)

    def aashish(self,):
        return  self.name,self.age,self.village,self.sub,self.branch

Aashish=Student('Aashish Patankar',21,'Yenkheda','Python','CSE')

by=Boy('Aashish Patankar',21,'Yenkheda')

# Aashish.aashish()
print(Student.aashish(Aashish))
# print(Student.data(by))
print(by.data())