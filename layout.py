# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(733, 478)
        self.gridLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 731, 471))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 1)
        self.salami = QtWidgets.QCheckBox(parent=self.gridLayoutWidget)
        self.salami.setObjectName("salami")
        self.gridLayout.addWidget(self.salami, 2, 2, 1, 1)
        self.normal = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.normal.setObjectName("normal")
        self.gridLayout.addWidget(self.normal, 0, 1, 1, 1)
        self.big = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.big.setObjectName("big")
        self.gridLayout.addWidget(self.big, 0, 2, 1, 1)
        self.small = QtWidgets.QRadioButton(parent=self.gridLayoutWidget)
        self.small.setObjectName("small")
        self.gridLayout.addWidget(self.small, 0, 0, 1, 1)
        self.double_2 = QtWidgets.QCheckBox(parent=self.gridLayoutWidget)
        self.double_2.setObjectName("double_2")
        self.gridLayout.addWidget(self.double_2, 3, 2, 1, 1)
        self.mushroom = QtWidgets.QCheckBox(parent=self.gridLayoutWidget)
        self.mushroom.setObjectName("mushroom")
        self.gridLayout.addWidget(self.mushroom, 1, 2, 1, 1)
        self.pineapple = QtWidgets.QCheckBox(parent=self.gridLayoutWidget)
        self.pineapple.setObjectName("pineapple")
        self.gridLayout.addWidget(self.pineapple, 4, 2, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 4, 2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem1, 5, 2, 1, 1)
        self.orderButton = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.orderButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.orderButton.setObjectName("orderButton")
        self.gridLayout.addWidget(self.orderButton, 5, 1, 1, 1)
        self.result = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.result.setMaximumSize(QtCore.QSize(16777215, 50))
        self.result.setText("")
        self.result.setObjectName("result")
        self.gridLayout.addWidget(self.result, 6, 0, 1, 3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.salami.setText(_translate("Dialog", "Salami"))
        self.normal.setText(_translate("Dialog", "Pizza normalna"))
        self.big.setText(_translate("Dialog", "Pizza duża"))
        self.small.setText(_translate("Dialog", "Pizza mała"))
        self.double_2.setText(_translate("Dialog", "Podwójny syr"))
        self.mushroom.setText(_translate("Dialog", "Pieczarka"))
        self.pineapple.setText(_translate("Dialog", "Ananas"))
        self.label.setText(_translate("Dialog", "Wybierz dodatki"))
        self.orderButton.setText(_translate("Dialog", "Zamów"))
