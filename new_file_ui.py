# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\arssa\Projects\Sport\Sport-Oracle\new_file.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(442, 181)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 421, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.Text_Edit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.Text_Edit.setMaximumSize(QtCore.QSize(16777215, 34))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Text_Edit.setFont(font)
        self.Text_Edit.setObjectName("Text_Edit")
        self.verticalLayout.addWidget(self.Text_Edit)
        self.Error_Text = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Error_Text.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Error_Text.setText("")
        self.Error_Text.setObjectName("Error_Text")
        self.verticalLayout.addWidget(self.Error_Text)
        self.Buttons = QtWidgets.QDialogButtonBox(self.verticalLayoutWidget)
        self.Buttons.setOrientation(QtCore.Qt.Horizontal)
        self.Buttons.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.Buttons.setObjectName("Buttons")
        self.verticalLayout.addWidget(self.Buttons)

        self.retranslateUi(Dialog)
        self.Buttons.accepted.connect(Dialog.accept) # type: ignore
        self.Buttons.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Введите название для создания нового файла"))