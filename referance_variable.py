class Person:
    def __init__(self, name, gender)  -> None:
        self.name = name
        self.gender = gender
    
    def details(self):
        print(self.name, self.gender)

Person("Aashish,", "M")  # Object Creation

p1 = Person("Aashish", " M")  # Referance Variable creation (p1 is a Referance Variable Not a Object).
p2 = Person("Golu", " M")
p1.details()

print("p1 obj =", p1.name)
q = p1
print("q obj =",q.name)

print("p1 obj =",id(p1))
print("q obj =",id(q))