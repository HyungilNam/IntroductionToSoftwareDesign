#170313_Mon_Practice2

print 'Input dan.'
A = raw_input()

print '**********'+ A + 'dan'+ '**********'

counter = 1
A = int(A)

while(counter < 10):
    Result = A * counter
    print str(A)+'*'+str(counter)+'='+str(Result)
    counter = counter + 1

print '***************************'
