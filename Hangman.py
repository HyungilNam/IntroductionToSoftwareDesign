import random

HANGMANPICS = ['''

    +---+
    |   |
        |
        |
        |
        |
=============''', '''

    +---+
    |   |
    o   |
        |
        |
        |
=============''', '''

    +---+
    |   |
    o   |
    |   |
        |
        |
=============''', '''

    +---+
    |   |
    o   |
   /|   |
        |
        |
=============''', '''

    +---+
    |   |
    o   |
   /|\  |
        |
        |
=============''', '''

    +---+
    |   |
    o   |
   /|\  |
   /    |
        |
=============''', '''


    +---+
    |   |
    o   |
   /|\  |
   / \  |
        |
=============''']

words2 = 'ant baboon badger bat bear camel cat clam cobra cougar coyote crow deerdog donkey eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle warsel whale wolf wombat zebra'.split()
words = 'apple banana mango orange lemon cherry strawberry pears kiwi blueberry peach melon avocado coconut grapes berry walnut '.split()

def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList)-1)
    return wordList[wordIndex]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print HANGMANPICS[len(missedLetters)]
    print

    print 'Missed Letters:',
    for letter in missedLetters:
        print letter,
    print

    blanks = '_'*len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks= blanks[:i] + secretWord[i] + blanks[i+1:]
    print
    print '=>',
    for letter in blanks:
        print letter,
    print

def getGuess(alreadyGuessed):
    while True:
        print 'Guess a letter.'
        guess = raw_input()
        guess = guess.lower()
        if len(guess) != 1:
            print 'Please enter a single letter.'
        elif guess in alreadyGuessed:
            print 'You have already guessed that letter. Choose again.'
        elif guess not in 'abcdfeghijklmnopqrstuvwxyz':
            print 'Please enter a LETTER.'
        else:
            return guess
    
def playAgain():
    print 'Do you want to play again? (yes or no)'
    return raw_input().lower().startswith('y')

print 'H A N G M A N'
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print 'Yes! The secret word is "'+ secretWord + '"! You have won!'
            gameIsDone = True

    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMANPICS)-1:
                displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
                print 'You have run out of guesses!\nAfter' + str(len(missedLetters))+ 'missed guesses and ' + str(len(correctLetters)) + 'correct guesses, the word was "'+secretWord+ '"'
                gameIsDone = True
                
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetter = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
        
    
