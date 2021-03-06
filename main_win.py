# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_win.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import base64
from PyQt5 import QtCore, QtGui, QtWidgets
from images.location_of_plants_in_jilin_png import img as location_of_plants_in_jilin

tmp = open('location_of_plants_in_jilin.png', 'wb')        #创建临时的文件
tmp.write(base64.b64decode(location_of_plants_in_jilin))    ##把这个one图片解码出来，写入文件中去。
tmp.close()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 371, 31))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 60, 879, 3))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 90, 151, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 90, 151, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.dir_data_1 = QtWidgets.QLabel(self.centralwidget)
        self.dir_data_1.setGeometry(QtCore.QRect(440, 100, 281, 16))
        self.dir_data_1.setObjectName("dir_data_1")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(500, 180, 256, 241))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.dir_data_2 = QtWidgets.QLabel(self.centralwidget)
        self.dir_data_2.setGeometry(QtCore.QRect(560, 140, 151, 31))
        self.dir_data_2.setObjectName("dir_data_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(50, 150, 400, 300))
        self.graphicsView.setMinimumSize(QtCore.QSize(400, 300))
        self.graphicsView.setMaximumSize(QtCore.QSize(400, 300))
        self.graphicsView.setStyleSheet("border-image: url(:/location/location_of_plants_in_jilin.png);")
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 450, 113, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(630, 450, 131, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(500, 500, 113, 32))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(640, 500, 113, 32))
        self.pushButton_7.setObjectName("pushButton_7")
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
        self.pushButton.setText(_translate("MainWindow", "风/光电站分布"))
        self.pushButton_2.setText(_translate("MainWindow", "静态数据导入地址"))
        self.dir_data_1.setText(_translate("MainWindow", "TextLabel"))
        self.dir_data_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">电站基本信息</span></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "数据导入更新"))
        self.pushButton_4.setText(_translate("MainWindow", "时空关联模式分析"))
        self.pushButton_5.setText(_translate("MainWindow", "风电超短期预测"))
        self.pushButton_7.setText(_translate("MainWindow", "光伏超短期预测"))


