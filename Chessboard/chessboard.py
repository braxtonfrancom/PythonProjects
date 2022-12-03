# Braxton Francom
# CS1400 - LW2
# Assignment 7

import turtle
turtle.speed(0)

def drawChessboard(startX, startY, width=250, height=250):
    turtle.penup()
    turtle.goto(startX, startY)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(width)
    turtle.setheading(90)
    turtle.forward(height)
    turtle.setheading(180)
    turtle.forward(width)
    turtle.setheading(270)
    turtle.forward(height)
    turtle.penup()
    drawAllRectangles(startX, startY, width, height)
    turtle.done()



def drawAllRectangles(startX, startY, width, height):
    currentY = startY

    for i in range(0, 4):
        currentX = startX
        turtle.setheading(0)
        turtle.goto(currentX, currentY)

        for j in range(0, 4):
            drawRectangle(currentX, currentY, width, height)
            turtle.goto(currentX, currentY)
            turtle.setheading(0)
            currentX += width / 4

        currentY += height / 4

    currentY = startY + height / 8

    for i in range(0, 4):
        currentX = startX + width / 8
        turtle.setheading(0)
        turtle.goto(currentX, currentY)

        # up a row
        for j in range(0, 4):
            drawRectangle(currentX, currentY, width, height)
            turtle.goto(currentX, currentY)
            turtle.setheading(0)
            currentX += width / 4

        currentY += height / 4


def drawRectangle(startX, startY, width, height):
    turtle.penup()
    turtle.goto(startX, startY)
    turtle.pendown()
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.forward(width/8)
    turtle.setheading(90)
    turtle.forward(height/8)
    turtle.setheading(180)
    turtle.forward(width/8)
    turtle.setheading(270)
    turtle.forward(height/8)
    turtle.end_fill()
    turtle.penup()

