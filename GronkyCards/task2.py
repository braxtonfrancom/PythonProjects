# Braxton Francom
# CS1400 - LW2
# Assignment 12

def main():
    done = False

    while not done:

        number = eval(input("Enter a number yo: "))
        count = 0
        list1 = []
        if type(number) == int:
            list1 = [number]
            count += 1
            print(list1)
            print(count)
        elif number == "":
            print("The number of values you entered: " + str(count))
            print("The biggest number you entered was: ")
            print("The smallest number you entered was: " + min(list1))
            print("The sum of all the numbers you entered is: ")
            print("The average value of the numbers you entered is: ")


main()