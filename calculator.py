#!/usr/bin/env python

import sys
import calendar
import time
import math

from PySide.QtGui import *
from PySide.QtCore import *


class Calculator(QWidget):

    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)
        self.createLayoutAndWidget()
        self.createConnection()

    def calculateHeadAndTailMonth(self):
        total = 0
        headDays = self.beginDate.date().daysInMonth() - self.beginDate.date().day() + 1
        tailDays = self.endDate.date().day()

        headRate = float(headDays) / self.beginDate.date().daysInMonth()
        tailRate = float(tailDays) / self.endDate.date().daysInMonth()

        base = int(self.base.text())
        total = (headRate + tailRate) * base
        
        self.headDays.setText(str(headDays))
        self.tailDays.setText(str(tailDays))
        return total
    
    def calculate(self):
        total = 0
        beginYear = self.beginDate.date().year()
        endYear = self.endDate.date().year()
        if beginYear == endYear:
            if self.beginDate.date().month() == self.endDate.date().month():
                days = self.beginDate.date().daysTo(self.endDate.date()) + 1
                rate = float(days) / self.beginDate.date().daysInMonth()
                base = int(self.base.text())
                total = rate * base
                self.headDays.setText("")
                self.tailDays.setText("")
            elif self.endDate.date().month() - self.beginDate.date().month() > 1:
                wholeMonths = []
                prevMonth = self.beginDate.date().month() + 1
                curMonth = self.endDate.date().month()
                for month in range(prevMonth, curMonth):
                    wholeMonths.append(month)
                total = len(wholeMonths) * int(self.base.text()) + self.calculateHeadAndTailMonth() 
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

    def addWidgetToLayout(self):
        self.v1.addWidget(self.beginDateLabel)
        self.v1.addWidget(self.beginDate)
        self.v1.addWidget(self.endDateLabel)
        self.v1.addWidget(self.endDate)
        self.v1.addWidget(self.baseLabel)
        self.v1.addWidget(self.base)
        
        self.h1.addWidget(self.resultLabel)
        self.h1.addWidget(self.headDaysLabel)
        self.h1.addWidget(self.tailDaysLabel)
        self.h2.addWidget(self.result)
        self.h2.addWidget(self.headDays)
        self.h2.addWidget(self.tailDays)

        self.v1.addLayout(self.h1)
        self.v1.addLayout(self.h2)
        
        self.v1.addWidget(self.resetButton)
        self.v1.addWidget(self.quitButton)

        self.layout = QVBoxLayout(self)
        self.layout.addLayout(self.v1)        
        self.setLayout(self.layout)

    def createLayoutAndWidget(self):

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
        self.base = QLineEdit("1")
        self.baseLabel.setBuddy(self.base)
         
        self.resetButton = QPushButton("&Reset")
        self.quitButton = QPushButton("&Quit")
        
        self.resultLabel = QLabel("Result:   ")
        self.result = QLabel("$0.0")
        self.resultLabel.setBuddy(self.result)

        self.headDays = QLabel("0")
        self.headDaysLabel = QLabel("Head days:")
        self.headDaysLabel.setBuddy(self.headDays)
        
        self.tailDays = QLabel("0")
        self.tailDaysLabel = QLabel("Tail days:")
        self.tailDaysLabel.setBuddy(self.tailDays)

        self.v1 = QVBoxLayout()
        self.h1 = QHBoxLayout()
        self.h2 = QHBoxLayout()
        self.addWidgetToLayout() 
	
    def createConnection(self):
        self.beginDate.dateChanged.connect(self.calculate)
        self.endDate.dateChanged.connect(self.calculate)
        self.base.textChanged.connect(self.calculate)
        self.resetButton.clicked.connect(self.resetAll)
        self.quitButton.clicked.connect(self.close)
        
