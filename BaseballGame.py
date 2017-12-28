#Baseball Game
#2009024249 Hyun-gil Nam

import random

def getRandomDigit():
    intList = random.randint(102,987)
    intList = str(intList)
    if(intList[0]==intList[1]or intList[0]==intList[1]or intList[1]==intList[2]):
        while(intList[0]!=intList[1]and intList[0]!=intList[1]and intList[1]!=intList[2]):
            intList = random.randit(102,987)
    return intList

def getGuess(alreadyGuessed, secretInt):
    while True:
        print 'Guess 3 digits' 
        guess = raw_input()
        if len(guess) != 3:
            print 'Please enter 3 digits.'
        elif guess in alreadyGuessed:
            print 'You have already guessed that digit. Choose again.'
        elif guess[0] == 0:
            print 'Do not start digit 0'
        elif int(guess)<100 or int(guess)>999:
            print 'Please enter digits'
        else:
            return guess
            break

def playAgain():
    print 'Do you want to play again?(yes or no)'
    return raw_input().startswith('y')

print '=======Start========'
alreadyInts = ''
secretInt = getRandomDigit()
gameIsDone = False
strikeCounter = 0
ballCounter = 0

while True:
    strikeCounter = 0
    ballCounter = 0
    guess = getGuess(alreadyInts, secretInt)
    if guess[0] in secretInt:
        alreadyInts = alreadyInts + guess
        
        if guess[0] == secretInt[0]:
            strikeCounter += 1
        else:
            ballCounter += 1
            
    if guess[1] in secretInt:
        if guess[1] == secretInt[1]:
            strikeCounter += 1
        else:
            ballCounter += 1

    if guess[2] in secretInt:
        if guess[2] == secretInt[2]:
            strikeCounter +=1
        else:
            ballCounter += 1

    if strikeCounter == 3:
        print 'Homerun!' + secretInt
        gameIsDone = True
    else:
        if ballCounter == 0 and strikeCounter == 0:
            print 'Out!'
            gameIsDone = False

        else:
            print 'Ball : ' + str(ballCounter )+ ', Strike : ' + str(strikeCounter)
            gameIsDone = False

    if gameIsDone:
        if playAgain():
            missedInt = ''
            correctInt = ''
            gameIsDone = False
            secretInt = getRandomInt()
        else:
            break
    
