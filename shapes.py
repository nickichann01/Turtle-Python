import turtle

#Set the background color to Black
turtle.Screen().bgcolor("black")

ts = turtle.getscreen()

# Create a turtle object
t = turtle.Turtle()


# Triangle
t.begin_fill()
t.color("yellow")
t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.forward(200)
t.end_fill()
# (This will remove the fill color of triangle shape) t.undo()
# (This will remove the entire shape) t.clear()
# (This will remove the entire shape and all the t.goto() function will override) t.reset()

# Moving the position of the pen to draw the circle shape
t.penup()
t.goto(0, -100)
t.pendown()

# Circle
t.begin_fill()
t.color("red")
t.circle(100)
t.end_fill()

# Moving the position of the pen to draw the rectangle shape
t.penup()
t.goto(-40, -100)
t.pendown()

# Rectangle
t.begin_fill()
t.color("blue")
t.forward(250)
t.right(90)
t.forward(150)
t.right(90)
t.forward(250)
t.right(90)
t.forward(150)
t.right(90)
t.end_fill()

# Moving the position of the pen to draw the star shape
t.penup()
t.goto(-110, 180)
t.pendown()

# Star
t.begin_fill()
t.pencolor("white")
t.color("white")
t.forward(200)
t.right(144)
t.forward(200)
t.right(144)
t.forward(200)
t.right(144)
t.forward(200)
t.right(144)
t.forward(200)
t.right(144)
t.end_fill()


# Hide the turtle
t.hideturtle()

# Keep the window open
turtle.done()
