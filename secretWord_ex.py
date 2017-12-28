secretWord = 'pineapple'

correctLetters = 'iae'

blanks = '_' * len(secretWord)

for i in range(len(secretWord)):
    if secretWord[i] in correctLetters:
        blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    print blanks

