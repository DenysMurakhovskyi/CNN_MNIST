from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QPainter, QPen
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import QBuffer, QByteArray, QIODevice
from io import BytesIO
from PIL import Image, ImageOps
import numpy as np
from numpy.typing import ArrayLike


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
        self.painter.fillRect(0, 0, 160, 160, Qt.white)
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

    def get_the_image_as_array(self) -> ArrayLike:
        # Save QPixmap to QByteArray via QBuffer.
        byte_array = QByteArray()
        buffer = QBuffer(byte_array)
        buffer.open(QIODevice.WriteOnly)
        self.myPixmap.save(buffer, 'PNG')

        pil_im = Image.open(BytesIO(buffer.data()))
        grayscale = ImageOps.grayscale(pil_im)
        grayscale = grayscale.resize((20, 20), resample=1)
        np_img = np.array(grayscale)
        f = lambda x: 0 if x < 100 else 255
        np_img = np.vectorize(f)(np_img)
        img = Image.fromarray(np_img)
        img.show()
        pass
