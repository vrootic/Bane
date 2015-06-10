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

        base = self.base.text().toInt()[0]
        total = (headRate + tailRate) * base

        return total
    
    def calculate(self):
        total = 0
        beginYear = self.beginDate.date().year()
        endYear = self.endDate.date().year()
        if beginYear == endYear:
            if self.beginDate.date().month() == self.endDate.date().month():
                days = self.beginDate.date().daysTo(self.endDate.date()) + 1
                rate = float(days) / self.beginDate.date().daysInMonth()
                base = self.base.text().toInt()[0]
                total = rate * base
            elif self.endDate.date().month() - self.beginDate.date().month() > 1:
                wholeMonths = []
                prevMonth = self.beginDate.date().month() + 1
                curMonth = self.endDate.date().month()
                for month in range(prevMonth, curMonth):
                    wholeMonths.append(month)
                total = len(wholeMonths) * self.base.text().toInt()[0] + self.calculateHeadAndTailMonth() 
            else:
                total = self.calculateHeadAndTailMonth()
            
            self.result.setText("$" + str(total))
        else:
            self.result.setText("Different year.")

    def resetAll(self):
        self.beginDate.setDateTime(QDateTime.currentDateTime())
        self.endDate.setDateTime(QDateTime.currentDateTime())
        self.base.setText(str(1))
        self.calculate()

    def handleLayout(self):
        self.v1.addWidget(self.beginDateLabel)
        self.v1.addWidget(self.beginDate)
        self.v1.addWidget(self.endDateLabel)
        self.v1.addWidget(self.endDate)
        self.v1.addWidget(self.baseLabel)
        self.v1.addWidget(self.base)
        self.v1.addWidget(self.resultLabel)
        self.v1.addWidget(self.result)
        self.v1.addWidget(self.resetButton)
        self.v1.addWidget(self.quitButton)

        self.layout = QVBoxLayout(self)
        self.layout.addLayout(self.v1)        
        self.setLayout(self.layout)

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
        self.base = QLineEdit()
        self.baseLabel.setBuddy(self.base)
         
        self.resetButton = QPushButton("&Reset")
        self.quitButton = QPushButton("&Quit")
        
        self.resultLabel = QLabel("Result:")
        self.result = QLabel("$0.0")

        self.v1 = QVBoxLayout()
        self.handleLayout() 
	
    def createConnection(self):
        self.beginDate.dateChanged.connect(self.calculate)
        self.endDate.dateChanged.connect(self.calculate)
        self.base.textChanged.connect(self.calculate)
        self.resetButton.clicked.connect(self.resetAll)
        self.quitButton.clicked.connect(self.close)
        
