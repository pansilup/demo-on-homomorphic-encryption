# -*- coding: utf-8 -*-
"""
----------------------------------------------------------
Program : Demonstrates homomorphic properties of Paillier
          crypto system
Author  : Pansilu Pitigalaarachchi
Created : on Mon Sep 14 11:54:36 2020

Based on: Concepts & Examples of https://asecuritysite.com 
          and thanks to the world of Free online resources
----------------------------------------------------------
"""


from random import randint
# import libnum
import sys
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b // gcd(a, b)



def L(x,n):
        return ((x-1)//n)

def modInverse(a, m) :
    a = a % m;
    for x in range(1, m) :
        if ((a * x) % m == 1) :
            return x
    return 1

def relPrime(g,n):
    result = 0
    if (gcd(g,n*n)==1):
        print'g is relatively prime to n*n';result = 1;
    else:
        print'WARNING: g is NOT relatively prime to n*n. Will not work!!!'
    return g,result

print(bcolors.OKGREEN+'\nDEMO : Paillier Partial Homomorphic Encryption\n----------------------------------------\n')

p=97
q=89
m=1250
m1 = 100




if (len(sys.argv)>1):
        m=int(sys.argv[1])

if (len(sys.argv)>2):
        p=int(sys.argv[2])

if (len(sys.argv)>3):
        q=int(sys.argv[3])

if (p==q):
        print'P and Q cannot be the same'
        sys.exit()

n = p*q

gLambda = lcm(p-1,q-1)
print'----------------------------------------'
print('Key Generation\n'+bcolors.ENDC)
result = 0
while( result == 0):
    g,result = relPrime(randint(20,150),n)
    if(result == 1):
        print'g OK'
    else:
        print'g Not OK'

r = randint(20,150)


l = (pow(g, gLambda, n*n)-1)//n
gMu = modInverse(l, n)



k1 = pow(g, m, n*n)
k2 = pow(r, n, n*n)


cipher = (k1 * k2) % (n*n)


l = (pow(cipher, gLambda, n*n)-1) // n

mess= (l * gMu) % n

print'\nPublic key (n,g):\t\t',n,g
print'Private key (lambda,mu):\t',gLambda,gMu
print(bcolors.OKGREEN+'\n----------------------------------------')
print('Encryption'+bcolors.ENDC)
print'\nMessage:\t',mess
print'Cipher1:\t',cipher
#print'Decrypted:\t',mess


k3 = pow(g, m1, n*n)

cipher2 = (k3 * k2) % (n*n)
print'\nMessage:\t',m1

print'Cipher2:\t',cipher2
#m1=3
print(bcolors.OKGREEN+'\n----------------------------------------')
print('Computing on Encrypted Data'+bcolors.ENDC)

print'\nMultiply Cipher1 and 2 to generate the cipher for addition'

ciphertotal = (cipher* cipher2) % (n*n)



l = (pow(ciphertotal, gLambda, n*n)-1) // n

mess2= (l * gMu) % n


print'Answer in encrypted form:\t',ciphertotal
print(bcolors.OKGREEN+'\n----------------------------------------')
#m1=3
print('Decryption'+bcolors.ENDC)
print'\nDecrypted Answer:\t\t',mess2,'\n'

