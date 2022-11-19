from io import BytesIO
from typing import Tuple, Union

import PIL.Image
from PIL import Image
from PySide6.QtCore import QBuffer, QByteArray, QIODevice, QRect
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QPainter, QPen
from PySide6.QtWidgets import QLabel


class Canvas(QLabel):
    def __init__(self, size: Union[Tuple, QRect], parent=None):
        super().__init__(parent)
        self.setGeometry(size)
        self.size_x, self.size_y = size.size().width(), size.size().height()
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setAutoFillBackground(True)
        self.setPalette(p)
        self.myPixmap = QPixmap(self.size_x, self.size_y)
        self.painter = QPainter(self.myPixmap)
        self.painter.setPen(QPen(Qt.black, 10))
        self.painter.fillRect(0, 0, self.size_x, self.size_y, Qt.white)
        self.setPixmap(self.myPixmap)
        self.last = None

    def mouseMoveEvent(self, event):
        """
        Mouse move event handler
        event: event object
        """
        if self.last:
            self.painter.drawLine(self.last, event.pos())
            self.last = event.pos()
            self.setPixmap(self.myPixmap)
            self.update()

    def mousePressEvent(self, event):
        """
        Mouse press event handler
        event: event object
        """
        self.last = event.pos()

    def mouseReleaseEvent(self, event):
        """
        Mouse release event handler
        event: event object
        """
        self.last = None

    def clear_the_field(self):
        """
        Clears the canvas
        """
        self.painter.fillRect(0, 0, self.size_x, self.size_y, Qt.white)
        self.last = None
        self.setPixmap(self.myPixmap)
        self.update()

    def get_the_image(self) -> PIL.Image.Image:
        """
        Returns image as a numpy array
        """
        # Save QPixmap to QByteArray via QBuffer.
        byte_array = QByteArray()
        buffer = QBuffer(byte_array)
        buffer.open(QIODevice.WriteOnly)
        self.myPixmap.save(buffer, 'PNG')

        # gets image using Pillow
        return Image.open(BytesIO(buffer.data()))  # image getter

