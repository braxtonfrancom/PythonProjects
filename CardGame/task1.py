# Braxton Francom
# CS1400 - LW2
# Assignment 13

from deck import Deck
from card import Card
import time



def sumHandTotal(playerId, playerHands):
    playerTotal = 0
    for x in range(len(playerHands[playerId])):
        cardValue = playerHands[playerId][x].getCardValue()
        if cardValue > 10:
            cardValue = 10
        if cardValue == 1 and playerTotal <= 10:
            cardValue = 11

        playerTotal += cardValue

    return playerTotal

def main():

    # Check to see if player still has money to play
    # for i in range(numOfPlayers):
    #     for j in range(len(playerBalances)):
    #         if playerBalances[j] <= 0:
    #             numOfPlayers.pop([i])
    #         else:
    #             pass

    playerHands = []
    playerBalances = []
    playerBets = []
    deck = Deck()
    numOfPlayers = 0

    numOfPlayers = eval(input(("How many players? ")))
    while numOfPlayers > 5:
        print("\n" + "The maximum number of players allowed is 5...Please try again ")
        numOfPlayers = eval(input("\n" + "How many players? "))

    dealerPlayerId = numOfPlayers

    done = False

    # Initialize Balances
    for i in range(numOfPlayers):
        playerBalances.append(100)

    while not done:
        playerHands = []
        for i in range(numOfPlayers+1):
            playerHands.append([])

        # Need a fresh deck at the start of each round
        deck.shuffle()


        for i in range(numOfPlayers):
            bet = eval(input("\n" + "Player " + str(i+1) + ", how much money do you want to bet this round? "))
            if bet < playerBalances[i] and bet < 5:
                print("The minimum allowed bet is $5, or your remaining balance (if less than $5). Please try again: ")
                bet = eval(input("How much money do you want to bet this round? "))
            else:
                playerBets.append(bet)

        ######DEAL THE CARDS########
        print("\n")
        for j in range(2):
            for i in range(numOfPlayers+1):
                newCard = deck.draw()
                playerHands[i].append(newCard)
        print("Dealing Cards...")
        for i in range(4):
            print(".", end="")
            time.sleep(.25)
        print()
        # Display second dealer card
        print("Dealer 2nd Card: " + str(playerHands[dealerPlayerId][1]))
        print("\n")

        #####PLAYER TURN########
        for i in range(numOfPlayers):
            print("\n")
            while 1==1:
                print("Player " + str(i+1) + " Your hand is: " + str(playerHands[i]) + "----->>>TOTAL: " + str(sumHandTotal(i, playerHands)))

                playerMove = eval(input("Would you like to... " + "\n" + "1) Take another card? " + "\n" + "2) Hold "))

                if playerMove == 1:
                    playerHands[i].append(deck.draw())

                elif playerMove == 2:
                    break

                currentTotal = sumHandTotal(i, playerHands)

                if currentTotal == 21:
                    print("Right On")
                    break

                if currentTotal > 21:
                    print("Busted")
                    break

        #####DEALER TURN#######
        print("\n" + "The dealer's first card is " + str(playerHands[dealerPlayerId][0]))
        print("The dealer's second card is " + str(playerHands[dealerPlayerId][1]))
        dealerTotal = sumHandTotal(dealerPlayerId, playerHands)

        while dealerTotal < 17:
            for i in range(4):
                print(".", end="")
                time.sleep(.25)
            print()

            print("The dealer takes a card")
            playerHands[dealerPlayerId].append(deck.draw())
            dealerTotal = sumHandTotal(dealerPlayerId, playerHands)

        if dealerTotal >= 17 and dealerTotal <= 21:
            print("The dealer holds")
        elif dealerTotal > 21:
            print("The dealer busts")

        print("Dealer Total:" + str(dealerTotal))



        ####DETERMINE WINNERS OF ROUND###

        print("\n")

        dealerTotal = sumHandTotal(dealerPlayerId, playerHands)
        dealerBusted = dealerTotal > 21
        dealerDifference = 1000 if dealerBusted else 21 - dealerTotal
        for playerId in range(numOfPlayers):
            playerTotal = sumHandTotal(playerId, playerHands)
            playerBusted = playerTotal > 21
            playerDifference = 1000 if playerBusted else 21-playerTotal

            if playerBusted or dealerDifference < playerDifference:
                playerBalances[playerId] = playerBalances[playerId] - playerBets[playerId]
                print("Player " + str(playerId+1) + ", you lost and your new balance is at $" + str(playerBalances[playerId]))
            elif dealerBusted or playerDifference < dealerDifference:
                playerBalances[playerId] = playerBalances[playerId] + playerBets[playerId]
                print("Player " + str(playerId+1) + ", you won and your new balance is at $" + str(playerBalances[playerId]))
            elif dealerDifference == playerDifference:
                print("Player " + str(playerId+1) + ", you tied and your balance remains at $" + str(playerBalances[playerId]))


        ###ASK TO PLAY AGAIN
        response = eval(input("Would you like to play again? " + "\n" + "1) Yes " + "\n" + "2) No "))
        if response == 1:
            pass
        elif response == 2:
            break

    print("Thanks for playing!")


    print("\n" + "-----------------GAME RESULTS----------------")
    playerBalances.sort(reverse=True)
    for i in range(numOfPlayers):
        print("Player " + str(i+1) + ": You finished with a balance of $" + str(playerBalances[i]))

main()

