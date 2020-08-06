# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Dmitry\PycharmProjects\pythonProject\venv\te\design.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(303, 364)
        MainWindow.setStyleSheet("background-color: gray;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 90, 281, 251))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton2.setStyleSheet("background-color: green;")
        self.pushButton2.setObjectName("pushButton2")
        self.gridLayout.addWidget(self.pushButton2, 0, 1, 1, 1)
        self.pushButton7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton7.setStyleSheet("background-color: green;")
        self.pushButton7.setObjectName("pushButton7")
        self.gridLayout.addWidget(self.pushButton7, 2, 0, 1, 1)
        self.pushButton9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton9.setStyleSheet("background-color: green;")
        self.pushButton9.setObjectName("pushButton9")
        self.gridLayout.addWidget(self.pushButton9, 2, 2, 1, 1)
        self.pushButton8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton8.setStyleSheet("background-color: green;")
        self.pushButton8.setObjectName("pushButton8")
        self.gridLayout.addWidget(self.pushButton8, 2, 1, 1, 1)
        self.pushButton5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton5.setStyleSheet("background-color: green;")
        self.pushButton5.setObjectName("pushButton5")
        self.gridLayout.addWidget(self.pushButton5, 1, 1, 1, 1)
        self.pushButton4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton4.setStyleSheet("background-color: green;")
        self.pushButton4.setObjectName("pushButton4")
        self.gridLayout.addWidget(self.pushButton4, 1, 0, 1, 1)
        self.pushButton6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton6.setStyleSheet("background-color: green;")
        self.pushButton6.setObjectName("pushButton6")
        self.gridLayout.addWidget(self.pushButton6, 1, 2, 1, 1)
        self.pushButton0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton0.setStyleSheet("background-color: green;")
        self.pushButton0.setObjectName("pushButton0")
        self.gridLayout.addWidget(self.pushButton0, 3, 1, 1, 1)
        self.pushButton3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton3.setStyleSheet("background-color: green;")
        self.pushButton3.setObjectName("pushButton3")
        self.gridLayout.addWidget(self.pushButton3, 0, 2, 1, 1)
        self.pushButton1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton1.setStyleSheet("background-color: green;")
        self.pushButton1.setObjectName("pushButton1")
        self.gridLayout.addWidget(self.pushButton1, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 281, 51))
        self.lineEdit.setStyleSheet("background-color: white;\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton2.setText(_translate("MainWindow", "2"))
        self.pushButton7.setText(_translate("MainWindow", "7"))
        self.pushButton9.setText(_translate("MainWindow", "9"))
        self.pushButton8.setText(_translate("MainWindow", "8"))
        self.pushButton5.setText(_translate("MainWindow", "5"))
        self.pushButton4.setText(_translate("MainWindow", "4"))
        self.pushButton6.setText(_translate("MainWindow", "6"))
        self.pushButton0.setText(_translate("MainWindow", "0"))
        self.pushButton3.setText(_translate("MainWindow", "3"))
        self.pushButton1.setText(_translate("MainWindow", "1"))
