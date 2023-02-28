import sys
from PyQt5 import QtWidgets, uic
from output import Ui_MainWindow
import pathlib


class Warehouse:
    # *keeping and managing
    def __init__(self, typeI=["vd", "au", "pl"], selectTagVideo="360p", pytubeTag = 18):
        self.selectType = typeI[0]
        self.type = typeI
        self.selectTagVideo = selectTagVideo
        self.path = pathlib.Path.home().joinpath("Desktop")
        self.link = ""
        self.decodeTag = {"360p": 18, "720p": 22}
        self.pytubeTag = pytubeTag

    def setTag(self, tag):
        self.selectTagVideo = tag
        self.pytubeTag = self.decodeTag[tag]
        print(" tag ---", tag)

    def setType(self, component1, component2):
        self.shift(self.type)
        self.selectType = self.type[0]
        print(self.selectType)
        component1.setText(self.selectType)
        component2.defineTag()

    def setPath(self, component):
        folderpath = QtWidgets.QFileDialog.getExistingDirectory(
            component, 'Select Folder')
        self.path = pathlib.Path(folderpath)

        print(self.path)

    @staticmethod
    def shift(a):
        a.append(a.pop(0))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # warehouse declaration
        self.bd = Warehouse()
        self.setupUi(self, self)
        self.DescriptionLayout.hide()
        # ? self.scrollArea.hide()
        self.descrButton.clicked.connect(lambda: self.DescriptionLayout.show(
        ) if self.DescriptionLayout.isHidden() else self.DescriptionLayout.hide())
        self.typeButton.clicked.connect(
            lambda: self.bd.setType(self.typeButton, self.tagButton))
        self.pathButton.clicked.connect(lambda: self.bd.setPath(self))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
