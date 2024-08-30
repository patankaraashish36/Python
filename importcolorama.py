import turtle

# Set up the turtle
t = turtle.Turtle()
t.shape("arrow")
t.color("red", "pink")
t.speed(5)
t.penup()
t.goto(-20 , -150)
t.pendown()

# Draw the heart shape
t.begin_fill()
t.left(45)
t.forward(200)
t.circle(80, 180)
t.right(90)
t.circle(80, 180)
t.forward(200)
t.end_fill()

# Write "Love" in the center of the heart
t.penup()
t.goto(0, 0)
t.color("black")
t.write("PA", align="center", font=("italic", 15, "bold"))

turtle.done()
