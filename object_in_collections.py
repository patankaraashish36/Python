class Person:
    def __init__(self)  -> None:
        self.__name = "Aashish"
        self.branch = "CSE"
    
    def details(self):
        print(self.__name, self.branch)

p1 = Person()
p2 = Person() 
p3 = Person()  
p1.details()

print("----------------------------------")
l= [p1, p2, p3]
print(l[0].branch)

for i in l:
    print(i.branch)

print("----------------------------------")

d = {
    "p1":p1,
    "p2":p2,
    "p3":p3
}

for i in d:
    print(d[i].branch)