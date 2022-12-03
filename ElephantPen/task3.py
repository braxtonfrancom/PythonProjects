# Braxton Francom
# CS1400 - LW2
# Assignment 6 - Task 3

# import modules
from time import time
from random import randint, seed

# Assign variables
iterator = 0
beginTime = time()
count = 0

# Find fluky numbers and display
for num in range(1, 10001):
    total = 0
    for i in range(1, (num // 2 + 1)):
        iterator += 1
        if num % i == 0:
            seed(i)
            total += randint(1, num)
            if total > num:
                break

    if total == num:
        count += 1
        print("Fluky Number: " + str(num))
    if count == 7:
        break

# Display total time and total iterations
print(format(f"Total Time: {time()-beginTime}", ".16s") + " seconds")
print(format(f"Total Loops: {iterator}"))


