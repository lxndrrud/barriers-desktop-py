from PySide6.QtWidgets import QApplication

from main_widget import MainWidget

app = QApplication([])

widget = MainWidget()
widget.show()

app.exec()
