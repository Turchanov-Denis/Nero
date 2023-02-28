import sys
from PyQt5 import QtWidgets, uic
from output import Ui_MainWindow
import pathlib
from pytube import YouTube, Playlist
import clipboard


class YtManager:
    @staticmethod
    def dowloadVA(link: str, pytubeTag: int, path: str):
        print(link, pytubeTag)
        try:
            yt = YouTube(link)
            stream = yt.streams.get_by_itag(pytubeTag)
            stream.download(output_path=path)
            return yt.title
        except:
            pass

    @staticmethod
    def dowloadPl(link: str, pytubeTag: int):
        try:
            p = Playlist(link)
            for video in p.videos:
                video.streams.get_by_itag(pytubeTag).download()
        except:
            pass


class Warehouse:
    # *keeping and managing
    def __init__(self, typeI: list[str] = ["vd", "au", "pl"], selectTagVideo: str = "360p", pytubeTag: int = 18):
        self.selectType = typeI[0]
        self.type: list[str] = typeI
        self.selectTagVideo: str = selectTagVideo
        self.path: str = str(pathlib.Path.home().joinpath("Desktop"))
        self.link = ""
        self.decodeTag = {"360p": 18, "720p": 22, "1080p": 137, '128kb': 140}
        self.pytubeTag: int = pytubeTag
        # *YtManager
        self.yt = YtManager()

    def setTag(self, tag):
        self.selectTagVideo = tag
        self.pytubeTag = self.decodeTag[tag]
        print(" tag ---", self.pytubeTag)

    def setType(self, component1: QtWidgets.QPushButton, component2: QtWidgets.QPushButton):
        self.shift(self.type)
        self.selectType = self.type[0]
        print(self.selectType)
        dictionary = {"vd": ["360p", "720p",
                             "1080p"], "au": ['128kb'], "pl": ["360p"]}
        self.setTag(dictionary[self.selectType][0])
        component1.setText(self.selectType)
        component2.defineTag()

    def setPath(self, component: QtWidgets.QMainWindow):
        folderpath = QtWidgets.QFileDialog.getExistingDirectory(
            component, 'Select Folder')
        if folderpath:
            self.path: str = folderpath
            print(self.path)

    def download(self, link: str):
        self.link = link
        title = self.yt.dowloadVA(self.link, self.pytubeTag, self.path)
        print(title)

    @staticmethod
    def shift(a: list):
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
        self.downloadButton.clicked.connect(
            lambda: self.bd.download(clipboard.paste()))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
