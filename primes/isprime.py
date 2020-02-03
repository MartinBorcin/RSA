import random
import time

export = open('export.txt', 'w')
export.write('')
export.close()

def isprime(p, k=10):
    global t
#    t = time.clock()
#    print('\nchecking if prime...')
    if (p <= 2 ):
        return True
    for i in range(0, k):
        a = random.randint(1, p-1)
        if (pow(a, p-1, p) != 1):
            return False
#    print ('time: '+ str(time.clock()-t))
    return True


for i in range(0,100000,50):
    t=time.clock()
    cislo = 10**i+7
    print(cislo)
    if isprime(cislo):
        print ('yes')
    else:
        print('no')
    export = open('export.txt', 'a')
    export.write(str(i)+ ' ; ' + str(time.clock()-t)+ '\n')
    export.close()
    print ('time: '+ str(time.clock()-t)+' sec')
    print (str(i) + ' cifier\n')


