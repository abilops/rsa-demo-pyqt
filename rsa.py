'''************************************************************
Name       : RSA Calculations Demonstration
Description: A graphical programme that demonstrates the
                working of the RSA cryptosystem in crude way
Author     : Aadi B.
Date       : 25 Dec 2018
Files      : rsa.py => Contains all mathematics code
                and GUI connections
             signals.py => All GUI constructers
             primes.txt => List of primes upto 10,000
             primes.py  => Returns ints from primes.txt as a set
************************************************************'''
#import numpy as np
import string
import math
# Signal.py contains all GUI code
from signals import *

# Returns Euler's Totient function of primes p & q
def phi(p, q):
    return (p-1)*(q-1)

# Assuming p is odd, which it almost always has to be
def modEx(n, p, N):
    c = 1
    i = 0
    while i < p:
        c = (n * c) % N
        i += 1
    return c

def encrypt(set_m, N, e):
    c = [modEx(num,e,N) for num in set_m]
    return c

def decrypt(set_c, N, d):
    return encrypt(set_c, N, d)

# finds solution for ed = 1 mod Phi
def modInv(e, Phi):
    m,n = eEA(e,Phi)
    while m < 0 or n > 0:
        m += Phi
        n -= e
    return m


# To find Bezout's integers m & n to satisfy mx + ny = 1
def eEA(x,y):
    (q1,r1) = divmod(x,y)
    if r1 > 1:
        (m, n) = eEA(y, r1)
        return (n, m - q1*n)
    elif r1 == 1:
        return  (1, -q1)
    elif r1 == 0:
        print("If mx+ny=1, GCD|RHS => GCD|LHS=>GCD must be 1. Is it?")
        return 0,0

# Set of integers to string of hyphen-delimited integers
def setToNums(set_a):
    if len(set_a) == 0:
        return '0'
    s = str(set_a[0])
    for i in set_a[1:]:
        s += '-' + str(i)
    return s

# Alphanumeric sentence to set of integers (ASCII)
def strToSet(s):
    return [int.from_bytes(char.encode(), 'big') for char in s]

def inputDone():
    encodedEdit.setText(str(setToNums(strToSet(inputEdit.toPlainText()))))

class constants:
    N = 1574449
    Phi = 1571940
    e = 7
    d = 224563
C = constants()

def updateConstants():
    C.p, C.q, C.e = getValues()
    C.N = C.p*C.q
    C.Phi = phi(C.p,C.q)
    C.d = modInv(C.e, C.Phi)
    if C.d == 0:
        C.d = "Change e"
        encButton.setEnabled(False)
        decButton.setEnabled(False)
    else:
        encButton.setEnabled(True)
        decButton.setEnabled(True)
    bits = countBits(C.N)
    NLabel.setText("N = " + str(C.N) + "(" + str(bits) + " bits)")
    PhiLabel.setText("φ = "+ str(C.Phi))
    DLabel.setText("d = "+ str(C.d))
    encButton.setDefault(True)

def getValues():
    p = int(pEdit.currentText())
    q = int(qEdit.currentText())
    e = int(eEdit.currentText())
    return (p,q,e)    

# Ignore inputs that would crash the program
def clean_str(dirty):
    clean = ''
    for char in dirty:
        if char == '-' or char in '0123456789':
            clean += char
    if clean[-1] == '-':
        clean = clean[:-1]
    return clean

def encPressed():
    eE = encodedEdit.toPlainText()
    if len(eE) == 0:
        return
    clean_eE = clean_str(eE)
    set_m = [int(num) for num in clean_eE.split('-')]
    set_c = encrypt(set_m, C.N, C.e)
    str_c = setToNums(set_c)
    cipherEdit.setText(str_c)
#    decCipherEdit.setText(bytes(set_c).decode())
    decButton.setDefault(True)
    encButton.setDefault(False)
    decButton.setFocus()

def decPressed():
    decButton.setText("Loading")
    cE = cipherEdit.toPlainText()
    if len(cE) == 0:
        return
    clean_cE = clean_str(cE)
    set_c = [int(num) for num in clean_cE.split('-')]
    set_m = decrypt(set_c, C.N, C.d)
    str_m = setToNums(set_m)
    decodedEdit.setText(str_m)
    try:
        outputEdit.setText(bytes(set_m).decode())
    except ValueError as e:
        outputEdit.setText('?')
    decButton.setText("Decrypt with public key (N,d)")

def reset():
    pEdit.setCurrentIndex(200)
    qEdit.setCurrentIndex(205)
    eEdit.setCurrentIndex(10)
    inputEdit.setText("")
#    encodedEdit.setText('')
    cipherEdit.setText('')
    outputEdit.setText('')
    decodedEdit.setText('')
    inputEdit.setFocus()

def countBits(N):
    return math.ceil(math.log2(N))

pEdit.currentIndexChanged.connect(updateConstants)
qEdit.currentIndexChanged.connect(updateConstants)
eEdit.currentIndexChanged.connect(updateConstants)
inputEdit.textChanged.connect(inputDone)
encButton.clicked.connect(encPressed)
decButton.clicked.connect(decPressed)
resetButton.clicked.connect(reset)

window.show()
app.exec_()
