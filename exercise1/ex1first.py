#script in part from https://codereview.stackexchange.com/questions/239990/basic-blackjack-game-in-python
import random
import time

deck = []
firstDraw = 0
usedCards = []
playerHand = []
playerHandValue = 0
dealtCard1 = ''
dealtCard1Number = 0
dealtCard2 = ''
dealtCard2Number = 0
dealerHand = []
dealerHandValue = 0



def dealHand():

    global deck
    global playerHand
    global playerHandValue
    global dealerHand
    global dealerHandValue
    global firstDraw
    firstDraw = 0
    # The starting deck is created #
    deck = ['2sp', '3sp', '4sp', '5sp', '6sp', '7sp', '8sp', '9sp', '10sp', 'Jsp', 'Qsp', 'Ksp', 'Asp', '2cl', '3cl', '4cl', '5cl', '6cl', '7cl', '8cl', '9cl', '10cl', 'Jcl', 'Qcl', 'Kcl', 'Acl', '2he', '3he', '4he', '5he', '6he', '7he', '8he', '9he', '10he', 'Jhe', 'Qhe', 'Khe', 'Ahe', '2di', '3di', '4di', '5di', '6di', '7di', '8di', '9di', '10di', 'Jdi', 'Qdi', 'Kdi', 'Asp']

    playerHand = []
    playerHandValue = 0
    dealerHand = []
    dealerHandValue = 0

# Two cards are dealt to the player #
    dealtCard1Number = random.randint(0, len(deck)-1)
    playerHand.append(deck[dealtCard1Number])
    del deck[dealtCard1Number]

    dealtCard2Number = random.randint(0, len(deck)-1)
    playerHand.append(deck[dealtCard2Number])
    del deck[dealtCard2Number]

# Two cards are dealt to the dealer #
    dealerCard1Number = random.randint(0, len(deck)-1)
    dealerCard1 = deck[dealerCard1Number]
    dealerHand.append(dealerCard1)
    del deck[dealerCard1Number]

    dealerCard2Number = random.randint(0, len(deck)-1)
    dealerCard2 = deck[dealerCard2Number]
    dealerHand.append(dealerCard2)
    del deck[dealerCard2Number]



# The player's starting hand is revealed to the player #
    print('\n' + 'Your current hand is ' + str(playerHand) + '\n')
    time.sleep(1)
    findHandValue()

def findHandValue():
    global playerHand
    global playerHandValue
# Resets the player's hand value to 0 for new deals #
    playerHandValue = 0
# The value of the player's cards is determined #
    if '2sp' in playerHand:
        playerHandValue = playerHandValue + 2
    if '3sp' in playerHand:
        playerHandValue = playerHandValue + 3
    if '4sp' in playerHand:
        playerHandValue = playerHandValue + 4
    if '5sp' in playerHand:
        playerHandValue = playerHandValue + 5
    if '6sp' in playerHand:
        playerHandValue = playerHandValue + 6
    if '7sp' in playerHand:
        playerHandValue = playerHandValue + 7
    if '8sp' in playerHand:
        playerHandValue = playerHandValue + 8
    if '9sp' in playerHand:
        playerHandValue = playerHandValue + 9
    if '10sp' in playerHand:
        playerHandValue = playerHandValue + 10
    if 'Jsp' in playerHand:
        playerHandValue = playerHandValue + 10
    if 'Qsp' in playerHand:
        playerHandValue = playerHandValue + 10
    if 'Ksp' in playerHand:
        playerHandValue = playerHandValue + 10
    if 'Asp' in playerHand:
        playerHandValue = playerHandValue + 11
    if '2cl' in playerHand:
        playerHandValue = playerHandValue + 2
    if '3cl' in playerHand:
        playerHandValue = playerHandValue + 3
    if '4cl' in playerHand:
        playerHandValue = playerHandValue + 4
    if '5cl' in playerHand:
        playerHandValue = playerHandValue + 5
    if '6cl' in playerHand:
        playerHandValue = playerHandValue + 6
    if '7cl' in playerHand:
        playerHandValue = playerHandValue + 7
    if '8cl' in playerHand:
        playerHandValue = playerHandValue + 8
    if '9cl' in playerHand:
        playerHandValue = playerHandValue + 9
    if '10cl' in playerHand:
        playerHandValue = playerHandValue + 10
    if 'Jcl' in playerHand:
        playerHandValue = playerHandValue + 10
    if 'Qcl' in playerHand:
        playerHandValue = playerHandValue + 10
    if 'Kcl' in playerHand:
        playerHandValue = playerHandValue + 10
    if 'Acl' in playerHand:
        playerHandValue = playerHandValue + 11
    if '2he' in playerHand:
        playerHandValue = playerHandValue + 2
    if '3he' in playerHand:
        playerHandValue = playerHandValue + 3
    if '4he' in playerHand:
        playerHandValue = playerHandValue + 4
    if '5he' in playerHand:
        playerHandValue = playerHandValue + 5
    if '6he' in playerHand:
        playerHandValue = playerHandValue + 6
    if '7he' in playerHand:
        playerHandValue = playerHandValue + 7
    if '8he' in playerHand:
        playerHandValue = playerHandValue + 8
    if '9he' in playerHand:
        playerHandValue = playerHandValue + 9
    if '10he' in playerHand:
        playerHandValue = playerHandValue + 10
    if 'Jhe' in playerHand:
        playerHandValue = playerHandValue + 10
    if 'Qhe' in playerHand:
        playerHandValue = playerHandValue + 10
    if 'Khe' in playerHand:
        playerHandValue = playerHandValue + 10
    if 'Ahe' in playerHand:
        playerHandValue = playerHandValue + 11
    if '2di' in playerHand:
        playerHandValue = playerHandValue + 2
    if '3di' in playerHand:
        playerHandValue = playerHandValue + 3
    if '4di' in playerHand:
        playerHandValue = playerHandValue + 4
    if '5di' in playerHand:
        playerHandValue = playerHandValue + 5
    if '6di' in playerHand:
        playerHandValue = playerHandValue + 6
    if '7di' in playerHand:
        playerHandValue = playerHandValue + 7
    if '8di' in playerHand:
        playerHandValue = playerHandValue + 8
    if '9di' in playerHand:
        playerHandValue = playerHandValue + 9
    if '10di' in playerHand:
        playerHandValue = playerHandValue + 10
    if 'Jdi' in playerHand:
        playerHandValue = playerHandValue + 10
    if 'Qdi' in playerHand:
        playerHandValue = playerHandValue + 10
    if 'Kdi' in playerHand:
        playerHandValue = playerHandValue + 10
    if 'Adi' in playerHand:
        playerHandValue = playerHandValue + 11
# Allows Aces to convert from 11 points to 1 point if the hand value is over 21 #
    if playerHandValue > 21:
        if 'Asp' in playerHand:
            playerHandValue = playerHandValue - 10
        if playerHandValue > 21:
            if 'Acl' in playerHand:
               playerHandValue = playerHandValue -10
            if playerHandValue > 21:
                if 'Adi' in playerHand:
                   playerHandValue = playerHandValue -10
                if playerHandValue > 21:
                    if 'Ahe' in playerHand:
                         playerHandValue = playerHandValue -10
# Displays the player's hand value to the player #
    print("Player hand value = " + str(playerHandValue) + '\n')
    hitOrStay()


def hitOrStay():
    global dealtCard1
    global firstDraw
# The dealer's first card is revealed to the player #
    if firstDraw == 0:
        print('The dealer draws 2 cards and reveals ' + str(dealerHand[0]) + '\n')
        firstDraw = 1
        time.sleep(2)
# If the player's hand value is less than or equal to 21, the player has the choice to hit or stay #
    if playerHandValue <= 21:
        hitOrStayChoice = ''
        while hitOrStayChoice != 'hit' or 'stay':
            hitOrStayChoice = input('Do you \'hit\' or \'stay\'?' '\n')
            if hitOrStayChoice == 'hit':
                dealtCard1Number = random.randint(0, len(deck)-1)
                dealtCard1 = deck[dealtCard1Number]
                playerHand.append(dealtCard1)
                del deck[dealtCard1Number]
                print('You were dealt ' + dealtCard1)
                findHandValue()
            if hitOrStayChoice == 'stay':
                revealDealerHand()
# If the player's hand value is over 21, the player loses automatically #
    elif playerHandValue > 21:
        loseGame()

def revealDealerHand():
    global playerHand
    global playerHandValue
    global dealerHand
    global dealerHandValue

    dealerHandValue = 0
# The value of the dealer's cards is determined in the same manner as the player's cards #
    if '2sp' in dealerHand:
        dealerHandValue = dealerHandValue + 2
    if '3sp' in dealerHand:
        dealerHandValue = dealerHandValue + 3
    if '4sp' in dealerHand:
        dealerHandValue = dealerHandValue + 4
    if '5sp' in dealerHand:
        dealerHandValue = dealerHandValue + 5
    if '6sp' in dealerHand:
        dealerHandValue = dealerHandValue + 6
    if '7sp' in dealerHand:
        dealerHandValue = dealerHandValue + 7
    if '8sp' in dealerHand:
        dealerHandValue = dealerHandValue + 8
    if '9sp' in dealerHand:
        dealerHandValue = dealerHandValue + 9
    if '10sp' in dealerHand:
        dealerHandValue = dealerHandValue + 10
    if 'Jsp' in dealerHand:
        dealerHandValue = dealerHandValue + 10
    if 'Qsp' in dealerHand:
        dealerHandValue = dealerHandValue + 10
    if 'Ksp' in dealerHand:
        dealerHandValue = dealerHandValue + 10
    if 'Asp' in dealerHand:
        dealerHandValue = dealerHandValue + 11
    if '2cl' in dealerHand:
        dealerHandValue = dealerHandValue + 2
    if '3cl' in dealerHand:
        dealerHandValue = dealerHandValue + 3
    if '4cl' in dealerHand:
        dealerHandValue = dealerHandValue + 4
    if '5cl' in dealerHand:
        dealerHandValue = dealerHandValue + 5
    if '6cl' in dealerHand:
        dealerHandValue = dealerHandValue + 6
    if '7cl' in dealerHand:
        dealerHandValue = dealerHandValue + 7
    if '8cl' in dealerHand:
        dealerHandValue = dealerHandValue + 8
    if '9cl' in dealerHand:
        dealerHandValue = dealerHandValue + 9
    if '10cl' in dealerHand:
        dealerHandValue = dealerHandValue + 10
    if 'Jcl' in dealerHand:
        dealerHandValue = dealerHandValue + 10
    if 'Qcl' in dealerHand:
        dealerHandValue = dealerHandValue + 10
    if 'Kcl' in dealerHand:
        dealerHandValue = dealerHandValue + 10
    if 'Acl' in dealerHand:
        dealerHandValue = dealerHandValue + 11
    if '2he' in dealerHand:
        dealerHandValue = dealerHandValue + 2
    if '3he' in dealerHand:
        dealerHandValue = dealerHandValue + 3
    if '4he' in dealerHand:
        dealerHandValue = dealerHandValue + 4
    if '5he' in dealerHand:
        dealerHandValue = dealerHandValue + 5
    if '6he' in dealerHand:
        dealerHandValue = dealerHandValue + 6
    if '7he' in dealerHand:
        dealerHandValue = dealerHandValue + 7
    if '8he' in dealerHand:
        dealerHandValue = dealerHandValue + 8
    if '9he' in dealerHand:
        dealerHandValue = dealerHandValue + 9
    if '10he' in dealerHand:
        dealerHandValue = dealerHandValue + 10
    if 'Jhe' in dealerHand:
        dealerHandValue = dealerHandValue + 10
    if 'Qhe' in dealerHand:
        dealerHandValue = dealerHandValue + 10
    if 'Khe' in dealerHand:
        dealerHandValue = dealerHandValue + 10
    if 'Ahe' in dealerHand:
        dealerHandValue = dealerHandValue + 11
    if '2di' in dealerHand:
        dealerHandValue = dealerHandValue + 2
    if '3di' in dealerHand:
        dealerHandValue = dealerHandValue + 3
    if '4di' in dealerHand:
        dealerHandValue = dealerHandValue + 4
    if '5di' in dealerHand:
        dealerHandValue = dealerHandValue + 5
    if '6di' in dealerHand:
        dealerHandValue = dealerHandValue + 6
    if '7di' in dealerHand:
        dealerHandValue = dealerHandValue + 7
    if '8di' in dealerHand:
        dealerHandValue = dealerHandValue + 8
    if '9di' in dealerHand:
        dealerHandValue = dealerHandValue + 9
    if '10di' in dealerHand:
        dealerHandValue = dealerHandValue + 10
    if 'Jdi' in dealerHand:
        dealerHandValue = dealerHandValue + 10
    if 'Qdi' in dealerHand:
        dealerHandValue = dealerHandValue + 10
    if 'Kdi' in dealerHand:
        dealerHandValue = dealerHandValue + 10
    if 'Adi' in dealerHand:
        dealerHandValue = dealerHandValue + 11
# this section is to allow Aces to convert from 11 points to 1 point if the hand value is over 21 #
    if dealerHandValue > 21:
        if 'Asp' in dealerHand:
            dealerHandValue = dealerHandValue - 10
        if dealerHandValue > 21:
            if 'Acl' in dealerHand:
               dealerHandValue = dealerHandValue -10
            if dealerHandValue > 21:
                if 'Adi' in dealerHand:
                   dealerHandValue = dealerHandValue -10
                if dealerHandValue > 21:
                    if 'Ahe' in dealerHand:
                         dealerHandValue = dealerHandValue -10
    # The dealer's hand is revealed #
    print('\n' + 'The dealer\'s hand is ' + str(dealerHand) + ' with a value of ' + str(dealerHandValue) + '\n')
    time.sleep(2)
    if dealerHandValue <= 16:
        dealerHit()
    if dealerHandValue > 16:
        dealerStay()

def dealerHit():
    global dealerHitCard1Number
    global dealerHitCard1
    global dealerHand
    global dealerHitCard1
    global dealerHitCard1Number
    dealerHitCard1Number = random.randint(0, len(deck)-1)
    dealerHitCard1 = deck[dealerHitCard1Number]
    dealerHand.append(dealerHitCard1)
    del deck[dealerHitCard1Number]
    print('The dealer hits and draws ' + dealerHitCard1)
    time.sleep(2)
    revealDealerHand()


def dealerStay():
    if playerHandValue <= dealerHandValue:
        if dealerHandValue <= 21:
            loseGame()
        if playerHandValue > 21:
            loseGame()
        if dealerHandValue >21 and playerHandValue <= 21:
            winGame()
    if playerHandValue > dealerHandValue:
        if playerHandValue <= 21:
            winGame()
        if playerHandValue >21:
            loseGame()

def loseGame():
    global playerHandValue
    if playerHandValue <= 21:
        print('You lose! Your hand value was ' + str(playerHandValue) + ', while the dealer\'s was ' + str(dealerHandValue) + '\n')
    elif playerHandValue > 21:
        print('You busted!' + '\n')
    askNewGame()

def winGame():
    global playerHandValue
    global dealerHandValue
    print('You won! Your hand value was ' + str(playerHandValue) + ', while the dealer\'s was ' + str(dealerHandValue) + '\n')
    newGame = ''
    while newGame != 'yes' or 'no':
        askNewGame()

def askNewGame():
    
def askNewGame():
    print('New game'!)



print('Welcome to Blackjack' + '\n')

input("Press Enter to deal your first hand.")
dealHand()
