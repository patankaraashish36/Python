class hello:
    def __init__(self):
        self.name="hello"
    def __del__(self):
        self.name
        print("deleted")
    def ok(self):
        return self.name
    
obj=hello()
# del obj
# o =obj.ok()  Object  has been deleted 
# print(o)   not print show error 