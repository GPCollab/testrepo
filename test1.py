import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Close App', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)

        printaction = QtGui.QAction('&Print a line', self)
        printaction.setStatusTip("print a line")
        printaction.triggered.connect(self.println)

        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        
        self.setToolTip('This is a <b>QWidget</b> widget')

        self.listWidget = QtGui.QListWidget(self)
        self.listWidget.setGeometry(QtCore.QRect(200, 200, 221, 91))

        qbtn = QtGui.QPushButton('Quit', self)
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        qbtn = QtGui.QPushButton('Print', self)
        qbtn.clicked.connect(self.println)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 100)

        qbtn = QtGui.QPushButton('testbutton', self)
        qbtn.clicked.connect(self.println)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(100, 150)
        
        qbtn = QtGui.QPushButton('remove some from >', self)
        qbtn.clicked.connect(self.removeSomeItems)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 250)

        self.listWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.listWidget.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.listWidget.setUniformItemSizes(False)
        self.listWidget.setSelectionRectVisible(False)
        self.listWidget.setObjectName("listWidget")


        self.statusBar()

        self.setGeometry(300, 300, 700, 500)
        self.setWindowTitle('Statusbar')    
        self.show()

        for i in range (1, 30):
            self.listWidget.addItem(QtGui.QListWidgetItem("test item " + str(i)))

    def println(self):
        print("HELLOOOOOO")

    def removeSomeItems(self):
        for i in range(1, 30):
            if i % 2 == 0:
                self.listWidget.takeItem(i)


def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()