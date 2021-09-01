# -*- coding: utf-8 -*-
"""
----------------------------------------------------------
Program : Demonstrates homomorphic properties of Paillier
          crypto system and a basic practical example
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

print(bcolors.OKGREEN+'\nDEMO : Paillier Partial Homomorphic Encryption : CA Entitlement Computation\n------------------------------------------------------------------------\n'+bcolors.ENDC)

b = [0,0,0,0,0]
cipher1 = [0,0,0,0,0]
cipher11 = [0,0,0,0,0]
ans1 = [0,0,0,0,0]
p=3331#97
q=3343#89
b[0] = 100
b[1] = 125
b[2] = 150
b[3] = 125
b[4] = 200
rate = 2
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
raw_input("Generate Keys : Continue ...")

print(bcolors.OKGREEN+'------------------------------------------------------------------------')
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
print'\nPublic Key (g,n) \t: ',g,',',n,'\nPrivate Key (lambda,mu) : ',gLambda,',',gMu
raw_input("\nEncrypt : Continue ...")

print(bcolors.OKGREEN+'------------------------------------------------------------------------')
print('Encryption'+bcolors.ENDC)

k1 = pow(g, m, n*n)
k2 = pow(r, n, n*n)
print'\nAccount\tInstrument\tBalance\tEncrypted Balance'
for i in range(0,5):
    r = randint(20,150)
    k11 = pow(g, b[i], n*n)
    k22 = pow(r, n, n*n) 
    cipher1[i] = (k11 * k22) % (n*n)
    print'Acc_',i,'\tIns1      \t',b[i],'\t',cipher1[i]

ans2 = 0
ans_final = 0
raw_input("\nEntitlement Computation : Continue ...")
print(bcolors.OKGREEN+'------------------------------------------------------------------------')
print('Computing on Encrypted Data\n'+bcolors.ENDC)

print'Computing the entitlements of individual clients ...\nScalar Multiplication : Raise the ciphertext to the power of Scalar'
print'\nCash Dividend Rate : $2 per share'
print'\nAccount\tBalance\tCipher Entitlement'

for i in range(0,5):
    
    cipher11[i] = (pow(cipher1[i],rate)) % (n*n)
    l = (pow(cipher11[i], gLambda, n*n)-1) // n
    ans1[i] = (l * gMu) % n
    print'Acc_',i,'\t',b[i],'\t',cipher11[i],''+bcolors.ENDC
    if i == 0:
        ans2 = cipher11[i]
    if i > 0:
        ans2 = (cipher11[i]* ans2) % (n*n)
        
l = (pow(ans2, gLambda, n*n)-1) // n
ans_final = (l * gMu) % n
print'\nComputing the total obligation for the issuer ...\nAddition : Multiply the ciphertexts together'
print'\nTotal Entitlements'
print'Encrypted : ',ans2,''+bcolors.ENDC


raw_input("\nDecrypt : Continue ...")
print(bcolors.OKGREEN+'------------------------------------------------------------------------')
print('Decrypting the Results\n'+bcolors.ENDC)

print'Account\tBalance\tDecrypted Entitlement'
for i in range(0,5):

    cipher11[i] = (pow(cipher1[i],rate)) % (n*n)
    l = (pow(cipher11[i], gLambda, n*n)-1) // n
    ans1[i] = (l * gMu) % n
    print'Acc_',i,'\t',b[i],''+bcolors.WARNING+'  \t\t$',ans1[i],''+bcolors.ENDC
    if i == 0:
        ans2 = cipher11[i]
    if i > 0:
        ans2 = (cipher11[i]* ans2) % (n*n)

print'\nTotal Entitlements, Decrypted : ',''+bcolors.WARNING+'$',ans_final,''+bcolors.ENDC
print'\n'

