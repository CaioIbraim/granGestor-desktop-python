from PySide6.QtWidgets import QMainWindow, QStackedWidget
from ui.login import LoginScreen

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("granGestor Desktop")
        self.stacked = QStackedWidget()
        self.setCentralWidget(self.stacked)
        self.login_screen = LoginScreen(self)
        self.stacked.addWidget(self.login_screen)
        # Futuramente: adicionar telas de vendas, estoque, etc.
