import turtle

t = turtle.Turtle()
t.width(5)

def up():
    t.setheading(90)
    t.forward(50)

def down():
    t.setheading(270)
    t.forward(50)

def left():
    t.setheading(180)
    t.forward(50)

def right():
    t.setheading(0)
    t.forward(50)

def u():
    t.up()

def d():
    t.down()

def red():
    t.color("red")

def mag():
    t.color("magenta")

def yello():
    t.color("yellow")

def gre():
    t.color("green")

def bla():
    t.color("black")

def whi():
    t.color("white")

turtle.listen()

turtle.onkey(up, "Up")
turtle.onkey(down, "Down")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")

turtle.onkey(u, "u")
turtle.onkey(d, "d")

turtle.onkey(red, "r")
turtle.onkey(mag, "m")
turtle.onkey(yello, "y")
turtle.onkey(gre, "g")
turtle.onkey(bla, "b")
turtle.onkey(whi, "w")

turtle.mainloop()