# Braxton Francom
# CS1400 - LW2
# Assignment 4

import math
from math import tan
from math import pi

# Prompt user for length of sides
lengthOfSides = eval(input("Enter the length of sides: "))

# Prompt user for number of sides
numberOfSides = eval(input("Enter the number of sides: "))

# Calculate area of polygon
Area = (numberOfSides * math.pow(lengthOfSides, 2)) / (4 * (tan(pi / numberOfSides)))

# Display the area of the polygon
print("The area of the polygon is: " + str(round(Area, 5)))