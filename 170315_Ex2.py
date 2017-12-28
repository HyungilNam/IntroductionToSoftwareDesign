#Exercise2
import random
import time

print '******Start******'

counter = 1

while(counter<6):

    A= random.randint(1,9)
    B= random.randint(1,9)
    C=random.randint(1,9)
    D=random.randint(1,9)

    print str(A)+'*'+str(B)+'+'+str(C)+'-'+str(D)+'= ?'

    CorrectA = A*B+C-D

    time.sleep(1)
    print 1,

    time.sleep(1)
    print 2,
    time.sleep(1)
    print 3

    GuessNum = raw_input()
    GuessNum = int(GuessNum)

    if(GuessNum == CorrectA):
        print 'Correct Answer'

    if(GuessNum != CorrectA):
        print 'Wrong Answer, '+ str(A)+'*'+str(B)+'+'+str(C)+'-'+str(D)+'='+str(CorrectA)

    counter = counter+1

    
    
