lst=[[0,9],6,1,2,3,4,5]
print(lst[0][1]) # 0
print(lst[:-2]) 
print(lst[:-2][1]) # 2
print(lst[::-2])
print(lst[::-2][0]) #reverse the list 5
print(lst[::-3]) #reverse the list with skip the every second element
print(lst[len(lst)//2:]) # print the list length and slice them
print(lst[5//2:]) # like as ^ here
print(lst[2:]) # like as ^ here

class hello():
    def __init__(self):
        self.__name="hello world"
    def h(self):
        return self.__name
    
obj=hello()
x=obj.h()
print(obj._hello__name)

