from PySide6.QtWidgets import QApplication
from container import build_app

if __name__ == "__main__":
    app = QApplication([])

    widget= build_app()
    widget.show()

    app.exec()
