# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\turch\Desktop\PyProject\Nero\srcUI\app.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(566, 427)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BaseLayout = QtWidgets.QFrame(self.centralwidget)
        self.BaseLayout.setGeometry(QtCore.QRect(0, 60, 551, 321))
        self.BaseLayout.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BaseLayout.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BaseLayout.setObjectName("BaseLayout")
        self.ManagePannel = QtWidgets.QFrame(self.BaseLayout)
        self.ManagePannel.setGeometry(QtCore.QRect(200, 270, 351, 51))
        self.ManagePannel.setStyleSheet("background: #222222;")
        self.ManagePannel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ManagePannel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ManagePannel.setObjectName("ManagePannel")
        self.pushButton = QtWidgets.QPushButton(self.ManagePannel)
        self.pushButton.setGeometry(QtCore.QRect(150, 10, 111, 28))
        self.pushButton.setStyleSheet("font-family: \'Handjet\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 16px;\n"
"line-height: 18px;\n"
"/* identical to box height */\n"
"\n"
"letter-spacing: 0.28em;\n"
"\n"
"color: rgba(255, 255, 255, 0.8);\n"
"\n"
"background: rgba(34, 34, 34, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.ManagePannel)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 7, 71, 31))
        self.pushButton_2.setStyleSheet("font-family: \'Handjet\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 16px;\n"
"line-height: 18px;\n"
"/* identical to box height */\n"
"\n"
"letter-spacing: 0.28em;\n"
"\n"
"color: rgba(255, 255, 255, 0.8);\n"
"\n"
"background: rgba(34, 34, 34, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.border = QtWidgets.QLabel(self.ManagePannel)
        self.border.setGeometry(QtCore.QRect(270, 16, 2, 20))
        self.border.setStyleSheet("background: rgba(217, 217, 217, 0.14);")
        self.border.setText("")
        self.border.setObjectName("border")
        self.border_2 = QtWidgets.QLabel(self.ManagePannel)
        self.border_2.setGeometry(QtCore.QRect(90, 16, 2, 20))
        self.border_2.setStyleSheet("background: rgba(217, 217, 217, 0.14);")
        self.border_2.setText("")
        self.border_2.setObjectName("border_2")
        self.border_3 = QtWidgets.QLabel(self.ManagePannel)
        self.border_3.setGeometry(QtCore.QRect(140, 16, 2, 20))
        self.border_3.setStyleSheet("background: rgba(217, 217, 217, 0.14);")
        self.border_3.setText("")
        self.border_3.setObjectName("border_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.ManagePannel)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 10, 31, 28))
        self.pushButton_3.setStyleSheet("font-family: \'Handjet\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 16px;\n"
"line-height: 18px;\n"
"/* identical to box height */\n"
"\n"
"letter-spacing: 0.28em;\n"
"\n"
"color: rgba(255, 255, 255, 0.8);\n"
"\n"
"background: rgba(34, 34, 34, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.ManagePannel)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 10, 31, 28))
        self.pushButton_4.setStyleSheet("font-family: \'Handjet\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 16px;\n"
"line-height: 18px;\n"
"/* identical to box height */\n"
"\n"
"letter-spacing: 0.28em;\n"
"\n"
"color: rgba(255, 255, 255, 0.8);\n"
"\n"
"background: rgba(34, 34, 34, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.border_4 = QtWidgets.QLabel(self.ManagePannel)
        self.border_4.setGeometry(QtCore.QRect(50, 16, 2, 20))
        self.border_4.setStyleSheet("background: rgba(217, 217, 217, 0.14);")
        self.border_4.setText("")
        self.border_4.setObjectName("border_4")
        self.pushButton_9 = QtWidgets.QPushButton(self.ManagePannel)
        self.pushButton_9.setGeometry(QtCore.QRect(56, 10, 31, 28))
        self.pushButton_9.setStyleSheet("font-family: \'Handjet\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 16px;\n"
"line-height: 18px;\n"
"/* identical to box height */\n"
"\n"
"letter-spacing: 0.28em;\n"
"\n"
"color: rgba(255, 255, 255, 0.8);\n"
"\n"
"background: rgba(34, 34, 34, 0);")
        self.pushButton_9.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\turch\\Desktop\\PyProject\\Nero\\srcUI\\../resource/icon/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon)
        self.pushButton_9.setObjectName("pushButton_9")
        self.DescriptionLayout = QtWidgets.QFrame(self.BaseLayout)
        self.DescriptionLayout.setGeometry(QtCore.QRect(0, 80, 551, 241))
        self.DescriptionLayout.setStyleSheet("background: rgba(34, 34, 34, 0);")
        self.DescriptionLayout.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DescriptionLayout.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DescriptionLayout.setObjectName("DescriptionLayout")
        self.label = QtWidgets.QLabel(self.DescriptionLayout)
        self.label.setGeometry(QtCore.QRect(100, 70, 161, 41))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("background: #222222;\n"
"font-family: \'Inter\';\n"
"font-style: normal;\n"
"font-weight: 200;\n"
"font-size: 13px;\n"
"line-height: 16px;\n"
"\n"
"color: #FFFFFF;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.DescriptionLayout)
        self.label_2.setGeometry(QtCore.QRect(310, 110, 181, 41))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("background: #222222;\n"
"font-family: \'Inter\';\n"
"font-style: normal;\n"
"font-weight: 200;\n"
"font-size: 13px;\n"
"line-height: 16px;\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"padding-left: 10px;")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.DescriptionLayout)
        self.label_3.setGeometry(QtCore.QRect(60, 130, 161, 31))
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setStyleSheet("background: #222222;\n"
"font-family: \'Inter\';\n"
"font-style: normal;\n"
"font-weight: 200;\n"
"font-size: 13px;\n"
"line-height: 16px;\n"
"\n"
"color: #FFFFFF;\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.DescriptionLayout)
        self.label_4.setGeometry(QtCore.QRect(10, 200, 121, 31))
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setStyleSheet("background: #222222;\n"
"font-family: \'Inter\';\n"
"font-style: normal;\n"
"font-weight: 200;\n"
"font-size: 13px;\n"
"line-height: 16px;\n"
"\n"
"color: #FFFFFF;\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.scrollArea = QtWidgets.QScrollArea(self.BaseLayout)
        self.scrollArea.setGeometry(QtCore.QRect(200, 90, 351, 181))
        self.scrollArea.setStyleSheet("background: rgba(34, 34, 34, 0);\n"
"border: 0px")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 351, 181))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.LoadLabel_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.LoadLabel_2.setGeometry(QtCore.QRect(0, 10, 350, 71))
        self.LoadLabel_2.setStyleSheet("background: #222222;\n"
"paffing: 10px;")
        self.LoadLabel_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LoadLabel_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LoadLabel_2.setObjectName("LoadLabel_2")
        self.LoadLabel_path_4 = QtWidgets.QLabel(self.LoadLabel_2)
        self.LoadLabel_path_4.setGeometry(QtCore.QRect(0, 32, 171, 31))
        self.LoadLabel_path_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.LoadLabel_path_4.setStyleSheet("background: rgba(34, 34, 34, 0);\n"
"font-family: \'Inter\';\n"
"font-style: normal;\n"
"font-weight: 200;\n"
"font-size: 13px;\n"
"line-height: 16px;\n"
"\n"
"color: #FFFFFF;\n"
"")
        self.LoadLabel_path_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.LoadLabel_path_4.setObjectName("LoadLabel_path_4")
        self.LoadLabel_name_4 = QtWidgets.QLabel(self.LoadLabel_2)
        self.LoadLabel_name_4.setGeometry(QtCore.QRect(0, 0, 261, 31))
        self.LoadLabel_name_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.LoadLabel_name_4.setStyleSheet("background: rgba(34, 34, 34, 0);\n"
"font-family: \'Inter\';\n"
"font-style: normal;\n"
"font-weight: 200;\n"
"font-size: 13px;\n"
"line-height: 16px;\n"
"\n"
"color: #FFFFFF;\n"
"")
        self.LoadLabel_name_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.LoadLabel_name_4.setObjectName("LoadLabel_name_4")
        self.LoadLabel_progress_4 = QtWidgets.QLabel(self.LoadLabel_2)
        self.LoadLabel_progress_4.setGeometry(QtCore.QRect(170, 30, 141, 31))
        self.LoadLabel_progress_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.LoadLabel_progress_4.setStyleSheet("background: rgba(34, 34, 34, 0);\n"
"font-family: \'Inter\';\n"
"font-style: normal;\n"
"font-weight: 200;\n"
"font-size: 13px;\n"
"line-height: 16px;\n"
"\n"
"color: #FFFFFF;\n"
"")
        self.LoadLabel_progress_4.setAlignment(QtCore.Qt.AlignCenter)
        self.LoadLabel_progress_4.setObjectName("LoadLabel_progress_4")
        self.LoadLabel_close_4 = QtWidgets.QPushButton(self.LoadLabel_2)
        self.LoadLabel_close_4.setGeometry(QtCore.QRect(280, 0, 31, 28))
        self.LoadLabel_close_4.setStyleSheet("font-family: \'Handjet\';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 16px;\n"
"line-height: 18px;\n"
"/* identical to box height */\n"
"\n"
"letter-spacing: 0.28em;\n"
"\n"
"color: rgba(255, 255, 255, 0.8);\n"
"\n"
"background: rgba(34, 34, 34, 0);")
        self.LoadLabel_close_4.setObjectName("LoadLabel_close_4")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.DescriptionLayout.raise_()
        self.ManagePannel.raise_()
        self.scrollArea.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 566, 26))
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
        self.pushButton.setText(_translate("MainWindow", " * download *"))
        self.pushButton_2.setText(_translate("MainWindow", "descr"))
        self.pushButton_3.setText(_translate("MainWindow", "Vd"))
        self.pushButton_4.setText(_translate("MainWindow", "tag"))
        self.label.setText(_translate("MainWindow", "Change type: playlist or video"))
        self.label_2.setText(_translate("MainWindow", "Automaticaly copy link \n"
" from bufer"))
        self.label_3.setText(_translate("MainWindow", "Directory"))
        self.label_4.setText(_translate("MainWindow", "Setup quality"))
        self.LoadLabel_path_4.setText(_translate("MainWindow", "File path////////////////"))
        self.LoadLabel_name_4.setText(_translate("MainWindow", "Name////////////////"))
        self.LoadLabel_progress_4.setText(_translate("MainWindow", ">>In profress: 99%"))
        self.LoadLabel_close_4.setText(_translate("MainWindow", "X"))