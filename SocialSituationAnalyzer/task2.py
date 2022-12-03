# Braxton Francom
# CS1400 - LW2
# Assignment 5 - Task 2

import math

# Print welcome statement
print("Welcome to the Social Situation Analyzer System")

# Print Person One
print("Person One")

# Prompt person one for name
personOne = input("   Enter your name: ")

# Prompt person one for position
positionOne = x1, y1 = eval(input("   Enter your position (x, y): "))

# Prompt person one for personal space radius
radiusOne = eval(input("   Enter your personal space radius: "))

# New line
print("\n")

# Print Person Two
print("Person Two")

# Prompt person two for name
personTwo = input("   Enter your name: ")

# Prompt person two for position
x2, y2 = eval(input("   Enter your position (x, y): "))

# Prompt person two for personal space radius
radiusTwo = eval(input("   Enter your personal space radius: "))

# Begin message
msg = ""

# New line
msg += "\n"

# Calculate the distance between the two points
distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Label Social situation results
msg += "Social Situation Analysis Results" + "\n"

# Label Person Test
msg += "\t" + "Person Test: "

# Person Test- determines if individual has someone in their own personal space
if distance <= radiusOne and distance <= radiusTwo:
    msg += str(personOne) + " and " + str(personTwo) + " are in each other's personal space"
elif distance <= radiusTwo:
    msg += str(personOne) + " is in " + str(personTwo) + "'s personal space"
elif distance <= radiusOne:
    msg += str(personTwo) + " is in " + str(personOne) + "'s personal space"
else:
    msg += "Neither " + str(personOne) + " nor " + str(personTwo) + " is in the other's personal space"

# New line
msg += "\n"

# Label Space Test
msg += "\t" + "Space Test: "

# Space Test- determines the relation of the personal spaces of each person
if distance <= radiusOne - radiusTwo and radiusOne > radiusTwo:
    msg += str(personTwo) + "'s personal space is entirely inside " + str(personOne) + "'s personal space"
elif distance <= radiusTwo - radiusOne and radiusOne < radiusTwo:
    msg+= str(personOne) + "'s personal space is entirely inside " + str(personTwo) + "'s personal space"
elif distance <= abs(radiusOne + radiusTwo):
    msg += str(personOne) + " and " + str(personTwo) + "'s spaces overlap"
else: #distance >= abs(radiusOne + radiusTwo):
    msg += str(personOne) + " and " + str(personTwo) + "'s spaces do not overlap"

print(msg)