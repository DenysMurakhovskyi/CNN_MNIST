from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Canvas(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setAutoFillBackground(True)
        self.setPalette(p)
        self.myPixmap = QPixmap(160, 160)
        self.painter = QPainter(self.myPixmap)
        self.pen = QPen(Qt.black, 10)
        self.painter.setPen(self.pen)
        self.painter.fillRect(0,0,160,160, Qt.white)
        self.setPixmap(self.myPixmap)
        self.last = None

    def mouseMoveEvent(self, event):
        if self.last:
            self.painter.drawLine(self.last, event.pos())
            self.last = event.pos()
            self.setPixmap(self.myPixmap)
            self.update()

    def mousePressEvent(self, event):
        self.last = event.pos()

    def mouseReleaseEvent(self, event):
        self.last = None

    def clear_the_field(self):
        self.painter.fillRect(0, 0, 160, 160, Qt.white)
        self.last = None
        self.setPixmap(self.myPixmap)
        self.update()