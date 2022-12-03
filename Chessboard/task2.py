# Braxton Francom
# CS1400 - LW2
# Assignment 7

from chessboard import drawChessboard

# Call main function
def main():

    #Prompt user input
    startX, startY = eval(input("Enter starting location (x,y): "))

    height = input("Enter chessboard height: ")

    width = input("Enter chessboard width: ")

# Call drawChessboard function
    if width == "" and height == "":
        drawChessboard(startX, startY)
    elif height == "":
        drawChessboard(startX, startY, width=eval(width))
    elif width == "":
        drawChessboard(startX, startY, height=eval(height))
    else:
        drawChessboard(startX, startY, eval(width), eval(height))

main()