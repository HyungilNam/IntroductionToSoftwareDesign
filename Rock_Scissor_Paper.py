#Rocks/Scissors/Papers

import random
import time


Choice = ['Rock', 'Scissor', 'Paper']

j = random.randint(0,2)

Computer_j = Choice[j]

winner = Computer
ment = 'Rocks~, Scissors~, Papers!'

while winner != Computer or winner != Same:
    for i in range(len(ment)):
        time.sleep[1]
        print ment.split()

    YourChoice = raw_input()

    if(Computer_j == YourChoice):
        winner = Same

        elif(YourChoice == 'Rock' and Computer_j == 'Scissor'):
            winner = You
            elif(YourChoice == 'Rock' and Computer_j == 'Paper'):
                winner = Computer

        elif(YourChoice == 'Scissor' and Computer_j == 'Rock'):
            winner = Computer
            elif(YourChoice == 'Scissor' and Computer_j == 'Paper'):
                winner = You

        elif(YourChoice == 'Paper' and Computer_j == 'Scissor'):
            winner = Computer
            elif(ourChoice == 'Paper' and Computer_j == 'Rock'):
                winner = You
                    
        if winner == 'You':
            print 'You win! Computer lose! (You'+ YourChoice + 'Com'+Computer_j+')'
            elif winner == 'Computer':
                print 'You lose! Computer win! Again!(You'+ YourChoice + 'Com'+Computer_j+')'
            elif winner == 'Same'
                print 'Same! Again!(You'+ YourChoice + 'Com'+Computer_j+')'





