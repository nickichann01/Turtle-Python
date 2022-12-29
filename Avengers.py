import turtle

turtle.Screen().bgcolor("black")

# Create a turtle object
t = turtle.Turtle()
t.penup()
t.pensize(10)
t.speed(10)


#Draw first circle
t.penup()
t.begin_fill()
t.setposition(0, -280)
t.color('red')
t.pencolor("white")
t.circle(300)
t.end_fill()
t.pendown()

#Draw second circle 
t.penup()
t.begin_fill()
t.setposition(0, -230)
t.color('black')
t.circle(250)
t.pensize(2)
t.end_fill()
t.pendown()

# Draw an A
t.penup()
t.setposition(30, -110)
t.begin_fill()
t.color("red")
t.pensize(10)
t.pencolor("black")
t.forward(23)
t.backward(123)
t.left(60)
t.backward(220)
t.right(60)
t.backward(100)
t.right(117)
t.backward(710)
t.right(63)
t.backward(110)
t.right(90)
t.backward(510)
t.right(90)
t.backward(100)
t.right(90)
t.backward(70)
t.end_fill()
t.pendown()

# Draw triangle inside the A
t.setposition(53, -40)
t.pensize(10)
t.pendown()
t.begin_fill()
t.color("black")
t.pencolor("black")
t.right(90)
t.forward(100)
t.right(115)
t.forward(250)
t.right(157)
t.forward(227)
t.end_fill()

# Draw an arrow
t.backward(80)
t.left(42)
t.forward(147)
t.right(83)
t.forward(140)

t.hideturtle()
turtle.done()