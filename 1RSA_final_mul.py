# -*- coding: utf-8 -*-
"""
----------------------------------------------------------
Program : Demonstrates homomorphic properties of RSA
Author  : Pansilu Pitigalaarachchi
Created : on Mon Sep 14 11:54:36 2020

Based on: Concepts & Examples of https://asecuritysite.com
          and thanks to the world of Free online resources
----------------------------------------------------------
"""


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

print bcolors.OKGREEN+'\nDEMO : RSA Partial Homomorphic Encryption\n----------------------------------------\n'+bcolors.ENDC

raw_input("Key Generation : Continue ...")
print bcolors.OKGREEN+'------------------------------------------------------------------------'
print 'Key Generation\n'+bcolors.ENDC
e=65537
d=581692248042969245790410284176907073
n=902197724766112307222106340419908693
val1=250
val2=6

cipher1 = pow(val1,e,n)
cipher2 = pow(val2,e,n)

result = (cipher1 * cipher2) % n

decipher = pow(result,d,n)



print 'Public Key(e,n)\t\t: ',e, n
print 'Private Key(d,n)\t: ',d, n

raw_input("\nEncryption : Continue ...")
print bcolors.OKGREEN+'\n------------------------------------------------------------------------'
print 'Encryption\n'+bcolors.ENDC
print 'val1 \t\t:',val1
print 'val2 \t\t:',val2

print 'Cipher1 \t:',cipher1

print 'Cipher2 \t:',cipher2
raw_input("\nComputations : Continue ...")
print bcolors.OKGREEN+'\n------------------------------------------------------------------------'

print 'Computing on Encrypted Data'+bcolors.ENDC

print '\nMultiply Cipher1 and 2 to generate the cipher for multipliation'
print 'Answer in Encrypted form : ',result
raw_input("\nDecryption : Continue ...")
print bcolors.OKGREEN+'\n------------------------------------------------------------------------'
print 'Decryption\n'+bcolors.ENDC
print 'Result :',decipher
print '\n'
