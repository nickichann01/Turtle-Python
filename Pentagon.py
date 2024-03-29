#import turtle lib
import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the turtle's pen size
t.pensize(1)

# Move the turtle to the starting position for the Pentagon
t.penup()
t.goto(-50, 0)
t.pendown()

# Draw a circle moving Pentagon
t.color('blue', 'purple')
t.speed(0)

#600 is for 600 Pentagon
for i in range (600):
    if i % 5 == 0:
        t.lt(3)
    t.fd(200)
    t.lt(360/5)

# Hide the turtle and keep the window open
t.hideturtle()
turtle.done()
