# Braxton Francom
# CS1400 - LW2
# Assignment 12

from modules.gronkyutil import TITLE, GANG
from modules.card import Card
from random import shuffle

class Deck:
    def __init__(self):
        self.shuffle()

    def shuffle(self):
        self.__deck = []
        totalCards = self.__deck # Do not use a numeric literal

        for i in range(totalCards):
            <Fill-In> # Single line of code

        shuffle(self.__deck)

    def draw(self):
        <Fill-In> # Single line of code