# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowhgoygC.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtWidgets import (QLCDNumber, QProgressBar, QPushButton, QStatusBar,
                               QVBoxLayout, QWidget)
from application.gui.canvas import Canvas

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setFixedSize(340, 250)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.figure = Canvas(QRect(18, 15, 160, 200), parent=self.centralwidget)
        self.figure.setStyleSheet('background-color: grey;')
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(190, 10, 130, 210))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.lcdNumber = QLCDNumber(self.verticalLayoutWidget)
        self.lcdNumber.setObjectName(u"lcdNumber")

        self.verticalLayout.addWidget(self.lcdNumber)

        self.progressBar = QProgressBar(self.verticalLayoutWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.progressBar)

        self.processButton = QPushButton(self.verticalLayoutWidget)
        self.processButton.setObjectName(u"processButton")
        self.verticalLayout.addWidget(self.processButton)

        self.clearButton = QPushButton(self.verticalLayoutWidget)
        self.clearButton.setObjectName(u"clearButton")
        self.verticalLayout.addWidget(self.clearButton)

        self.saveButton = QPushButton(self.verticalLayoutWidget)
        self.saveButton.setObjectName(u"saveButton")
        self.verticalLayout.addWidget(self.saveButton)

        self.exitButton = QPushButton(self.verticalLayoutWidget)
        self.exitButton.setObjectName(u"exitButton")
        self.verticalLayout.addWidget(self.exitButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.processButton.setText(QCoreApplication.translate("MainWindow", u"Recognize", None))
        self.clearButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Save to...", None))
        self.exitButton.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

