#GivenNum Pyramid

def MakeP(GivenNum):
    Counter = 0
    
    while(Counter < GivenNum+1):
        blank =GivenNum
        while(Counter < blank):
            print ' ',
            blank = blank - 1

        markcounter = 0
        while(markcounter < (Counter *2)-1):
            print '*',
            markcounter = markcounter + 1
        print
        Counter = Counter + 1


print 'Give me Number: '
GivenNum = int(raw_input())

MakeP(GivenNum)




