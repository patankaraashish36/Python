from random import randrange
l1=["Aashish patankar","plv","A","B","C","D"]
a=randrange(6)
b=l1[a]
print(b)
for i in range(4):
    c=input(" : ")
    if b == c:
        print("True")
    else:
        print("False")