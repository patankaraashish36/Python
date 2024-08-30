class Person:
    def __init__(self, name, gender)  -> None:
        self.name = name
        self.gender = gender

def details(person):
    print(id(p1))
    print(id(person))
    person.name = "Golu"
    print(person.name)
    print(f"Hyy my name is {person.name} and i am a {person.gender}")
    p2 = Person("Ram", "Male")
    return p2
p1 = Person("Aashish,", "Male") 
print(id(p1))
print(p1.name)
x = details(p1)
print(x.name)
print(x.gender)
print(p1.name)