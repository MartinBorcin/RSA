import random

def gcd(A,B):
    gcd=0
    R=1
    while R != 0:
        if A==0:
            gcd=B
        elif B==0:
            gcd=A
        else:
            R=A%B
            A=B
            B=R
    return (A)

def isprime(p, k=20):
    global t
    if (p <= 2 ):
        return True
    for i in range(0, k):
        a = random.randint(1, p-1)
        if (pow(a, p-1, p) != 1):
            return False
    return True

def key(p):
    if p%2==0:
        p=p+1
    while True:
        if isprime(p):
            return(p)
            break        
        else:
            p=p+2

def e():
    global phin
    k=random.randrange(2, phin)
    while True:
        if gcd(k, phin) == 1:
            return (k)
        else:
            k=k+1
            if k==phin:
                k=random.randrange(2, phin)   

def d(a,b,r=1,p0=0,p1=1):
    m=b
    while r!=0:
        r=b%a
        if r==0:
            return(p2)
        q=b//a
        p2=(p0-p1*q)%m
        p0=p1
        p1=p2
        b=a
        a=r

p=random.randrange(10**300,10**450)
q=random.randrange(10**70,10**450)

p=(key(p))
q=(key(q))

n=p*q
phin=(p-1)*(q-1)
e = e()
d = d(e, phin)

tajny = e
mod = n
verejny = d

print("Verejny: ", verejny, "\n")
print(len(str(verejny)))
print("Tajny: ", tajny, "\n")
print(len(str(tajny)))


public = open("public_key.txt", "w")
private = open("private_key.txt", "w")

public.write(str(verejny) + "\n")
public.write(str(mod))

private.write(str(tajny) + "\n")
private.write(str(mod))

public.close()
private.close()

file = open("message.txt", "r")
for line in file:
    for pismeno in line:
        encrypt = pow(ord(pismeno), e, n)
        decrypt = pow(encrypt, d, n)
        print(chr(decrypt), end = '')
file.close()





