import sys
import os
from PyQt5.QtCore import pyqtSignal, QObject, QRunnable, pyqtSlot, QThreadPool, QRect, Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QPushButton, QSystemTrayIcon, QStyle, QAction, QMenu, QDesktopWidget
from layout import Ui_MainWindow, DefaultLoadedLabel
import pathlib
from pytube import YouTube, Playlist, exceptions
import clipboard
import traceback
import plyer


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


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

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''

        # Retrieve args/kwargs here; and fire processing using them
        try:
            print(*self.args)
            result = self.fn(*self.args)
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
        print(link, pytubeTag, path)
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
    def __init__(self, mainComponent: QMainWindow, typeI: list[str] = ["vd", "au"], selectTagVideo: str = "360p", pytubeTag: int = 18):
        self.selectType = typeI[0]
        self.type: list[str] = typeI
        self.selectTagVideo: str = selectTagVideo
        self.path: str = str(pathlib.Path.home().joinpath("Desktop"))
        self.link = ""
        self.decodeTag = {"360p": 18, "720p": 22, "1080p": 137, '128kb': 140}
        self.pytubeTag: int = pytubeTag
        # *YtManager
        self.yt = YtManager()
        self.threadpool = QThreadPool()
        self.mainComponent = mainComponent

    def setTag(self, tag):
        self.selectTagVideo = tag
        self.pytubeTag = self.decodeTag[tag]
        print(" tag ---", self.pytubeTag)

    def setType(self, component1: QPushButton, component2: QPushButton):
        self.shift(self.type)
        self.selectType = self.type[0]
        print(self.selectType)
        dictionary = {"vd": ["360p", "720p",
                             "1080p"], "au": ['128kb'], "pl": ["360p"]}
        self.setTag(dictionary[self.selectType][0])
        component1.setText(self.selectType)
        component2.defineTag()

    def setPath(self, component: QMainWindow):
        folderpath = QFileDialog.getExistingDirectory(
            component, 'Select Folder')
        if folderpath:
            self.path: str = folderpath
            print(self.path)

    def download(self, component: QMainWindow, link: str):
        self.link = link
        if "https://www.youtube.com/" in link:
            # Any other args, kwargs are passed to the run function
            self.mainComponent.downloadButton.setText("In process")
            self.mainComponent.downloadButton.setEnabled(False)
            worker = Worker(self.yt.dowloadVA, self.link,
                            self.pytubeTag, self.path)
            worker.signals.result.connect(self.addLabel)
            worker.signals.finished.connect(self.thread_complete)
            # worker.signals.progress.connect(self.progress_fn)
            self.threadpool.start(worker)
            # title = self.yt.dowloadVA(self.link, self.pytubeTag, self.path)
        else:
            self.showDialog("linkError")

    def thread_complete(self):
        self.mainComponent.downloadButton.setText("download")
        self.mainComponent.downloadButton.setEnabled(True)
        print("THREAD COMPLETE!")

    def addLabel(self, title):
        print(title)
        if title == "LinkError":
            print("LinkError")
            self.showDialog("LinkError")
        elif title == "PrivateError":
            print("PrivateError")
        elif title == "otherError":
            return
        else:
            loadedLabel = DefaultLoadedLabel(title, self.path)
            self.mainComponent.verticalLayout.addWidget(loadedLabel)
            plyer.notification.notify(message=f'{title[:20]}...',
                                      app_name='Nero',
                                      title=f'Success downloaded',
                                      app_icon=resource_path("resource\logo.ico"))
            # *loaded label

    @staticmethod
    def showDialog(text: str):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(text)
        msgBox.setWindowTitle("Event")
        msgBox.setStandardButtons(
            QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()

    @staticmethod
    def shift(a: list):
        a.append(a.pop(0))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # warehouse declaration
        self.bd = Warehouse(self)
        self.setupUi(self, self)

        self.tray_icon = QSystemTrayIcon(self)
        icon = QIcon()
        icon.addPixmap(QPixmap(resource_path("resource\logo.png")), QIcon.Normal,
                       QIcon.Off)
        self.tray_icon.setIcon(icon)
        show_action = QAction("Show", self)
        quit_action = QAction("Exit", self)
        hide_action = QAction("Hide", self)
        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        quit_action.triggered.connect(self.close_app)

        self.DescriptionLayout.hide()
        # ? self.scrollArea.hide()
        self.descrButton.clicked.connect(lambda: self.DescriptionLayout.show(
        ) if (self.DescriptionLayout.isHidden() and (len(self.scrollAreaWidgetContents.children()) == 1)) else self.DescriptionLayout.hide())
        self.typeButton.clicked.connect(
            lambda: self.bd.setType(self.typeButton, self.tagButton))
        self.pathButton.clicked.connect(lambda: self.bd.setPath(self))
        self.downloadButton.clicked.connect(
            lambda: self.bd.download(self, clipboard.paste()))
        self.setGeometry(QRect(int(QDesktopWidget().screenGeometry(-1).width()*0.7),
                         int(QDesktopWidget().screenGeometry(-1).height()*0.59), 600, 400))
        # print(QtWidgets.QDesktopWidget().screenGeometry(-1).width())
        icon = QIcon(resource_path("resource\link.png"))

        self.pathButton.setIcon(icon)
        tray_menu = QMenu()
        tray_menu.setStyleSheet("font-family: \'RobotoFlex\';\n"
                                "font-style: normal;\n"
                                "font-weight: 200;\n"
                                "font-size: 16px;\n"
                                "line-height: 75.4%;\n"
                                "/* or 14px */\n"
                                "background: rgba(199, 199, 199, 0.0);\n"
                                "border: 0.5px solid rgba(167, 167, 167, 0.01);\n"
                                "color: rgba(255, 255, 255, 0.85);\n"
                                "")
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()
        self.tray_icon.activated.connect(self.systemIcon)
        
    def systemIcon(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            if self.isHidden():
                self.show()
            else:
                self.hide()

    def close_app(self):
        sys.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.setWindowIcon(QIcon(resource_path("resource\logo.png")))
    app.exec()
