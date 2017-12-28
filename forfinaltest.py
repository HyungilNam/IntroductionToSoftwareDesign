import random
def string_generator(leng):
    i=0
    basic='a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
    st = str('')
    while i<leng:
        temp = random.randint(0,25)
        st += basic[temp]
        i=i+1
    return st

length = int(raw_input('Input the length of the string: '))
gen_string =string_generator(length)
print 'Generated random word is \''+gen_string+'\''


for i in range(1,6):
    strline =str('')
    for j in range(5-i):
        strline =strline + ' '
    for j in range(i-1):
        strline =strline + '*'
    print strline

for i in range(0,4):
    k = 4-i
    strline =str('')
    for j in range(4):
        strline =strline + ' '
    for j in range(k):
        strline =strline + '*'
    print strline
