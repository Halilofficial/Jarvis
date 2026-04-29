import sys
from PyQt5.QtWidgets import QApplication
from ui.main_window import MainWindow
from config import APP_TITLE

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.setWindowTitle(APP_TITLE)
    main_window.show()
    sys.exit(app.exec_())
