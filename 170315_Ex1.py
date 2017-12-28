#Exercise1

import random
import time

print '******Start******'

counter = 1

while(counter < 6):

    A = random.randint(1,9)
    B = random.randint(1,9)

    print str(A)+'*'+str(B) +'=?'

    CorrectA = A * B

    time.sleep(3)
    GuessNum = raw_input()
    GuessNum = int(GuessNum)
    
    if(CorrectA==GuessNum):
        print 'Correct Answer'


    if(CorrectA!=GuessNum):
        print 'Wrong Answer, '+ str(A)+'*'+str(B)+'='+str(CorrectA)

    counter = counter + 1
