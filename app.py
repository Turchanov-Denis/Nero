from re import match
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from layout import Ui_MainWindow, DefaultLoadedLabel
import pathlib
from pytube import YouTube, Playlist, exceptions
import clipboard
import traceback

class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        tuple (exctype, value, traceback.format_exc() )

    result
        object data returned from processing, anything

    progress
        int indicating % progress

    '''
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)


class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''

        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            # Return the result of the processing
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()  # Done


class YtManager():
    @staticmethod
    def dowloadVA(link: str, pytubeTag: int, path: str):
        print(link, pytubeTag)
        try:
            yt = YouTube(link)
            stream = yt.streams.get_by_itag(pytubeTag)
            stream.download(output_path=path)
            return yt.title
        except exceptions.RegexMatchError:
            return "LinkError"
        except exceptions.VideoPrivate:
            return "PrivateError"

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

    def download(self, component: QtWidgets.QMainWindow, link: str):
        self.link = link
        if link:
            self.worker_thread = QtCore.QThread()
            title = self.yt.dowloadVA(self.link, self.pytubeTag, self.path)
            if title == "LinkError":
                print("LinkError")
            elif title == "PrivateError":
                print("PrivateError")
            else:
                print("something is wrong")
                return
            # *loaded label
            loadedLabel = DefaultLoadedLabel(title, self.path)
            component.verticalLayout.addWidget(loadedLabel)

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
            lambda: self.bd.download(self, clipboard.paste()))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
