#GivenNum BlankPyramid

def MakeP(GivenNum):
    Counter = 0
    
    while(Counter < GivenNum):
        if(Counter == 0):
            blank =GivenNum-1
            while(Counter < blank):
                print ' ',
                blank = blank - 1
            print '*'
        if(0 < Counter < GivenNum-1):
            blank =GivenNum-1
            while(Counter < blank):
                print ' ',
                blank = blank - 1
            markcounter = 0
            print '*',
            while(markcounter < (Counter *2)-1):
                print ' ',
                markcounter = markcounter + 1

            print '*'
        if(Counter == GivenNum-1):
            markcounter = 0
            while(markcounter < (Counter *2)+1):
                print '*',
                markcounter = markcounter + 1
        Counter = Counter + 1


print 'Give me Number: '
GivenNum = int(raw_input())

MakeP(GivenNum)



