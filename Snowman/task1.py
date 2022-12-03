# Braxton Francom
# CS1400 - LW2
# Assignment 2

import turtle
turtle.speed(0)
turtle.showturtle()
turtle.hideturtle()

# snowman base circle
turtle.setheading(210)
turtle.circle(150, 300)

# snowman middle circle
turtle.penup()
turtle.setheading(210)
turtle.goto(15, 198)
turtle.pendown()
turtle.circle(120, 300)

# snowman head
turtle.penup()
turtle.goto(119,342)
turtle.pendown()
turtle.circle(90)

# snowman left eye
turtle.penup()
turtle.goto(45, 315)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.color("black")
turtle.end_fill()

# snowman right eye
turtle.penup()
turtle.goto(110, 315)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.color("black")
turtle.end_fill()

# snowman mouth
turtle.penup()
turtle.goto(60, 230)
turtle.pendown()
turtle.width(10)
turtle.setheading(340)
turtle.circle(40, 80)

# snowman top button
turtle.penup()
turtle.goto(85, 140)
turtle.pendown()
turtle.width(1)
turtle.begin_fill()
turtle.fillcolor("Medium Blue")
turtle.circle(8)
turtle.end_fill()


# snowman middle button
turtle.penup()
turtle.goto(85,100)
turtle.pendown()
turtle.begin_fill()
turtle.circle(8)
turtle.end_fill()

# snowman bottom button
turtle.penup()
turtle.goto(85,60)
turtle.pendown()
turtle.begin_fill()
turtle.circle(8)
turtle.end_fill()

# snowman hat
turtle.penup()
turtle.goto(32,334)
turtle.pendown()
turtle.pencolor("lime")
turtle.begin_fill()
turtle.fillcolor("red")
turtle.setheading(0)
turtle.forward(200)
turtle.setheading(90)
turtle.forward(10)
turtle.setheading(180)
turtle.forward(100)
turtle.setheading(90)
turtle.circle(60, 180)
turtle.setheading(270)
turtle.forward(10)
turtle.setheading(0)
turtle.forward(20)
turtle.end_fill()

# snowman left arm
turtle.penup()
turtle.goto(0,150)
turtle.pendown()
turtle.width(12)
turtle.color("brown")
turtle.setheading(210)
turtle.forward(200)

# snowman left hand
turtle.penup()
turtle.goto(-153,66)
turtle.pendown()
turtle.setheading(165)
turtle.width(10)
turtle.forward(25)
turtle.penup()
turtle.goto(-151,63)
turtle.pendown()
turtle.setheading(270)
turtle.forward(25)

# snowman right arm
turtle.penup()
turtle.goto(140,150)
turtle.pendown()
turtle.setheading(45)
turtle.forward(200)

# snowman left hand
turtle.penup()
turtle.goto(270,275)
turtle.pendown()
turtle.setheading(350)
turtle.forward(20)
turtle.penup()
turtle.goto(265,279)
turtle.pendown()
turtle.setheading(90)
turtle.forward(20)


# Messing around (Stump)
turtle.penup()
turtle.goto(420, -200)
turtle.pendown()
turtle.pencolor("brown")
turtle.width(1)
turtle.fillcolor("brown")
turtle.begin_fill()
turtle.forward(80)
turtle.setheading(0)
turtle.forward(50)
turtle.setheading(270)
turtle.forward(80)
turtle.setheading(180)
turtle.forward(50)
turtle.end_fill()

# Messing around (Tree)
turtle.penup()
turtle.goto(310,-120)
turtle.pendown()
turtle.pencolor("Magenta")
turtle.fillcolor("Magenta")
turtle.begin_fill()
turtle.setheading(0)
turtle.forward(280)
turtle.setheading(140)
turtle.forward(120)
turtle.setheading(0)
turtle.forward(50)
turtle.setheading(140)
turtle.forward(100)
turtle.setheading(0)
turtle.forward(40)
turtle.setheading(140)
turtle.forward(80)

# downhill side
turtle.setheading(220)
turtle.forward(80)
turtle.setheading(0)
turtle.forward(40)
turtle.setheading(220)
turtle.forward(100)
turtle.setheading(0)
turtle.forward(50)
turtle.setheading(220)
turtle.forward(120)
turtle.end_fill()

turtle.done()