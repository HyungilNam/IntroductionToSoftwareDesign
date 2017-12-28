#170320_Exercise1
#Summation/Average/Max/Min


print 'Input numbers'

Count = 0

A = ''
Total = 0
Average = 0
Max = 0
Min = 0

while(A != 0):

    A = raw_input()
    A = int(A)
    Count = Count + 1

    Total = Total + A
    Average = float(Total/Count)
    if(Max < A):
        Max = A
    if(Min > A):
        Min = A

print 'The total is '+ str(Total)
print 'The average is '+ str(Average)
print 'The max number is ' + str(Max)
print 'The min number is ' + str(Min)
