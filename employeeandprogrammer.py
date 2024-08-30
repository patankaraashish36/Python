class Employee:
    def __init__(self,name,ids,salary):
        self.name=name
        self.ids=ids
        self.salary=salary
    def Details(self):
        print(self.name,self.ids,self.salary)


class Programmer(Employee):
    def info(self):
       print(self.name,self.ids,self.salary)
       print("The language is pyhton")

E=Employee("Aashish",132,70000)
E.Details()

print("___________________________________\n")


p=Programmer("pa",122,70000)
p.info()