# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 60, 879, 3))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 371, 31))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 470, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 80, 300, 37))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(150, 280, 104, 26))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.setItemText(0, "")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 160, 255, 31))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(20, 240, 264, 31))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.widget1)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget1)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(0, "")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_2)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(20, 340, 263, 66))
        self.widget2.setObjectName("widget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_9 = QtWidgets.QLabel(self.widget2)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.widget2)
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.horizontalLayout_3.addWidget(self.dateTimeEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_8 = QtWidgets.QLabel(self.widget2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.widget2)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.horizontalLayout_2.addWidget(self.dateTimeEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt;\">风电/光伏发电功率超短期预测模块</span></p><p><br/></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "开始导入"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">动态数据导入地址：</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "打开文件夹"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "温度"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "风速"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">电站</span></p></body></html>"))
        self.comboBox.setItemText(1, _translate("MainWindow", "风电"))
        self.comboBox.setItemText(2, _translate("MainWindow", "光伏"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">导入数据类型：</span></p></body></html>"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "功率"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "数值天气预报"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">开始时间：</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">截止时间：</span></p></body></html>"))

