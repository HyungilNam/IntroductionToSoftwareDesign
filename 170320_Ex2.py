#170320_Exercise2
#Summation/Average/Max/Min

def Totaltotal(a,NumNum):
    Total = a + NumNum
    return Total

def Max(NowMax,A):
    if(NowMax < A):
        NowMax = A
    return NowMax

def Min(NowMin, A):
    if(NowMin > A):
        NowMin = A
    return NowMin

Count = -1
A = ''
Sum = 0
Ave = 0
NowMax = ''
NowMin = ''
print 'Select the Function'
print '1.Summation, 2.Average, 3.Max, 4.Min'
Select = ''
Select = raw_input()
Select = int(Select)

if(Select == 1):
    print 'Input numbers'
    while(A != 0):
        A = raw_input()
        A = int(A)
        Sum = Totaltotal(Sum, A)
    print 'The total is '+ str(Sum)

if(Select == 2):
    print 'Input numbers'
    while(A != 0):
        A = raw_input()
        A = int(A)
        Sum = Totaltotal(Sum, A)
        Count = Count + 1
    Ave = float(Sum/Count)
    print 'The average is '+ str(Ave)

if(Select == 3):
    print 'Input numbers'
    while(A != 0):
        A = raw_input()
        A = int(A)
        NowMax = Max(NowMax, A)
    print 'The max number is ' + str(NowMax)
    
if(Select == 4):
    print 'Input numbers'
    while(A!=0):
        A = raw_input()
        A = int(A)
        if(A != 0):
            NowMin = Min(NowMin, A)
    print 'The min number is ' + str(NowMin)

