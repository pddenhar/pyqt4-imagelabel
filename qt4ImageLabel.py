from PyQt4 import QtGui, QtCore

class ImageLabel(QtGui.QLabel):
    def __init__(self, parent=None, pixmap=None):
        QtGui.QLabel.__init__(self, parent)
        self.pixmap = pixmap
    def paintEvent(self, event):
        QtGui.QLabel.paintEvent(self, event)
        if self.pixmap == None:
            return
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setRenderHint(QtGui.QPainter.Antialiasing)
        scaledImg = self.pixmap.scaled(self.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        x = (self.size().width() - scaledImg.size().width()) / 2
        y = (self.size().height() - scaledImg.size().height()) / 2
        qp.drawPixmap(QtCore.QPoint(x,y), scaledImg)
    def setPixmap(self, pixmap):
        self.pixmap = pixmap