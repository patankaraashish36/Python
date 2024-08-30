import turtle 
a=turtle.Screen()
a.bgcolor("green")
a.title("cube")
b=turtle.Turtle()
b.color("orange")
a=turtle.Screen()

for i in range(4):
    b.forward(100)
    b.left(90)

b.goto(50,50)
for i in  range(4):
        b.forward(100)
        b.left(90)
        

b.goto(150,50)
b.goto(100,0)

b.goto(100,100)
b.goto(150,150)

b.goto(50,150)
b.goto(0,100)
