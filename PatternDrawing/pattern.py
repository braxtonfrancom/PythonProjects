# Braxton Francom
# CS1400 - LW2
# Assignment 8

import turtle
import random

def reset():
    turtle.reset()
    turtle.speed(100)
    turtle.hideturtle()

def setup():
    turtle.speed(100)
    turtle.setup(1000, 800)

def drawRectangle(centerX, centerY, offset, width, height, count, rotation):
    turtle.penup()
    turtle.goto(centerX, centerY)
    turtle.forward(offset)
    turtle.pendown()
    setRandomColor()
    turtle.setheading(rotation)
    turtle.forward(width)
    turtle.setheading(rotation + 90)
    turtle.forward(height)
    turtle.setheading(rotation + 180)
    turtle.forward(width)
    turtle.setheading(rotation + 270)
    turtle.forward(height)

def drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation):
    for i in range (0, count):
        rotation += 360 / count
        turtle.penup()
        turtle.goto(centerX, centerY)
        turtle.forward(offset)
        turtle.setheading(rotation)
        turtle.pendown()
        drawRectangle(centerX, centerY, offset, width, height, count, rotation)
        turtle.penup()                                                                          ###How do get it to rotate each time it draws a new one?
        turtle.goto(centerX, centerY)
        turtle.setheading(360 / count)

def drawCirclePattern(centerX, centerY, offset, radius, count):
    rotation = 0
    for i in range(0, count):
        rotation += 360/count
        turtle.penup()
        turtle.goto(centerX, centerY)
        turtle.forward(offset)
        turtle.right(90)
        turtle.pendown()
        setRandomColor()
        turtle.circle(radius)
        turtle.penup()
        turtle.goto(centerX, centerY)
        turtle.setheading(rotation)

def drawSuperPattern(num=3):

    for i in range(0, num):
        centerX = random.randint(-500, 500)
        centerY = random.randint(-300, 300)
        offset = random.randint(-200, 200)
        width = random.randint(0, 200)
        height = random.randint(0, 200)
        count = random.randint(0, 200)
        rotation = random.randint(0, 360)
        radius = random.randint(0, 200)

        a = random.randint(0,2)
        if a == 1:
            drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation)

        else:
            drawCirclePattern(centerX, centerY, offset, radius, count)

def setRandomColor():
    a = random.randint(0,4)
    if a == 1:
        turtle.pencolor("blue")
    elif a == 2:
        turtle.pencolor("red")
    elif a == 3:
        turtle.pencolor("orange")
    else:
        turtle.pencolor("green")

def done():
    turtle.done()

