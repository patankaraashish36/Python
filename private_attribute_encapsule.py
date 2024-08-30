class Person:
    def __init__(self)  -> None:
        self.__name = "Aashish"
        self.branch = "CSE"
    
    def details(self):
        print(self.__name, self.branch)

p = Person() 
p.__name = "Punit"      # This not change the value instead create new varible.
# p._Person__name = "Punit"  This change the Value.
p.branch = "ME"
p.details()
