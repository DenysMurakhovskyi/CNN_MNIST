import logging

from PySide6 import QtWidgets as qw

from application.gui.main_window import Ui_MainWindow


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
        self.ui.clearButton.clicked.connect(self.ui.figure.clear_the_field)
        self.ui.saveButton.clicked.connect(self.save_the_image)

        self.ui.lcdNumber.display(-1)
        self.ui.progressBar.setValue(0)

        self.logger = logging.getLogger('app_logger')
        logging.getLogger('app_logger').setLevel(logging.DEBUG)

    def process_image(self):
        self.ui.processButton.setDisabled(True)
        img_np = self.ui.figure.get_the_image()
        # synchronizer = SyncRunner()
        # synchronizer.signals.message_signal.connect(self._show_message)
        # synchronizer.signals.finish_signal.connect(self._enable_button)
        # QThreadPool().start(synchronizer)

    def save_the_image(self):
        file_name, _ = qw.QFileDialog.getSaveFileName(self, 'Save File', '', "Image files (*.png)")
        img = self.ui.figure.get_the_image()
        img.save(file_name, bitmap_format='png')