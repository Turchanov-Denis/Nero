import sys
from PyQt5 import QtWidgets, uic
from output import Ui_MainWindow


class Warehouse:
    def __init__(self, typeI=["vd", "au", "pl"], selectTagVideo="360p"):
        self.selectType = typeI[0]
        self.type = typeI
        self.selectTagVideo = selectTagVideo

    def setTag(self, tag):
        self.selectTagVideo = tag
        print(" tag ---", tag)

    def setType(self, component1, component2):
        self.shift(self.type)
        self.selectType = self.type[0]
        print(self.selectType)
        component1.setText(self.selectType)
        component2.defineTag()
        

    @staticmethod
    def shift(a):
        a.append(a.pop(0))


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
        self.typeButton.clicked.connect(
            lambda: self.bd.setType(self.typeButton,self.tagButton))


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
