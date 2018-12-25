from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from primes import primes
app = QApplication([])
window = QWidget()
inlayout = QHBoxLayout()
outlayout = QHBoxLayout()
oplayout = QVBoxLayout()
paramsLayout = QGridLayout()
inputEdit = QTextEdit('Welcome')
inputEdit.setTabChangesFocus(True)

encodedEdit = QTextEdit('87-101-108-99-111-109-101')
encodedEdit.setTabChangesFocus(True)

encButton = QPushButton('&Encrypt with public key (N,e)')
#encButton.setFlat(True)
encButton.setAutoDefault(True)
cipherEdit = QTextEdit('Ciphertext')

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

pLabel = QLabel("Value of &P:")
pLabel.setBuddy(pEdit)
qLabel = QLabel("Value of &Q:")
qLabel.setBuddy(qEdit)
eLabel = QLabel("Value of &e:")
eLabel.setBuddy(eEdit)

paramsLayout.addWidget(pLabel, 0,0)
paramsLayout.addWidget(qLabel, 1,0)
paramsLayout.addWidget(eLabel, 2,0)
NLabel = QLabel("N = 1574449")
PhiLabel = QLabel("φ = 1571940")
DLabel = QLabel("d = 224563")

autoButton = QPushButton("&Autoset")
paramsLayout.addWidget(pEdit, 0,1)
paramsLayout.addWidget(qEdit, 1,1)
paramsLayout.addWidget(eEdit, 2, 1,)

paramsLayout.addWidget(NLabel, 0,2, QtCore.Qt.AlignRight)
paramsLayout.addWidget(PhiLabel, 1,2, QtCore.Qt.AlignRight)
paramsLayout.addWidget(DLabel, 2,2, QtCore.Qt.AlignRight)
paramsLayout.addWidget(autoButton, 0,3, 3, 1,QtCore.Qt.AlignCenter)
inlayout.addWidget(inputEdit)
inlayout.addWidget(encodedEdit)

outlayout.addWidget(decodedEdit)
outlayout.addWidget(outputEdit)
oplayout.addLayout(paramsLayout)
oplayout.addLayout(inlayout)
oplayout.addWidget(encButton)
oplayout.addWidget(cipherEdit)
oplayout.addWidget(decButton)
oplayout.addLayout(outlayout)

window.setLayout(oplayout)
window.setWindowTitle("RSA Demo")

#pEdit.currentIndexChanged.connect(limitEtoPhi)
#qEdit.currentIndexChanged.connect(limitEtoPhi)


