import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from calculator import Calculator


app = QApplication(sys.argv)
layout = QHBoxLayout()
spinBox = QLineEdit()
result = QLabel("$")
ylayout = QVBoxLayout()
ylayout.addWidget(result)
spinBox.resize(200, 50)
addBtn = QPushButton("&Add")
layout.addWidget(spinBox)
layout.addWidget(addBtn)
ylayout.addLayout(layout)

def adder():
    tmp = spinBox.selectedText()
    print tmp
    #tmp = tmp + 1
    result.setText(str(tmp))

addBtn.clicked.connect(adder)
#layout.addStretch(1)


widget = QWidget()
widget.setLayout(ylayout)
widget.show()
#calculator = Calculator()
#layout.addWidget(calculator)
#calculator.show()

if __name__ == '__main__':
    sys.exit(app.exec_())
