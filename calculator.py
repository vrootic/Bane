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

    def calculateHeadAndTailMonth(self):
        total = 0
        headDays = self.beginDate.date().daysInMonth() - self.beginDate.date().day() + 1
        tailDays = self.endDate.date().day()

        headRate = float(headDays) / self.beginDate.date().daysInMonth()
        tailRate = float(tailDays) / self.endDate.date().daysInMonth()

        base = self.base.value()
        total = (headRate + tailRate) * base

        return total
    
    def calculate(self):
        total = 0
        beginYear = self.beginDate.date().year()
        endYear = self.endDate.date().year()
        if beginYear == endYear:
            if self.beginDate.date().month() == self.endDate.date().month():
                days = self.beginDate.date().daysTo(self.endDate.date())
                rate = float(days) / self.beginDate.date().daysInMonth()
                base = self.base.value()
                total = rate * base
            elif self.endDate.date().month() - self.beginDate.date().month() > 1:
                wholeMonths = []
                prevMonth = self.beginDate.date().month() + 1
                curMonth = self.endDate.date().month()
                for month in range(prevMonth, curMonth):
                    wholeMonths.append(month)
                total = len(wholeMonths) * self.base.value() + self.calculateHeadAndTailMonth() 
            else:
                total = self.calculateHeadAndTailMonth()
            
            self.result.setText(str(total))
        else:
            self.result.setText("Different year.")

    
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
