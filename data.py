class aayush:
    def __init__(self, mobile,name,age,profession,hight):
        self.mobile=mobile
        self.age=age
        self.profession=profession
        self.name=name
        self.hight=hight
    def data(self):
        return (self.mobile ,self.age,
        self.profession,
        self.name,
        self.hight)

class ashwin(aayush):
    def data(self):
        return (self.mobile ,
        self.age,
        self.profession,
        self.name,
        self.hight)
        
asw=aayush(830521,16,"yt","ashwin",5.78)
print(asw.data())
obj=ashwin(830521,16,"yt","aayush",5.78)
obj.data()
print(obj.data())