#banding machine

def Coke(money):
    if money<800:
        money2 = money
        print 'Lack of Rest'
        return money2

    else:
        money2 = money - 800
        print 'Here is Coke, Your deposit is '+ str(money2)
        return money2
    
def Cidar(money):
    if money < 700:
        money2 = money
        print 'Lack of Rest'
        return money2

    else:
        money2 = money - 700
        print 'Here is Cidar, Your deposit is '+ str(money2)
        return money2
    
def Hotsix(money):
    if money<500:
        money2 = money
        print 'Lack of Rest'
        return money2

    else:
        money2 = money - 500
        print 'Here is Hot six, Your deposit is '+ str(money2)
        return money2
        

print 'Are you going to drink at Banding machine?'
print 'Give me some money'
yourDeposit = int(raw_input())
yourChoice = 0
onOff = 0

while(onOff<1):
    print "--------------------------------"
    print 'Your deposit is '+str(yourDeposit)
    print 'What is your Choice?'
    print 'Coke 800 WON(1), Cidar 700 WON(2), Hot six 500 WON(3), Rest(4)'
    yourChoice = int(raw_input())

    if yourChoice == 1:
        yourDeposit = Coke(yourDeposit)

    if yourChoice == 2:
        yourDeposit = Cidar(yourDeposit)

    if yourChoice == 3:
        yourDeposit = Hotsix(yourDeposit)

    if yourChoice == 4:
        print 'Here!! '+str(yourDeposit)
        onOff = 1
        
    if yourDeposit < 500:
        print 'Lack of money'
        onOff = 1
