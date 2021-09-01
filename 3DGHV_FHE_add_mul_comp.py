# -*- coding: utf-8 -*-
"""
----------------------------------------------------------
Program : Demonstrates DGHV fully homomorphic encryption 
          scheme and examples for Addition, Subtraction, 
          Multiplication & Comparison
Author  : Pansilu Pitigalaarachchi
Created : on Mon Sep 14 11:54:36 2020

Based on: Concepts & Examples of https://asecuritysite.com
          and thanks to the world of Free online resources
----------------------------------------------------------
"""


import sys
from random import randint

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def tobits(val):
	l = [0]*(8)

	l[0]=val & 0x1
	l[1]=(val & 0x2)>>1
	l[2]=(val & 0x4)>>2
	l[3]=(val & 0x8)>>3
	return l

def XOR(a,b):
    return ( (NOT(a)*b) + (a*NOT(b)))

def NOT(val):
	return(val ^ 1)

def AND(a,b):
	return(a*b)

def OR(a,b):
	return(a+b)

def HA(bit1,bit2):
	sum=XOR(bit1,bit2)
	carryout=AND(bit1,bit2)
	return sum,carryout

def FA(bit1,bit2,cin):
	sum1,c1=HA(bit1,bit2)
	sum,c2=HA(sum1,cin)
	carryout=OR(c1,c2)
	return sum,carryout

def FOURBITADDER(*value):
    i = 0
    for n in value:
        i = i + 1
        if(i==1):cval_a0 = n
        if(i==2):cval_a1 = n
        if(i==3):cval_a2 = n
        if(i==4):cval_a3 = n
        if(i==5):cval_b0 = n
        if(i==6):cval_b1 = n
        if(i==7):cval_b2 = n
        if(i==8):cval_b3 = n
        if(i==9):c_carryin = n
    c_sum1,c_carryout=FA(cval_a0,cval_b0,c_carryin )
    c_sum2,c_carryout=FA(cval_a1,cval_b1,c_carryout )
    c_sum3,c_carryout=FA(cval_a2,cval_b2,c_carryout )
    c_sum4,c_carryout=FA(cval_a3,cval_b3,c_carryout )
    return c_sum1,c_sum2,c_sum3,c_sum4,c_carryout

def TWOBITMUL(*value):
    i = 0
    for n in value:
        i = i + 1
        if(i==1):cval_a0 = n
        if(i==2):cval_a1 = n
        if(i==3):cval_b0 = n
        if(i==4):cval_b1 = n
    c_mul1 = AND(cval_a0,cval_b0)
    c_mul2,c_carryout = HA(AND(cval_a1,cval_b0),AND(cval_a0,cval_b1))
    c_mul3,c_mul4 = HA(c_carryout,AND(cval_a1,cval_b1))
    return c_mul1,c_mul2,c_mul3,c_mul4

def THREEBITMUL(*value):
    i = 0
    for n in value:
        i = i + 1
        if(i==1):cval_a0 = n
        if(i==2):cval_a1 = n
        if(i==3):cval_a2 = n
        if(i==4):cval_b0 = n
        if(i==5):cval_b1 = n
        if(i==6):cval_b2 = n    
    cml0 = AND(cval_a0,cval_b0)
    cml1,ha1_c = HA(AND(cval_a1,cval_b0),AND(cval_a0,cval_b1))
    ha2_out,ha2_c = HA(AND(cval_a2,cval_b0),AND(cval_a1,cval_b1))
    cml2,fa1_c = FA(AND(cval_a0,cval_b2),ha2_out,ha1_c)
    fa2_out,fa2_c = FA(AND(cval_a1,cval_b2),AND(cval_a2,cval_b1),ha2_c)
    cml3,ha3_c = HA(fa2_out,fa1_c)
    cml4,cml5 = FA(AND(cval_a2,cval_b2),fa2_c,ha3_c)
    return cml0,cml1,cml2,cml3,cml4,cml5      
    
def cipher(bit,p):
	q=randint(20000, 30000)
	r=randint(1,10)
	return(  q * p + 2*r +int(bit)),q,r

def inv(val):
	return(val ^ 1)

max_no = int(15)
print(bcolors.OKGREEN)
print(bcolors.UNDERLINE+'DEMO : DGHV Fully Homomorphic Encryption : Addition,Subtraction,Multiplication and Millionaires\' problem')
val1 = 3
val2 = 2
#val1 = int(input("Enter Number 1 : "))
#val2 = int(input("Enter Number 2 : "))

#err = 0
#if(val1 > max_no):
#    print("Number 1 is invalid");err = 1;
#if(val2 > max_no):
#    print("Number 2 is invalid");err = 1;
#if(err == 1):
#    sys.exit()


cin=0

v1=[]
v2=[]

v1=tobits(val1)
v2=tobits(val2)
print(bcolors.ENDC)
raw_input("Key Generation : Continue ...")
print(bcolors.OKGREEN+'# Key Generation >>')
print("-----------------------------------------------------------------------------------------------------")
p =randint(3e23, 6e23)*2+1
public_key = [0 for i in range(32)]

print('Public key:'+bcolors.ENDC)
for i in range(0,len(public_key)):
	public_key[i],q,r = cipher(0,p)
	print public_key[i],   
print(bcolors.OKGREEN+'\nSecret Key : '+bcolors.ENDC)
print p
print(bcolors.OKGREEN+'\nPlain Text Numbers : '+bcolors.ENDC)
print val1,', ',val2
raw_input("\nEncryption : Continue ...")
print(bcolors.OKGREEN+'\n\n# Encryption >>')
print("-----------------------------------------------------------------------------------------------------")

c_carryin,q,r=cipher(cin,p)

cval_a0,q,r=cipher(v1[0],p)
cval_b0,q,r=cipher(v2[0],p)

cval_a1,q,r=cipher(v1[1],p)
cval_b1,q,r=cipher(v2[1],p)

cval_a2,q,r=cipher(v1[2],p)
cval_b2,q,r=cipher(v2[2],p)

cval_a3,q,r=cipher(v1[3],p)
cval_b3,q,r=cipher(v2[3],p)
print(bcolors.OKGREEN+'Cipher Text : Number 1'+bcolors.ENDC)
print cval_a0,cval_a1,cval_a2,cval_a3
print(bcolors.OKGREEN+'Cipher Text : Number 2'+bcolors.ENDC)
print cval_b0,cval_b1,cval_b2,cval_b3
raw_input("\nComputations : Continue ...")
print(bcolors.OKGREEN+'\n\n# Computing On Encrypted Data >>')
print("-----------------------------------------------------------------------------------------------------")
print (bcolors.OKGREEN+'Addition \t: Answer in Encrypted form'+bcolors.ENDC)
#c_sum1,c_carryout=FA(cval_a0,cval_b0,c_carryin )
#c_sum2,c_carryout=FA(cval_a1,cval_b1,c_carryout )
#c_sum3,c_carryout=FA(cval_a2,cval_b2,c_carryout )
#c_sum4,c_carryout=FA(cval_a3,cval_b3,c_carryout )
c_sum1,c_sum2,c_sum3,c_sum4,c_carryout = FOURBITADDER(cval_a0,cval_a1,cval_a2,cval_a3,cval_b0,cval_b1,cval_b2,cval_b3,c_carryin)
print c_sum1,c_sum2,c_sum3,c_sum4

#decrypt

sum1 = (c_sum1 % p) % 2
sum2 = (c_sum2 % p) % 2
sum3 = (c_sum3 % p) % 2
sum4 = (c_sum4 % p) % 2
carryout = (c_carryout % p) % 2

print (bcolors.OKGREEN+'Subtraction \t: Answer in Encrypted form'+bcolors.ENDC)
c_carryin,q,r=cipher(1,p)
c_sum1_,c_carryout=FA(cval_a0,XOR(cval_b0,c_carryin),c_carryin )
c_sum2_,c_carryout=FA(cval_a1,XOR(cval_b1,c_carryin),c_carryout )
c_sum3_,c_carryout=FA(cval_a2,XOR(cval_b2,c_carryin),c_carryout )
c_sum4_,c_carryout=FA(cval_a3,XOR(cval_b3,c_carryin),c_carryout )

#c_sum1_,c_sum2_,c_sum3_,c_sum4_,c_carryout = FOURBITADDER(cval_a0,cval_a1,cval_a2,cval_a3,cval_b0,cval_b1,cval_b2,cval_b3,c_carryin)
print c_sum1_,c_sum2_,c_sum3_,c_sum4_

sum1_ = (c_sum1_ % p) % 2
sum2_ = (c_sum2_ % p) % 2
sum3_ = (c_sum3_ % p) % 2
sum4_ = (c_sum4_ % p) % 2
carryout = (c_carryout % p) % 2


print(bcolors.OKGREEN+'Multiplication \t: Answer in Encrypted form'+bcolors.ENDC)
#c_mul1 = AND(cval_a0,cval_b0)
#c_mul2,c_carryout = HA(AND(cval_a1,cval_b0),AND(cval_a0,cval_b1))
#c_mul3,c_mul4 = HA(c_carryout,AND(cval_a1,cval_b1))
c_mul1,c_mul2,c_mul3,c_mul4 = TWOBITMUL(cval_a0,cval_a1,cval_b0,cval_b1)
print c_mul1,c_mul2,c_mul3,c_mul4

mul1 = (c_mul4 % p) % 2
mul2 = (c_mul3 % p) % 2
mul3 = (c_mul2 % p) % 2
mul4 = (c_mul1 % p) % 2

#c_mul1,c_mul2,c_mul3,c_mul4,c_mul5,c_mul6 = THREEBITMUL(cval_a0,cval_a1,cval_a2,cval_b0,cval_b1,cval_b2)
#mul1 = (c_mul6 % p) % 2
#mul2 = (c_mul5 % p) % 2
#mul3 = (c_mul4 % p) % 2
#mul4 = (c_mul3 % p) % 2
#mul5 = (c_mul2 % p) % 2
#mul6 = (c_mul1 % p) % 2
#print(c_mul1,c_mul2,c_mul3,c_mul4,c_mul5,c_mul6)

print(bcolors.OKGREEN+'Comparison \t: Answer in Encrypted form'+bcolors.ENDC)
cipher_older = inv(cval_a1)*cval_b1 + inv(cval_a1)*inv(cval_a0)*cval_b0  + inv(cval_a0)*cval_b1*cval_b0
print cipher_older
compresult = (cipher_older % p) % 2
raw_input("\nDecryption : Continue ...")
print(bcolors.OKGREEN+'\n\n# Decyption of computation results >>')
print("-----------------------------------------------------------------------------------------------------")
print'Number 1:',val1
print'Number 2:',val2
print'\nResult of Addition\t: ',sum4,sum3,sum2,sum1,' -> ',sum4*8+sum3*4+sum2*2+sum1*1
#print'Carry-out:\t',carryout
print'Result of Substraction\t: ',sum4_,sum3_,sum2_,sum1_,' -> ',sum4_*8+sum3_*4+sum2_*2+sum1_*1

print'Result of Multiplication: ',mul1,mul2,mul3,mul4,' -> ',mul1*8+mul2*4+mul3*2+mul4*1
if (compresult==1):
	print'Result of Comparison\t: ',compresult,'\t    ->  Number 2 is greter than Number 1'
else:
	print'Result of Comparison\t: ',compresult,'\t    ->  Number 2 is NOT greter than Number 1'
print(bcolors.ENDC)
