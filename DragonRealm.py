#Practice1
#Dragon Realm --> What is function?

import random
import time

def displayIntro():         #print is function so, need not to return something
    print 'You are in a land full of dragon, In front of you,'
    print 'You see two caves, In one cave, the dragon'
    print 'and will share hits treasure wiht you. The other dragon'
    print 'Is greedy and hungry, and will eat you on sight.'
    print

def chooseCave():           # while is function, so, need to return something
    cave = ' '
    while cave != '1' and cave != '2':      #Exceptional Case!! User should pick 1 or 2 only
        print 'Which cave will you go into? (1 or 2)'   
        cave = raw_input()      #When you pick 1 or 2 escape!!

    return cave

def checkCave(chosenCave):
    print 'You approach the cave...'
    time.sleep(2)
    print 'It is dark and spooky...'
    time.sleep(2)
    print 'A large dragon jumps out in front of you! He opens his jaws and...'
    print
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print 'Gives you his treasure!'
    else:
        print 'Gobbles you down in one bite!'
    
playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':

    displayIntro()      #function call
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print 'Do you want to play again (yes or no)'
    playAgain = raw_input()


