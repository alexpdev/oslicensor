from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class Window(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.layout = QHBoxLayout()
        self.central = QWidget(parent=self)
        self.setCentralWidget(self.central)
        self.central.setLayout(self.layout)
