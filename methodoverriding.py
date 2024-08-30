class ap:
    def __init__(self,mul):
        self.mul=mul
    def app(self):
        return self.mul*self.mul
class plv(ap):
    def __init__(self,hight):
        self.hight=hight
        super().__init__(hight)
o=plv(12)
print(o.app())
# print(o)
