# Braxton Francom
# CS1400 - LW2
# Assignment 5 - Task 1

# Import random module
import random

# Print intro to game
print("Welcome to the Guessing Game")

# Print explanation of random generator's choice
print("The Computer has picked a number from 1-10. Try to match it.")

# Prompt user for a number from 1-10
userNum = eval(input("What number do you choose (1-10): "))

# Generate computer number
systemNum = random.randint(1, 10)

# Begin msg
msg = ""

# Display the users number and the computer generated number
msg += "You picked " + str(userNum) + ", and the actual number was " + str(systemNum)

# New line
msg += "\n"

# Use if-else-if statement to account for different outcomes.
if abs(userNum - systemNum) == 0:
    msg += "Honored to play with you, Master."

elif abs(userNum - systemNum) == 1:
    msg += "You are a worthy opponent, Knight."

elif abs(userNum - systemNum) == 2:
    msg += "You have much to learn, Padawan."

elif abs(userNum - systemNum) <= 3:
    msg += "Youngling, your time will come."

else:
    msg += "Keep working hard in the Service Corps."

print(msg)