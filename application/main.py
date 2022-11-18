import logging

from PySide6 import QtWidgets as qw
from PySide6.QtCore import QPoint


from application.main_window import Ui_MainWindow


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

        self.ui.pushButton_2.clicked.connect(self.ui.figure.get_the_image_as_array)
        self.ui.pushButton.clicked.connect(self.close)
        self.ui.clearButton.clicked.connect(self.ui.figure.clear_the_field)

        self.ui.lcdNumber.display(-1)
        self.ui.progressBar.setValue(0)

        self.logger = logging.getLogger('app_logger')
        logging.getLogger('app_logger').setLevel(logging.DEBUG)

    def _run_sync(self):
        self.ui.pushButton_2.setDisabled(True)
        # synchronizer = SyncRunner()
        # synchronizer.signals.message_signal.connect(self._show_message)
        # synchronizer.signals.finish_signal.connect(self._enable_button)
        # QThreadPool().start(synchronizer)