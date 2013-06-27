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

        qbtn = QtGui.QPushButton('Quit', self)
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        qbtn = QtGui.QPushButton('Print', self)
        qbtn.clicked.connect(self.println)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 100)
        
        self.setWindowTitle('Icon')
        self.setGeometry(300, 300, 250, 150)
        self.setWindowIcon(QtGui.QIcon('ic.png'))

        self.statusBar()
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        fileMenu.addAction(printaction)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')    
        self.show()

    def println(self):
        print("HELLOOOOOO")

    # def closeEvent(self, event):
        
    #     reply = QtGui.QMessageBox.question(self, 'Message', "Are you sure to quit?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)

    #     if reply == QtGui.QMessageBox.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()


def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()