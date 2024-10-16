import turtle
t = turtle.Turtle()

# Draw the first circle
t.penup()
t.goto(-0, 0)
t.pendown()
t.circle(50)

# Draw the second circle
t.penup()
t.goto(30, 0)
t.pendown()
t.circle(50)

# Keep the window open
turtle.done()