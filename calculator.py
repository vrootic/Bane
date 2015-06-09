#!/usr/bin/env python

import sys
import calendar
import time
import math

from PyQt4.QtGui import *
from PyQt4.QtCore import *


class Calculator(QWidget):

    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)
        self.createLayout()
        self.createConnection()

    def calculate(self):
        total = 0
        if self.beginDate.date().month() == self.endDate.date().month():
            days = self.beginDate.date().daysTo(self.endDate.date())
            rate = float(days) / self.beginDate.date().daysInMonth()
            base = self.base.value()
            total = rate * base
        else:
            prevDays = self.beginDate.date().daysInMonth() - self.beginDate.date().day() + 1
            curDays = self.endDate.date().day()

            prevRate = float(prevDays) / self.beginDate.date().daysInMonth()
            curRate = float(curDays) / self.endDate.date().daysInMonth()
            
            base = self.base.value()
            total = (prevRate + curRate) * base

        self.result.setText(str(total))
    
    def createLayout(self):

        self.beginDate = QDateEdit(self) 
        self.beginDate.setDateTime(QDateTime.currentDateTime())
        self.beginDate.setDisplayFormat("yyyy/MM/dd")
        self.beginDate.setCalendarPopup(True)
        
        self.endDate = QDateEdit(self)
        self.endDate.setDateTime(QDateTime.currentDateTime())
        self.endDate.setDisplayFormat("yyyy/MM/dd")
        self.endDate.setCalendarPopup(True)
        
        self.beginDateLabel = QLabel("&Begin Date:")
        self.beginDateLabel.setBuddy(self.beginDate)
        
        self.endDateLabel = QLabel("&End Date:")
        self.endDateLabel.setBuddy(self.beginDate)
        
        self.baseLabel = QLabel("Base")
        self.base = QSpinBox()
        self.base.setRange(1, 20000)
        self.baseLabel.setBuddy(self.base)
        
        self.quitButton = QPushButton("&Quit")
        
        self.resultLabel = QLabel("Result:")
        self.result = QLabel("$")

        v1 = QVBoxLayout()
        v1.addWidget(self.beginDateLabel)
        v1.addWidget(self.beginDate)
        v1.addWidget(self.endDateLabel)
        v1.addWidget(self.endDate)
        v1.addWidget(self.baseLabel)
        v1.addWidget(self.base)
        v1.addWidget(self.resultLabel)
        v1.addWidget(self.result)
        v1.addWidget(self.quitButton)
        v1.addStretch(1)
        
        layout = QVBoxLayout(self)
        layout.addLayout(v1)
        
        self.setLayout(layout)
        self.resize(300, 300)
	
    def createConnection(self):
        self.beginDate.dateChanged.connect(self.calculate)
        self.endDate.dateChanged.connect(self.calculate)
        self.base.valueChanged.connect(self.calculate)
        self.quitButton.clicked.connect(self.close)
        

app = QApplication(sys.argv)

calculator = Calculator()
calculator.show()

app.exec_()
