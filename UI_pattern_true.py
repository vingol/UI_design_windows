# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_pattern.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
import base64
from images.cloud_corr_jpg import img as cloud_corr
from images.wind_corr_jpg import img as wind_corr
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

tmp = open('cloud_corr.jpg', 'wb')        #创建临时的文件
tmp.write(base64.b64decode(cloud_corr))    ##把这个one图片解码出来，写入文件中去。
tmp.close()

tmp = open('wind_corr.jpg', 'wb')        #创建临时的文件
tmp.write(base64.b64decode(wind_corr))    ##把这个one图片解码出来，写入文件中去。
tmp.close()

class Ui_MainWindow_pattern_true(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 0, 371, 31))
        self.label.setObjectName("label")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(50, 130, 401, 331))
        self.graphicsView.setMinimumSize(QtCore.QSize(401, 331))
        self.graphicsView.setMaximumSize(QtCore.QSize(401, 331))
        self.graphicsView.setObjectName("graphicsView")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 40, 879, 3))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.layoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(490, 160, 300, 31))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_18 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_14.addWidget(self.label_18)
        self.comboBox_4 = QtWidgets.QComboBox(self.layoutWidget_3)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.setItemText(0, "")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.horizontalLayout_14.addWidget(self.comboBox_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 200, 241, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(510, 310, 241, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.layoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_7.setGeometry(QtCore.QRect(490, 270, 300, 31))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.layoutWidget_7)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_21 = QtWidgets.QLabel(self.layoutWidget_7)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_18.addWidget(self.label_21)
        self.comboBox_5 = QtWidgets.QComboBox(self.layoutWidget_7)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.setItemText(0, "")
        self.comboBox_5.addItem("")
        self.horizontalLayout_18.addWidget(self.comboBox_5)
        self.layoutWidget_8 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_8.setGeometry(QtCore.QRect(490, 390, 300, 31))
        self.layoutWidget_8.setObjectName("layoutWidget_8")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.layoutWidget_8)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_22 = QtWidgets.QLabel(self.layoutWidget_8)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_19.addWidget(self.label_22)
        self.comboBox_6 = QtWidgets.QComboBox(self.layoutWidget_8)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.setItemText(0, "")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.horizontalLayout_19.addWidget(self.comboBox_6)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 60, 723, 29))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_17 = QtWidgets.QLabel(self.widget)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout.addWidget(self.label_17)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_19 = QtWidgets.QLabel(self.widget)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_16.addWidget(self.label_19)
        self.dateTimeEdit_7 = QtWidgets.QDateTimeEdit(QtCore.QDateTime(QtCore.QDate(2017, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateTimeEdit_7.setObjectName("dateTimeEdit_7")
        self.dateTimeEdit_7.setDisplayFormat("yyyy/MM/dd HH-mm-ss")
        self.horizontalLayout_16.addWidget(self.dateTimeEdit_7)
        self.horizontalLayout.addLayout(self.horizontalLayout_16)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_20 = QtWidgets.QLabel(self.widget)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_17.addWidget(self.label_20)
        self.dateTimeEdit_8 = QtWidgets.QDateTimeEdit(QtCore.QDateTime(QtCore.QDate(2017, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateTimeEdit_8.setObjectName("dateTimeEdit_8")
        self.dateTimeEdit_8.setDisplayFormat("yyyy/MM/dd HH-mm-ss")
        self.horizontalLayout_17.addWidget(self.dateTimeEdit_8)
        self.horizontalLayout.addLayout(self.horizontalLayout_17)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton_2.clicked.connect(self.slot_1)
        self.pushButton_3.clicked.connect(self.slot_2)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'等线\'; font-size:24pt; color:#000000;\">风/光电场关联模式识别</span></p><p><br/></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">选择功率预测方法：</span></p></body></html>"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "SVR"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "ELM"))
        self.pushButton_2.setText(_translate("MainWindow", "风电电站关联模式分析"))
        self.pushButton_3.setText(_translate("MainWindow", "光伏电站关联模式分析"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">选择云图预测方法：</span></p></body></html>"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "频域"))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">选择关联时间尺度：</span></p></body></html>"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "30min"))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "1h"))
        self.comboBox_6.setItemText(3, _translate("MainWindow", "1.5h"))
        self.comboBox_6.setItemText(4, _translate("MainWindow", "2h"))
        self.comboBox_6.setItemText(5, _translate("MainWindow", "2.5h"))
        self.comboBox_6.setItemText(6, _translate("MainWindow", "3h"))
        self.comboBox_6.setItemText(7, _translate("MainWindow", "3.5h"))
        self.comboBox_6.setItemText(8, _translate("MainWindow", "4h"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">关联模式信息</span></p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">开始时间：</span></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">截止时间：</span></p></body></html>"))

    def slot_1(self):
        self.graphicsView.setStyleSheet(
            "image: url(wind_corr.jpg);\n"
            "border-image: url(wind_corr.jpg);")

    def slot_2(self):
        self.graphicsView.setStyleSheet(
            "image: url(cloud_corr.jpg);\n"
            "border-image: url(cloud_corr.jpg);")

class MyWindow(QMainWindow, Ui_MainWindow_pattern_true):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()

    sys.exit(app.exec_())