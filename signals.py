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
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from primes import primes
app = QApplication([])
window = QWidget()
# parameters area
paramsLayout = QGridLayout()
# for parameters
formLayout = QFormLayout()
# input (cleartext) area
inlayout = QHBoxLayout()
# ciphertext area
ciplayout = QHBoxLayout()
# decrypted (cleartext)  area
outlayout = QHBoxLayout()
# final layout
oplayout = QVBoxLayout()

inputEdit = QTextEdit('Welcome')
inputEdit.setTabChangesFocus(True)

encodedEdit = QTextEdit('87-101-108-99-111-109-101')
encodedEdit.setTabChangesFocus(True)

encButton = QPushButton('&Encrypt with public key (N,e)')
#encButton.setFlat(True)
encButton.setAutoDefault(True)
cipherEdit = QTextEdit('Ciphertext')
decCipherEdit = QTextEdit('Decoded Ciphertext')
decButton = QPushButton('&Decrypt with private key (N,d)')
#decButton.setFlat(True)
decodedEdit = QTextEdit('Decoded')
outputEdit = QTextEdit('Output')

pEdit = QComboBox()
pEdit.setCurrentText("343")
pEdit.addItems(primes)
pEdit.setEditable(True)
pEdit.setCurrentIndex(200)
qEdit = QComboBox()
qEdit.setCurrentText('711')
qEdit.addItems(primes)
qEdit.setEditable(True)
qEdit.setCurrentIndex(205)

eEdit = QComboBox()
eEdit.setCurrentText('5')
eEdit.addItems(primes[:200])
eEdit.setCurrentIndex(10)

pLabel = QLabel("Value of &P :")
pLabel.setBuddy(pEdit)
qLabel = QLabel("Value of &Q :")
qLabel.setBuddy(qEdit)
eLabel = QLabel("Value of &e :")
eLabel.setBuddy(eEdit)

NLabel = QLabel("N = 1574449(21 bits)")
PhiLabel = QLabel("φ = 1571940")
DLabel = QLabel("d = 224563")

resetButton = QPushButton("&Reset")

formLayout.addRow(pLabel, pEdit)
formLayout.addRow(qLabel, qEdit)
formLayout.addRow(eLabel, eEdit)

paramsLayout.addLayout(formLayout, 0,0, 3,1)
paramsLayout.addWidget(NLabel, 0,2, QtCore.Qt.AlignCenter)
paramsLayout.addWidget(PhiLabel, 1,2, QtCore.Qt.AlignCenter)
paramsLayout.addWidget(DLabel, 2,2, QtCore.Qt.AlignCenter)
paramsLayout.addWidget(resetButton, 0,3, 3, 1,QtCore.Qt.AlignCenter)

inlayout.addWidget(inputEdit)
inlayout.addWidget(encodedEdit)
ciplayout.addWidget(cipherEdit)
#ciplayout.addWidget(decCipherEdit)
outlayout.addWidget(decodedEdit)
outlayout.addWidget(outputEdit)

oplayout.addLayout(paramsLayout)
oplayout.addLayout(inlayout)
oplayout.addWidget(encButton)
oplayout.addLayout(ciplayout)
oplayout.addWidget(decButton)
oplayout.addLayout(outlayout)

window.setLayout(oplayout)
window.setWindowTitle("RSA Demo")
