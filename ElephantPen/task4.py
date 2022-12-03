# Braxton Francom
# CS1400 - LW2
# Assignment 6 - Task 4

# Import modules
from random import randint

# While loop to determine if the simulation should be ran again
while True:
    # Define variables
    atLeastOne = 0
    both = 0

    # Elephant pen selection and zookeeper pen selection
    for i in range(1, 100001):
        elephantOne = randint(1, 6)
        elephantTwo = randint(1, 6)
        zookeeper = randint(1, 6)

        # Indicates presence of one elephant in pen
        if zookeeper == elephantOne:
            atLeastOne += 1
        if zookeeper == elephantTwo:
            atLeastOne += 1

        # Indicates presence of both elephants in one pen
        if zookeeper == elephantOne and zookeeper == elephantTwo:
            both += 1
            atLeastOne -= 1

    # Calculate percentage of times the zookeeper finds one elephant in pen
    percentOfOneElephant = (atLeastOne / 100000) * 100
    print("There is an elephant in the pen " + format(percentOfOneElephant, ".2f") + "% of the time")

    # Calculate percentage of times the zookeeper finds both elephants in same pen when he finds an elephant in the pen
    percentOfBothElephants = ((both / atLeastOne) * 100)
    print("When there is one elephant in the pen, " + format(percentOfBothElephants, ".2f") + "% of the time, both elephants are in the pen")

    # Determine who was correct (Zookeeper estimated 1/3 of the time there was one elephant, and 1/6 of the time there was two)
    if percentOfOneElephant >= 31.33 and percentOfOneElephant <= 35.33 and percentOfBothElephants >= 14.66 and percentOfBothElephants <= 18.66:
        print("The zookeeper was correct")

    else:
        print("The custodian was correct")

    # Prompt user if they want to run the program again
    userInput = input("Run the simulation again? (yes or no): ")

    if userInput.upper() != str("YES"):
        print("See ya l8er skater!")
        break
