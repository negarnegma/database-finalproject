# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_grafic.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(795, 672)
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(70, 59, 641, 581))
        self.stackedWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.textEdit = QtWidgets.QTextEdit(self.page)
        self.textEdit.setGeometry(QtCore.QRect(110, 110, 231, 41))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(420, 120, 121, 20))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(270, 260, 93, 28))
        self.pushButton.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(self.page)
        self.listWidget.setGeometry(QtCore.QRect(160, 370, 281, 141))
        self.listWidget.setObjectName("listWidget")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "نام خود را وارد کنید:"))
        self.pushButton.setText(_translate("Form", "sabt"))



