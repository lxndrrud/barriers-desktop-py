from PySide6.QtWidgets import QWidget, QAbstractItemView
from PySide6.QtCore import QDate, QTime

from services.movements import MovementsService
from table_manager import TableManager
from ui_main_window import Ui_Form


class MainWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui_form = Ui_Form()
        self.ui_form.setupUi(self)

        self.ui_form.fromTime.setDate(QDate.currentDate())
        self.ui_form.fromTime.setTime(QTime(0, 0, 0))
        self.ui_form.toTime.setDate(QDate.currentDate().addDays(1))
        self.ui_form.toTime.setTime(QTime(0, 0, 0))
        self.ui_form.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.movement_service = MovementsService()
        self.table_manager = TableManager(self.ui_form.tableView, self.movement_service)
        self.ui_form.updateMovements.clicked.connect(self.table_manager.get_all_and_set_data)
        self.ui_form.openBarrier1.clicked.connect(lambda: self.movement_service.create_action("1", 1, "enter"))
