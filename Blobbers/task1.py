# Braxton Francom
# CS1400 - LW2
# Assignment 8

import turtle

class Face:
    def __init__(self):
        self.__smile = True
        self.__happy = True
        self.__darkEyes = True

    turtle.speed(0)

    def draw_face(self):
        turtle.clear()
        self.__drawHead()
        self.__drawEyes()
        self.__drawMouth()

    def __drawHead(self):
        turtle.penup()
        turtle.goto(0,-100)
        if self.__happy == True:
            turtle.fillcolor("yellow")
        else:
            turtle.fillcolor("red")
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(100)
        turtle.end_fill()

    def __drawEyes(self):
        turtle.penup()
        turtle.goto(-20,40)
        turtle.pendown()

        if self.__darkEyes == True:
            turtle.fillcolor("black")
        else:
            turtle.fillcolor("blue")

        turtle.begin_fill()
        turtle.circle(10)
        turtle.penup()
        turtle.goto(20, 40)
        turtle.pendown()
        turtle.circle(10)
        turtle.end_fill()

    def __drawMouth(self):
        turtle.penup()
        turtle.goto(-35,-30)
        turtle.setheading(325)
        turtle.pendown()
        turtle.pensize(8)

        if self.__smile == True:
            turtle.circle(60, 70)
        else:
            turtle.penup()
            turtle.goto(35,-30)
            turtle.pendown()
            turtle.setheading(145)
            turtle.circle(60, 70)
        turtle.setheading(0)
        turtle.pensize(1)

    def isSmile(self):
            return self.__smile

    def isHappy(self):
            return self.__happy

    def isDarkEyes(self):
            return self.__darkEyes

    def changeMouth(self):
        if self.__smile == False:
            self.__smile = True
            self.draw_face()
        else:
            self.__smile = False
            self.draw_face()
    def changeEmotion(self):
        if self.__happy == False:
            self.__happy = True
            self.draw_face()
        else:
            self.__happy = False
            self.draw_face()

    def changeEyes(self):
        if self.__darkEyes == False:
            self.__darkEyes = True
            self.draw_face()
        else:
            self.__darkEyes = False
            self.draw_face()


def main():
    face = Face()
    face.draw_face()

    done = False

    while not done:
        print("Change My Face")
        mouth = "frown" if face.isSmile() == True else "smile"
        emotion = "angry" if face.isHappy() == True else "happy"
        eyes = "blue" if face.isDarkEyes() == True else "black"
        print("1) Make me", mouth)
        print("2) Make me", emotion)
        print("3) Make my eyes", eyes)
        print("0) Quit")

        menu = eval(input("Enter a selection: "))

        if menu == 1:
            face.changeMouth()
        elif menu == 2:
            face.changeEmotion()
        elif menu == 3:
            face.changeEyes()
        else:
            break

    print("Thanks for Playing")

    turtle.hideturtle()
    turtle.done()


main()