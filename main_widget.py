from PySide6.QtWidgets import QWidget
from services.movements import MovementsService
from table_manager import TableManager
from ui_main_window import Ui_Form

class MainWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui_form = Ui_Form()
        self.movement_service = MovementsService("http://localhost:8081")
        self.ui_form.setupUi(self)
        self.table_manager = TableManager(self.ui_form.tableWidget, self.movement_service)
        self.ui_form.updateMovements.clicked.connect(self.table_manager.get_all_and_set_data)
        self.ui_form.openBarrier1.clicked.connect(lambda: self.movement_service.create_action("1", 1, "enter"))
