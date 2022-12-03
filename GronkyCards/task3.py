# Braxton Francom
# CS1400 - LW2
# Assignment 12

from modules.deck import Deck
from time import sleep
from modules.gronkyutil import convertCardToId
from modules.gronkyutil import TITLE, GANG

def main():
    print("Welcome to Gronky Cards\n")
    print("Shuffling Cards", end="")
    thinking()

    deck = Deck()
    playerHand = []

    cardCount = int(input("How many cards would you like?: "))

    for i in range(cardCount):
        print(playerHand) # Single line

    done = False
    while not done:
        print()
        print("Menu")
        print("\t(1) Display hand")
        print("\t(2) Sort by title")
        print("\t(3) Sort by gang")
        print("\t(4) Search for card")
        print("\t(5) Quit")
        choice = int(input("Choose an option: "))
        print()

        if choice == 1:
            displayHand(playerHand)
        elif choice == 2:
            sortTitle(title) # Single line   # Or do I call getTitle from card.py?
        elif choice == 3:
            sortGang() # Single line
        elif choice == 4:
            searchCard() # Single line
        #elif choice == 5:                                          ###FIGURE this one out!!
           # <Fill-In> # Not a function and not 'break'

def thinking():
    for i in range(5):
        print(".", end="")
        sleep(0.5)
    print()

def displayHand(hand):
    print() # Not a single line. The entire function body

# Add other functions you need below

def sortTitle(title):        #USING Insertion sort
    for i in range(1,len(TITLE)):
        currCard = TITLE[i]
        j = i -1
        while j >= 0 and TITLE[j] > currCard:
            TITLE[j + 1] = TITLE[j]
            j -= 1
        TITLE[j + 1] = currCard

    print("Selection sort by Title")
    thinking()

def sortGang():
    for i in range():
        pass

def searchCard(playerHand, key): #Binary Search
    playerHand.sort
    low = 0
    high = len(playerHand) - 1
    while high >= low:
        mid = (high + low) // 2
        if key == playerHand[mid]:
            return mid
        elif key < playerHand[mid]:
            high = mid -1
        else:
            low = mid + 1




main()
