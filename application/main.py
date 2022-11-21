import numpy as np
from PySide6 import QtWidgets as qw

from application import model
from application.main_window import Ui_MainWindow
from application.utils import Utils


class TheWindow(qw.QMainWindow):
    """
    Program's graphic interface
    """

    def __init__(self):
        """
        Main window constructor
        """
        # main window init
        super(TheWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.processButton.clicked.connect(self.process_image)
        self.ui.exitButton.clicked.connect(self.close)
        self.ui.clearButton.clicked.connect(self.clear)
        self.ui.saveButton.clicked.connect(self.save_the_image)

        self.ui.lcdNumber.display(-1)

    def process_image(self):
        """
        Image recognition
        """
        self.ui.processButton.setDisabled(True)

        image_np = Utils.get_formatted_image(self.ui.figure.get_the_image()).reshape((28, 28, 1))
        prediction = model.predict(np.array([(np.array(image_np) / 255).astype('int')]))
        most_prob_value  = list(sorted({v: k for k, v in enumerate(list(prediction)[0])}.items(),
                                       reverse=True))[0][1]

        self.ui.lcdNumber.display(most_prob_value)

        self.ui.processButton.setDisabled(False)

    def clear(self):
        """
        Clears the canvas, resets the LCD indicator
        """
        self.ui.figure.clear_the_field()
        self.ui.lcdNumber.display(-1)

    def save_the_image(self):
        """
        Saves the image to a PNG file
        """
        file_name, _ = qw.QFileDialog.getSaveFileName(self, 'Save File', '', "Image files (*.png)")
        if file_name:
            img = self.ui.figure.get_the_image()
            img.save(file_name, bitmap_format='png')
