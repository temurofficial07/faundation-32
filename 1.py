#1

'''
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtWidgets import QLabel,QLineEdit,QPushButton
from PyQt5.QtGui import QFont
import sys

app=QApplication(sys.argv)

oyna=QWidget()
oyna.setWindowTitle("1 - MISOL ")
oyna.setGeometry(300, 300, 500, 300)

yozuv=QLabel("Aslonboyev",oyna)
yozuv.move(80, 10)
yozuv.setFont(QFont("Times",25))

yozuv1 = QLabel("Temur",oyna)
yozuv1.move(80, 45)
yozuv1.setFont(QFont("Times", 25))

yozuv2 = QLabel("Ashurboyevich", oyna)
yozuv2.move(80, 80)
yozuv2.setFont(QFont("Times", 25))
yozuv2.clear()
oyna.show()
sys.exit(app.exec_())

'''

#2

'''
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtWidgets import QLabel,QLineEdit,QPushButton
from PyQt5.QtGui import QFont
import sys


def Ism():
    yozuv.setText("Temur")    
    yozuv.adjustSize()

def Fam():
    yozuv.setText("Aslonboyev")
    yozuv.adjustSize()

def Sana():
    yozuv.setText("08.10.2003")    
    yozuv.adjustSize()

    
app=QApplication(sys.argv)

oyna = QWidget()
oyna.setWindowTitle("2 - MISOL")
oyna.setGeometry(300, 300, 500, 300)

yozuv = QLabel("", oyna)
yozuv.move(200, 50)
yozuv.setFont(QFont("Times", 20))

ism = QPushButton("ISM", oyna)
ism.move(200, 100)
ism.setFont(QFont("Times", 20))
ism.clicked.connect(Ism)

fam = QPushButton("FAMILIYA", oyna)
fam.move(200, 150)
fam.setFont(QFont("Times", 20))
fam.clicked.connect(Fam)

sana = QPushButton("SANA", oyna)
sana.move(200, 200)
sana.setFont(QFont("Times", 20))
sana.clicked.connect(Sana)

oyna.show()
sys.exit(app.exec_())
'''

#3


from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtWidgets import QLabel,QLineEdit,QPushButton
from PyQt5.QtGui import QFont
import sys

def Plus():
    yozuv.setText(str(int(son1.text()) + int(son2.text())))
    yozuv.adjustSize()
    
def Minus():
    yozuv.setText(str(int(son1.text()) - int(son2.text())))
    yozuv.adjustSize()
    
def Multipy():
    yozuv.setText(str(int(son1.text()) * int(son2.text())))
    yozuv.adjustSize()
    
def Devide():
    yozuv.setText(str(int(son1.text()) / int(son2.text())))
    yozuv.adjustSize()
    
def Percent():
    yozuv.setText(str(int(son1.text()) * int(son2.text()) / 100))
    yozuv.adjustSize()
    
def Degree():
    yozuv.setText(str(int(son1.text()) ** int(son2.text())))
    yozuv.adjustSize()
    
    
app = QApplication(sys.argv)
oyna = QWidget()
oyna.setWindowTitle("3 - MISOL")
oyna.setGeometry(300, 300, 600, 400)

yozuv = QLabel("", oyna)
yozuv.move(200, 50)
yozuv.setFont(QFont("Times", 20))

son1 = QLineEdit(oyna)
son1.move(20, 20)
son1.setFont(QFont("Times",12))

son2 = QLineEdit(oyna)
son2.move(20, 60)
son2.setFont(QFont("Times", 12))

plus = QPushButton(" + ", oyna)
plus.move(20, 100)
plus.setFont(QFont("Times", 10))
plus.clicked.connect(Plus)

minus = QPushButton(" - ", oyna)
minus.move(110, 100)
minus.setFont(QFont("Times", 10))
minus.clicked.connect(Minus)

multiply = QPushButton(" * ", oyna)
multiply.move(200, 100)
multiply.setFont(QFont("Times", 10))
multiply.clicked.connect(Multipy)

devide = QPushButton(" / ", oyna)
devide.move(20, 150)
devide.setFont(QFont("Times", 10))
devide.clicked.connect(Devide)

percent = QPushButton(" % ", oyna)
percent.move(110, 150)
percent.setFont(QFont("Times", 10))
percent.clicked.connect(Percent)

degree = QPushButton(" x^y ", oyna)
degree.move(200, 150)
degree.setFont(QFont("Times", 10))
degree.clicked.connect(Degree)

oyna.show()
sys.exit(app.exec_())










