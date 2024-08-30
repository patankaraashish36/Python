class classmethod:
    a="Aashish Patankar"
    def __init__(self):
        print("hello",self.a)
    def show(self):
        print("hello",self.a)
        
    @classmethod
    def change_a(cls,p):
        cls.a=p

g=classmethod()
g.change_a("ap")
g.show()
# print(classmethod.a)

