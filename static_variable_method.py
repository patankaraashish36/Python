class Person:
    # Static or Class variable.
    clg = "SIRT"

    def __init__(self)  -> None:
        # Instance or object variable
        self.name = "Aashish"
        self.branch = "CSE"


    # Static or Class method.
    @staticmethod
    def cls_method():
        print(Person.clg)

    # Instance or object Method
    def details(self):
        print(self.name, self.branch)

print("Static Variable :", Person.clg)

Person.cls_method()