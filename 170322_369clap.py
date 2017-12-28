#3,6,9 clap

def ClapFinder(CountNum):
    Feature = CountNum
    Head = 0
    Tail = 0
    clapcounter = 0
    while(Feature != 0):
        Head = Feature/10
        Tail = Feature%10
        if(Tail==3 or Tail==6 or Tail==9):
            print 'clap!',
            clapcounter = clapcounter + 1

        Feature = Head
        

    if(clapcounter == 0):
        if(Tail != 3 and Tail != 6 and Tail != 9):
            print str(CountNum),

    print
        


print 'Give me Last Number:'
GivenNum = int(raw_input())
Counter = 1


print '**********Start**********'
while(Counter <= GivenNum):    
    ClapFinder(Counter)
    Counter = Counter+1
