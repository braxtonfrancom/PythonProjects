# Braxton Francom
# CS1400 - LW2
# Assignment 11

from math import pi
from random import shuffle
from random import randint
import time

class Orbian:
    # DO NOT MODIFY THE CONSTRUCTOR
    def __init__(self, name, headRadius, bodyRadius, bodyHeight):
        # NOTE: These are constants
        self.__HEAD_RADIUS = headRadius
        self.__BODY_RADIUS = bodyRadius
        self.__BODY_HEIGHT = bodyHeight
        self.__NAME = name
        self.__BIRTH_TIME = time.time()

        # This is the only variable
        self.__adult = False

    def __getHeadVolume(self):
        return 4 / 3 * pi * self.__getHeadRadius() ** 3

    def __getBodyVolume(self):
        return pi * self.__getBodyRadius() ** 2 * self.__getBodyHeight()

    def __ageCheck(self):
        # Become an adult at 2
        if self.getAge() >= 2:
            self.__adult = True

    ####### ADD OTHER REQUIRED METHODS BELOW. SEE THE ASSIGNMENT DESCRIPTION AND OTHER STARTER CODE FOR INSIGHT ######

    def getName(self):
        return self.__NAME

    def __getHeadRadius(self):
        self.__ageCheck()
        if self.__adult:
            return (self.__HEAD_RADIUS * 2)
        else:
            return self.__HEAD_RADIUS

    def __getBodyRadius(self):
        self.__ageCheck()
        if self.__adult:
            return (self.__BODY_RADIUS * 2)
        else:
            return self.__BODY_RADIUS

    def __getBodyHeight(self):
        self.__ageCheck()
        if self.__adult:
            return (self.__BODY_HEIGHT * 4)
        else:
            return self.__BODY_HEIGHT

    def getVolume(self):
        volume = int(self.__getBodyVolume() + self.__getHeadVolume())
        return volume

    def getAge(self):
        return int(((time.time() - self.__BIRTH_TIME) // 5))

    def __gt__(self, other):
        if self.getVolume() > other.getVolume():
            return True
        else:
            return False

    def __eq__(self, other):
        if self.getVolume() == other.getVolume():
            return True
        else:
            return False

    def __len__(self):
        return (self.__BODY_HEIGHT + (self.__HEAD_RADIUS * 2))

    def __add__(self, other):
        newList = list(self.getName() + other.getName())
        length = int(len(self.getName()) + len(other.getName()))
        shuffle(newList)
        newName = (("".join(newList).capitalize())[:length // 2])
        newHeadRadius = ((self.__HEAD_RADIUS + other.__HEAD_RADIUS) / 4)
        newBodyRadius = ((self.__BODY_RADIUS + other.__BODY_RADIUS) / 4)
        newHeight = ((self.__BODY_HEIGHT + other.__BODY_HEIGHT) / 8)
        return Orbian(newName, newHeadRadius, newBodyRadius, newHeight)