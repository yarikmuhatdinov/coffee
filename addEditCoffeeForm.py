# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addEditCoffeeForm(object):
    def setupUi(self, addEditCoffeeForm):
        addEditCoffeeForm.setObjectName("addEditCoffeeForm")
        addEditCoffeeForm.resize(621, 394)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(addEditCoffeeForm.sizePolicy().hasHeightForWidth())
        addEditCoffeeForm.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(addEditCoffeeForm)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(addEditCoffeeForm)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.spinBox = QtWidgets.QSpinBox(addEditCoffeeForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(999999999)
        self.spinBox.setProperty("value", 1)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 0, 1, 1, 1)
        self.pushButtonEdit = QtWidgets.QPushButton(addEditCoffeeForm)
        self.pushButtonEdit.setObjectName("pushButtonEdit")
        self.gridLayout.addWidget(self.pushButtonEdit, 2, 1, 1, 1)
        self.pushButtonAdd = QtWidgets.QPushButton(addEditCoffeeForm)
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.gridLayout.addWidget(self.pushButtonAdd, 0, 2, 1, 1)
        self.pushButtonSave = QtWidgets.QPushButton(addEditCoffeeForm)
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.gridLayout.addWidget(self.pushButtonSave, 2, 2, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(addEditCoffeeForm)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.gridLayout.addWidget(self.tableWidget, 5, 0, 1, 3)
        self.label_info = QtWidgets.QLabel(addEditCoffeeForm)
        font = QtGui.QFont()
        font.setKerning(True)
        self.label_info.setFont(font)
        self.label_info.setText("")
        self.label_info.setAlignment(QtCore.Qt.AlignCenter)
        self.label_info.setObjectName("label_info")
        self.gridLayout.addWidget(self.label_info, 2, 0, 1, 1)

        self.retranslateUi(addEditCoffeeForm)
        QtCore.QMetaObject.connectSlotsByName(addEditCoffeeForm)

    def retranslateUi(self, addEditCoffeeForm):
        _translate = QtCore.QCoreApplication.translate
        addEditCoffeeForm.setWindowTitle(_translate("addEditCoffeeForm", "????????????????, ??????????????????????????"))
        self.label.setText(_translate("addEditCoffeeForm", "?????????????? ID ????????????"))
        self.pushButtonEdit.setText(_translate("addEditCoffeeForm", "?????????????????????????? ????????????"))
        self.pushButtonAdd.setText(_translate("addEditCoffeeForm", "???????????????? ????????????"))
        self.pushButtonSave.setText(_translate("addEditCoffeeForm", "?????????????????? ????????????????????"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("addEditCoffeeForm", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("addEditCoffeeForm", "???????????????? ??????????"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("addEditCoffeeForm", "?????????????? ??????????????"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("addEditCoffeeForm", "??????????????/?? ????????????"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("addEditCoffeeForm", "???????????????? ??????????"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("addEditCoffeeForm", "????????"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("addEditCoffeeForm", "?????????? ????????????????"))
