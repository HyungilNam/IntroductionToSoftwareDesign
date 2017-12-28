#Practice1
#Dragon Realm


import time

def timechange(intint):
    
    if(intint % 2 == 1):
        time.sleep(intint+1)

    if(intint % 2 == 0):
        time.sleep(intint+2)


def displayIntro():         #print is function so, need not to return something
    i = 1
    timechange(i)
    print 'You ar in a land full of dragon, In front of you,'
    timechange(i+1)
    print 'You see two caves, In one cave, the dragon'
    timechange(i)
    print 'and will share hits treasure wiht you. The other dragon'
    timechange(i+1)
    print 'Is greedy and hungry, and will eat you on sight.'
    print


displayIntro()      #function call

