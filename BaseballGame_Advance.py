#Baseball Game
#2009024249 Hyun-gil Nam

import random

def getRandomDigit():
    intList = [random.randint(1,10)]
    while len(intList) < 3:
        r = random.randint(0, 10)
        if r in intList:
            continue
        else:
            intList.append(r)

    strList = ''
    for e in intList:
        strList += str(e)
    return strList

def getFighter(outNumbers, secretInt): #Com2: Player like human!!!--> pick numbers except Out numbers..
    intList = [random.randint(1,10)]
    while len(intList) < 3:
        r = random.randint(0, 10)
        if r in intList or str(r) in outNumbers:
            continue
        else:
            intList.append(r)

    strList = ''
    for e in intList:
        strList += str(e)
    return strList
 
def getGuess(alreadyGuessed, outNumbers, secretInt):
    while True:
        print 'Guess 3 digits' 
        guess = getFighter(outNumbers, secretInt)
        print str(guess)
        if len(guess) != 3:
            print 'Please enter 3 digits.'
        elif guess in alreadyGuessed:
            print 'You have already guessed that digit. Choose again.'
        elif guess[0] == 0:
            print 'Do not start digit 0'
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
outNumbers = ''
while True:
    strikeCounter = 0
    ballCounter = 0
    guess = getGuess(alreadyInts, outNumbers, secretInt)
    
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
            outNumbers = outNumbers + guess
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
    
