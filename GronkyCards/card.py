# Braxton Francom
# CS1400 - LW2
# Assignment 12

from modules.gronkyutil import TITLE, GANG

class Card:
    def __init__(self, id):
        self.__id = id

    def getTitle(self):
        return TITLE[self.getTitle()] # Do not use a numeric literal

    def getGang(self):
        return GANG[self.getGang()] # Do not use a numeric literal

    def getID(self):
        return self.__id

    # Add two dunder methods below to meet assignment requirements

    def __mul__():
        pass

    def __add__():
        pass
