import sys
from PyQt5 import QtWidgets, uic
from output import Ui_MainWindow


class Warehouse:
    def __init__(self, selectType="vd", typeI=["vd, au, pl"], selectTagVideo="360p"):
        self.selectType = selectType
        self.type = typeI
        self.selectTagVideo = selectTagVideo

    def setTag(self, tag):
        self.selectTagVideo = tag
        print(" tag ---", tag)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.bd = Warehouse()
        self.setupUi(self, self)
        # warehouse
        self.DescriptionLayout.hide()
        self.scrollArea.hide()
        self.descrButton.clicked.connect(lambda: self.DescriptionLayout.show(
        ) if self.DescriptionLayout.isHidden() else self.DescriptionLayout.hide())


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
