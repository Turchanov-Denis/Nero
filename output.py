# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\turch\Desktop\PyProject\Nero\srcUI\app.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class DefaultButton(QtWidgets.QPushButton):
    def __init__(self, parent, text=""):
        super(DefaultButton, self).__init__(parent=parent)
        self.setText(text)
        self.setStyleSheet(
            "QPushButton {"
            "font-family: \'Handjet\';\n"
            "font-style: normal;\n"
            "font-weight: 400;\n"
            "font-size: 12px;\n"
            "line-height: 18px;\n"
            "letter-spacing: 0.28em;\n"
            "color: rgba(255, 255, 255, 0.5);\n"
            "background: rgba(149, 149, 149, 0.0);}\n"
            "QPushButton:hover {\n"
            "color: rgba(255, 255, 255, 0.8);}")


class DefaulIconButton(QtWidgets.QPushButton):
    def __init__(self, parent, text=""):
        super(DefaulIconButton, self).__init__(parent=parent)
        self.setText(text)
        self.setStyleSheet(
            "QPushButton {"
            "font-family: \'Handjet\';\n"
            "font-style: normal;\n"
            "font-weight: 400;\n"
            "font-size: 12px;\n"
            "line-height: 18px;\n"
            "letter-spacing: 0.28em;\n"

            "color: rgba(255, 255, 255, 0.5);\n"
            "background: rgba(149, 149, 149, 0.0);}\n"
            "QPushButton:hover {\n"
            "color: rgba(255, 255, 255, 0.8);"
            "background: rgba(255, 255, 255, 0.1);}\n"
        )


class DescrLabel(QtWidgets.QLabel):
    def __init__(self, parent, text: str):
        super(DescrLabel, self).__init__(parent=parent)
        self.setText(text)
        self.setStyleSheet("background: #222222;\n"
                           "font-family: \'Inter\';\n"
                           "font-style: normal;\n"
                           "font-weight: 200;\n"
                           "font-size: 13px;\n"
                           "line-height: 16px;\n"
                           "color: #FFFFFF;\n")
        self.setAlignment(QtCore.Qt.AlignCenter)
# self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
# self.label.setAlignment(QtCore.Qt.AlignCenter)


class DefaultMenu(DefaultButton):

    def __init__(self, parent, main):
        super(DefaultMenu, self).__init__(parent)
        self.main = main
        self.dictionary = {"vd": ["360p", "720p", "1080p"]}
        self.defineTag()

    def setTag(self, tag):
        self.main.bd.setTag(tag)
        self.setText(tag)

    def defineTag(self):
        if self.main.bd.selectType in self.dictionary.keys():
            self.setText(self.dictionary["vd"][0])
        else:
            self.setText("")

    def enterEvent(self, event):
        menu = QtWidgets.QMenu(self)
        menu.setLayoutDirection(QtCore.Qt.RightToLeft)
        menu.setStyleSheet("QMenu{font-family: \'RobotoFlex\';\n"
                           "font-style: normal;\n"
                           "font-weight: 200;\n"
                           "font-size: 16px;\n"
                           "line-height: 75.4%;\n"
                           "/* or 14px */\n"
                           "background: #222222;"
                           "border: 0.5px solid rgba(167, 167, 167, 0.01);\n"
                           "color: rgba(255, 255, 255, 0.85);}\n"
                           """QMenu::item{
						color: rgba(255, 255, 255, 0.85);
						}
						QMenu::item:selected{
						color: rgba(255, 255, 255, 0.95);
						} """)

        if self.main.bd.selectType == "vd":
            Rename = menu.addAction('Res="360p"')
            Delete = menu.addAction('Res="720p"')
            menu_sort = menu.addAction('Res="1080p"')
            result = menu.exec_(self.mapToGlobal(QtCore.QPoint(-160, -30)))
            if Rename == result:
                self.setTag("360p")
            elif Delete == result:
                self.setTag("720p")
            elif menu_sort == result:
                self.setTag("1080p")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, main):
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
        self.ManagePannel.setGeometry(QtCore.QRect(180, 270, 371, 51))
        self.ManagePannel.setStyleSheet("background: #222222;")
        self.ManagePannel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ManagePannel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ManagePannel.setObjectName("ManagePannel")
        #! tag button
        self.tagButton = DefaultMenu(self.ManagePannel, main)
        self.tagButton.setGeometry(QtCore.QRect(15, 1, 41, 48))
        # download button
        self.downloadButton = DefaultButton(self.ManagePannel, "download")
        self.downloadButton.setGeometry(QtCore.QRect(160, 10, 111, 28))
        # descr
        self.descrButton = DefaultButton(self.ManagePannel, "desccr")
        self.descrButton.setGeometry(QtCore.QRect(290, 7, 71, 31))
        # type button
        self.typeButton = DefaultButton(self.ManagePannel, main.bd.selectType)
        self.typeButton.setGeometry(QtCore.QRect(110, 10, 31, 28))
         # path button
        self.pathButton = DefaulIconButton(self.ManagePannel)
        self.pathButton.setGeometry(QtCore.QRect(66, 12, 31, 28))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "C:\\Users\\turch\\Desktop\\PyProject\\Nero\\srcUI\\../resource/icon/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pathButton.setIcon(icon)
        self.pathButton.setObjectName("pathButton")
        # decoration border
        self.border = QtWidgets.QLabel(self.ManagePannel)
        self.border.setGeometry(QtCore.QRect(280, 16, 2, 20))
        self.border.setStyleSheet("background: rgba(217, 217, 217, 0.14);")
        self.border.setText("")
        self.border.setObjectName("border")
        self.border_2 = QtWidgets.QLabel(self.ManagePannel)
        self.border_2.setGeometry(QtCore.QRect(100, 16, 2, 20))
        self.border_2.setStyleSheet("background: rgba(217, 217, 217, 0.14);")
        self.border_2.setText("")
        self.border_2.setObjectName("border_2")
        self.border_3 = QtWidgets.QLabel(self.ManagePannel)
        self.border_3.setGeometry(QtCore.QRect(150, 16, 2, 20))
        self.border_3.setStyleSheet("background: rgba(217, 217, 217, 0.14);")
        self.border_3.setText("")
        self.border_3.setObjectName("border_3")
        self.border_4 = QtWidgets.QLabel(self.ManagePannel)
        self.border_4.setGeometry(QtCore.QRect(60, 16, 2, 20))
        self.border_4.setStyleSheet("background: rgba(217, 217, 217, 0.14);")
        self.border_4.setText("")
        self.border_4.setObjectName("border_4")
        # descr
        self.DescriptionLayout = QtWidgets.QFrame(self.BaseLayout)
        self.DescriptionLayout.setGeometry(QtCore.QRect(0, 80, 551, 241))
        self.DescriptionLayout.setStyleSheet(
            "background: rgba(34, 34, 34, 0);")
        self.DescriptionLayout.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DescriptionLayout.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DescriptionLayout.setObjectName("DescriptionLayout")
        self.label = DescrLabel(self.DescriptionLayout,
                                "Type: video/audio/playlist")
        self.label.setGeometry(QtCore.QRect(100, 70, 161, 41))
        self.label_2 = DescrLabel(
            self.DescriptionLayout, "Autobatically copy link")
        self.label_2.setGeometry(QtCore.QRect(310, 110, 181, 41))

        self.label_3 = DescrLabel(self.DescriptionLayout, "Directory")
        self.label_3.setGeometry(QtCore.QRect(60, 130, 161, 31))
        self.label_4 = DescrLabel(self.DescriptionLayout, "Select quality")
        self.label_4.setGeometry(QtCore.QRect(10, 200, 121, 31))

        # loaded frame
        self.scrollArea = QtWidgets.QScrollArea(self.BaseLayout)
        self.scrollArea.setGeometry(QtCore.QRect(200, 90, 351, 181))
        self.scrollArea.setStyleSheet("background: rgba(34, 34, 34, 0);\n"
                                      "border: 0px")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 351, 181))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.LoadLabel_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.LoadLabel_2.setGeometry(QtCore.QRect(0, 10, 350, 71))
        self.LoadLabel_2.setStyleSheet("background: #222222;\n")
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
        self.LoadLabel_path_4.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
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
        self.LoadLabel_name_4.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
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
        self.LoadLabel_path_4.setText("File path////////////////")
        self.LoadLabel_name_4.setText("Name////////////////")
        self.LoadLabel_progress_4.setText(">>In profress: 99%")
        self.LoadLabel_close_4.setText("X")
