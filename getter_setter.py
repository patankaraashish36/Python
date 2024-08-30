class Person:
    def __init__(self)  -> None:
        self.__name = "Aashish"
        self.branch = "CSE"
       
    def get_name(self):
        print(self.__name)

    def set_name(self, new_value):
        if type(new_value) == str:
            self.__name = new_value
        else:
            print("Kutte ki dum.")

    def details(self):
        print(self.__name, self.branch)

p = Person() 
p.get_name()
p.set_name("Golu")
p.get_name()