import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from calculator import Calculator


app = QApplication(sys.argv)
layout = QHBoxLayout()
calculator = Calculator()
layout.addWidget(calculator)
calculator.show()

if __name__ == '__main__':
    sys.exit(app.exec_())
