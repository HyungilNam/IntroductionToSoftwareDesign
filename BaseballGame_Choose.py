#Baseball Game
#2009024249 Hyun-gil Nam

import random

def getRandomDigit(givenNum):
    intList = [random.randint(1,10)]
    while len(intList) < givenNum:
        r = random.randint(0, 10)
        if r in intList:
            continue
        else:
            intList.append(r)

    strList = ''
    for e in intList:
        strList += str(e)
    return strList

def getGuess(alreadyGuessed, secretInt, givenNum):
    while True:
        print 'Guess'+str(givenNum)+' digits' 
        guess = raw_input()
        if len(guess) != givenNum:
            print 'Please enter' + str(givenNum) +' digits.'
        elif guess in alreadyGuessed:
            print 'You have already guessed that digit. Choose again.'
        elif guess[0] == '0':
            print 'Do not start digit 0'
        else:
            return guess

def playAgain():
    print 'Do you want to play again?(yes or no)'
    return raw_input().startswith('y')

def ballCounter(guess, secretInt):
    ball = 0
    for i in range(len(guess)):
        for j in range(len(secretInt)):
            if guess[i] == secretInt[j] and i!=j:
                ball+=1
    return ball

def strikeCounter(guess, secretInt):
    strike = 0
    for i in range(len(guess)):
        if guess[i] == secretInt[i]:
            strike+=1
    return strike

print '=======Start========'
alreadyInts = ''
givenNum = int(raw_input())
secretInt = getRandomDigit(givenNum)
gameIsDone = False


while True:
    strikeCount = 0
    ballCount = 0
    guess = getGuess(alreadyInts, secretInt, givenNum)
    alreadyInts = alreadyInts + guess

    ballCount = ballCounter(guess, secretInt)
    strikeCount = strikeCounter(guess, secretInt)

    
    if strikeCount == givenNum:
        print 'Homerun!' + secretInt
        gameIsDone = True
    else:
        if ballCount == 0 and strikeCount == 0:
            print 'Out!'
            gameIsDone = False

        else:
            print 'Ball : ' + str(ballCount)+ ', Strike : ' + str(strikeCount)
            gameIsDone = False

    if gameIsDone:
        if playAgain():
            missedInt = ''
            correctInt = ''
            gameIsDone = False
            secretInt = getRandomInt()
        else:
            break
    

