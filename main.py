from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow
from db.database import init_db

if __name__ == "__main__":
    import sys
    init_db()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())