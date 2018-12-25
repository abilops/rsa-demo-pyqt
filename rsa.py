import numpy as np
from signals import *

def phi(p, q):
    return (p-1)*(q-1)
# Assuming p is odd, which it almost always has to be
def modEx(n, p, N):
    c = 1
    i = 0
    while i < p:
        c = (n * c) % N
        i += 1
    '''
    ans = (n**p) % N
    if ans != c:
        print('MODEX NOT WORKING')
    '''
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
# em + nPhi = 1. So e(-m) = 1 mod phi.
    return m


# To find Bezout's integers to satisfy mx + ny = 1
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

def setToNums(set_a):
    if len(set_a) == 0:
        return '0'
    s = str(set_a[0])
    for i in set_a[1:]:
        s += '-' + str(i)
    return s

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
    NLabel.setText("N = " + str(C.N))
    PhiLabel.setText("φ = "+ str(C.Phi))
    DLabel.setText("d = "+ str(C.d))
    encButton.setDefault(True)

def getValues():
    p = int(pEdit.currentText())
    q = int(qEdit.currentText())
    e = int(eEdit.currentText())
    return (p,q,e)    

def encPressed():
    eE = encodedEdit.toPlainText()
    if len(eE) == 0 or '-' not in eE:
        return
    set_m = [int(num) for num in eE.split('-')]
    set_c = encrypt(set_m, C.N, C.e)
    str_c = setToNums(set_c)
    cipherEdit.setText(str_c)
    decButton.setDefault(True)
    encButton.setDefault(False)
    decButton.setFocus()

def decPressed():
    decButton.setText("Loading")
    cE = cipherEdit.toPlainText()
    if len(cE) == 0 or '-' not in cE:
        return
    set_c = [int(num) for num in cE.split('-')]
    set_m = decrypt(set_c, C.N, C.d)
    str_m = setToNums(set_m)
    decodedEdit.setText(str_m)
    outputEdit.setText(bytes(set_m).decode())
    decButton.setText("Decrypt with public key (N,d)")

pEdit.currentIndexChanged.connect(updateConstants)
qEdit.currentIndexChanged.connect(updateConstants)
eEdit.currentIndexChanged.connect(updateConstants)
inputEdit.textChanged.connect(inputDone)
encButton.clicked.connect(encPressed)
decButton.clicked.connect(decPressed)

window.show()
app.exec_()
'''
p = int(input("P"))
if p == 0: p = 48611
q = int(input("Q"))
if q == 0: q = 37813
N = p*q
phi = (p-1)*(q-1)
print("PHI "+str(phi))
# E should be coprime to PHI because ed = 1 mod phi
e = int(input("E"))
if e == 0: e = 1987
while (e > phi and e < 1):
    print("1 < E < Phi. Try again")
    e = int(input('E'))
d = modInv(e, phi)
print("D"+str(d))
str_m = input("M")
set_m = strToSet(str_m)
print(set_m)
nums_m = setToNums(set_m)
print(nums_m)
set_c = encrypt(set_m, N, e)
print(set_c)
nums_c = setToNums(set_c)

nums_c = str(set_c[0])
for i in set_c[1:]:
    nums_c += '-' + str(i)

print(nums_c)
set_m = decrypt(set_c, N, d)
print(set_m)
nums_m = setToNums(set_m)
print(nums_m)
'''
