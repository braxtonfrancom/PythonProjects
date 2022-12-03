# Braxton Francom
# CS1400 - LW2
# Assignment ???

from reprogram2 import Blobber

def main():
    name = input("Enter your B's name: ")
    color = input("Enter your B's color: ")
    radius = eval(input("Enter your B's radius: "))
    height = eval(input("Enter your B's height: "))

    myBlobber = Blobber(name, color, radius, height)

    done = False

    while not done:
        print()
        print("Main Menu")
        print("\t(1) Display Name")
        print("\t(2) Change Name")
        print("\t(3) Display Color")
        print("\t(4) Change Color")
        print("\t(5) Feed Blobber")
        print("\t(6) Blobber Speak")
        print("\t(7) Exit")


        vitals, blobberOK = myBlobber.vitalsOK()
        print("Your B is at " + format(vitals, ".2%") + " happiness")
        if not blobberOK:
            print("Your B got hecka smoofed")
            break

        choice = eval(input("Make a choice bruh: "))
        print()



        vitals, blobberOK = myBlobber.vitalsOK()
        if not blobberOK:
            print("Your B is only at like " + format(vitals, ".2%") + " happiness")
            print("Your B smoofed bruski")
            break

        if choice == 1:
            displayName(myBlobber)
        elif choice == 2:
            changeName(myBlobber)
        elif choice == 3:
            displayName(myBlobber)
        elif choice == 4:
            changeColor(myBlobber)
        elif choice == 5:
            feedBlobber(myBlobber)
        elif choice == 6:
            blobberSpeak(myBlobber)
        elif choice == 7:
            done = True

    print("Thanks for shmooving with us today")


def displayName(blobber):
    print("Your B's name is " + blobber.getName())

def changeName(blobber):
    name = input("Enter B's new name: ")
    blobber.setName(name)
    displayName(blobber)

def displayColor(blobber):
    print("yeesh, my new color is " + blobber.getColor())

def changeColor(blobber):
    color = input("Enter ya\' new color: ")
    blobber.setColor(color)
    displayColor(blobber)

def blobberSpeak(blobber):
    print(blobber.blobberSpeak())

main()

