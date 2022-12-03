# Braxton Francom
# CS1400 - LW2
# Assignment ???

from time import time
from math import pi

class Blobber():
    def __init__(self, name, color, radius, height):
        self.__radius = float(radius)
        self.__name = str(name.capitalize())
        self.__color = str(color.lower())
        self.__height = float(height)
        self.__originalRadius = radius
        self.__currentRadius = self.__originalRadius
        self.__originalVolume = ((self.__radius ** 2) * pi * self.__height)
        self.__currentVolume = self.__originalVolume
        self.__baseTime = time()
        self.__isAlive = True



    def getName(self):
        return self.__name


    def getColor(self):
        return self.__color


    def setName(self, name):
        self.__name = name.captitalize()


    def setColor(self, color):
        self.__color = color.lower()

    def feedBlobber(self, food):
        self.__currentRadius = self.__currentRadius + food
        self.__currentVolume = ((self.__currentRadius ** 2) * pi * self.__height)
        return (self.__currentVolume / self.__originalVolume)

    def blobberSpeak(self):
        vitals = (self.__currentVolume / self.__originalVolume)
        return "Eyy there. I 是 " + self.getName() + " and I'm " + self.getColor() + ". " + "\n" + "My current happiness level is " + format(vitals, ".2%") + ". Grand."

    def vitalsOK(self):
        self.__currentRadius = self.__currentRadius - (((time() - self.__baseTime) * .002) * self.__originalRadius)
        self.__currentVolume = ((self.__currentRadius ** 2) * pi * self.__height)
        self.__baseTime = time()
        vitals = (self.__currentVolume / self.__originalVolume)

        if self.__currentVolume < self.__originalVolume - (self.__originalVolume * .1) or self.__currentVolume > self.__originalVolume + (self.__originalVolume * .1):
            self.__isAlive = False

        return vitals, self.__isAlive