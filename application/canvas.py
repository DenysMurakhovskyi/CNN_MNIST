import os
from io import BytesIO

import numpy as np
from PIL import Image, ImageOps
from PySide6.QtCore import QBuffer, QByteArray, QIODevice
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QPainter, QPen
from PySide6.QtWidgets import QLabel
from numpy.typing import ArrayLike

THRESHOLD = 100


class Canvas(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setAutoFillBackground(True)
        self.setPalette(p)
        self.myPixmap = QPixmap(160, 160)
        self.painter = QPainter(self.myPixmap)
        self.painter.setPen(QPen(Qt.black, 10))
        self.painter.fillRect(0, 0, 160, 160, Qt.white)
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
        self.painter.fillRect(0, 0, 160, 160, Qt.white)
        self.last = None
        self.setPixmap(self.myPixmap)
        self.update()

    def get_the_image_as_array(self) -> ArrayLike:
        """
        Returns image as a numpy array
        """
        # Save QPixmap to QByteArray via QBuffer.
        byte_array = QByteArray()
        buffer = QBuffer(byte_array)
        buffer.open(QIODevice.WriteOnly)
        self.myPixmap.save(buffer, 'PNG')

        # gets image using Pillow
        pil_im = Image.open(BytesIO(buffer.data()))  # image getter
        grayscale = ImageOps.grayscale(pil_im).resize((20, 20), resample=1)  # image grayscale
        np_img = np.array(grayscale)  # image to a NumPy array
        np_img = np.vectorize(lambda x: 0 if x < THRESHOLD else 255)(np_img)  # gets black/white image (binary)

        # shows image for debug purpose only
        if os.environ.get('DEBUG', '0') == '1':
            img = Image.fromarray(np_img)
            img.show()

        # returns image as a numpy array
        return np_img
