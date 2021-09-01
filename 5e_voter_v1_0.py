# -*- coding: utf-8 -*-
"""
----------------------------------------------------------
Program : Paillier encryption, homomorphic addition and decryption for e-voting demo
Author  : Pansilu Pitigalaarachchi
Created : on Mon Feb 22 2021

Based on: Concepts & Examples of https://asecuritysite.com
          and thanks to the world of Free online resources
----------------------------------------------------------
"""

import PySimpleGUI as sg
from random import randint

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('--------------------------- Election : Vote now ----------------------------')],
            [sg.Button('Trump',size=(20,3)), sg.Button('Biden',size=(20,3))], 
            [sg.Text('--------------------------------------------------------------------------------------')],
            [sg.Button('Results')], 
            [sg.Button('Analysis')] 
            ]

# Create the Window
window = sg.Window('e-Voting Demo : IS708', layout,size=(380, 200))
# Event Loop to process "events" and get the "values" of the inputs


#paillier keys--------------------------------------------
n = 8633        #pk1
g = 25          #pk2
gLambda = 1056  #sk1
gMu = 404       #sk2

#utility functions----------------------------------------
def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def L(x,n):
        return ((x-1)//n)

def modInverse(a, m):
    a = a % m;
    for x in range(1, m) :
        if ((a * x) % m == 1) :
            return x
    return 1 #will not go here as l,n are already selected


#voting functions------------------------------------------

#encrypt a given vote
def paillier_enc(m):
    r = randint(20,150)
    k1 = pow(g, m, n*n)
    k2 = pow(r, n, n*n)
    cipher = (k1 * k2) % (n*n)
    return cipher #vote encrypted by public key

#vote counter
def paillier_h_add(c1, c2, c3):
    return (c1 * c2 * c3) % (n*n) #encrypted result

#decrypter
def paillier_dec(c):
    l = (pow(c, gLambda, n*n)-1) // n
    return (l * gMu) % n #result

############################################################    
#dummy election starts here---------------------------------

vote = -1
c1 = 0
c2 = 0
c3 = 0
v1 = -1
v2 = -1
v3 = -1
v11 = ''
v22 = ''
v33 = ''
cc = 0
round = 0
results_gen = 1
results = 0
analysis = 0
results_pending = 0
while True:
    voted = 0
    c = 0
    event, values = window.read()
    if (event == sg.WIN_CLOSED or event == 'Biden' or event == 'Trump') and round == 0 and results_pending == 0: #rigged
        vote = 1
        voted = 1
        v = 'Biden'
        round = round + 1
    elif (event == sg.WIN_CLOSED or event == 'Trump' or event == 'Biden') and (round == 1 or round == 2) and results_pending == 0: #rigged
        vote = 0
        voted = 1
        v = 'Trump'
        round = round + 1
    
    if voted == 1:
        print('Voter ', round, ' OK')
        c = paillier_enc(vote) #vote
        if(round == 1):
            c1 = c
            v1 = vote
            v11 = v
        elif(round == 2):
            c2 = c
            v2 = vote
            v22 = v
        elif(round == 3):
            c3 = c
            v3 = vote
            v33 = v
            results_gen = 0
            results_pending = 1
    
    
    #Vote Counting
    if (event == sg.WIN_CLOSED or event == 'Results') and round == 3 and results == 0:
        results = 1
        cc = paillier_h_add(c1, c2, c3) #encrypted result
        #print('encrypted result: ',cc)
        #final ans
        ans = paillier_dec(cc) #result
        #print('result \t\t\t: ',ans)
        if ans >= 2:
            print('\nBiden WINs : ',ans,' out of 3 votes')
        else:
            print('Trump WINs : ',3-ans,' out of 3 votes')
    #Printing analitics
    elif (event == sg.WIN_CLOSED or event == 'Analysis') and results == 1 and analysis == 0:
        analysis = 1
        print('\nVote 1 : ', v11,'  Binary Conversion m1 =>',v1,'  PK encryption(',v1,') c1 => ',c1)
        print('Vote 2 : ', v22,'  Binary Conversion m2 =>',v2,'  PK encryption(',v2,') c2 => ',c2)
        print('Vote 3 : ', v33,'  Binary Conversion m3 =>',v3,'  PK encryption(',v3,') c3 => ',c3)
        print("\nVote Counting : Computing on Encrypted Data")
        print('Encrypted Result C = c1 x c2 x c3  mod n^2=> ', cc)
        print('\nDecrypted election result : ',ans)
        print('Votes for Biden\t\t=> Decrypt(C) = ',ans)
        print('Votes for Trump\t\t=> Decrypt(C) = ',3-ans)
        break

while True:
    event, values = window.read()
    print('\n\nEletion has ended, Time to Exit ...')

#end
#window.close()