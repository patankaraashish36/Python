class Person:
    def __init__(self, name, gender)  -> None:
        self.name = name
        self.gender = gender
    
    def details(self):
        print(self.name, self.gender)

p1= Person("Aashish,", "M")

p1.details()  # Object access method (or instance method) from outside the class.
        
print(p1.name) # Object access attribute (or instance variable) value from outside the class.
print(p1.gender)

p1.name = "Sahil"  # Object Change attribute (or instance variable) Value from outside the class.
print(p1.name)

p1.branch = "CSE"   # Object create attribute (or instance variable) from outside the class.
print(p1.branch)