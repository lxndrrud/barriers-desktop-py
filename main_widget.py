from PySide6.QtWidgets import QWidget, QAbstractItemView
from PySide6.QtCore import QDate, QTime
from PySide6.QtGui import QPixmap
import requests
from services.buildings import BuildingsService
from services.persons import PersonsService
from services.movements import MovementsService
from table_manager import TableManager
from ui_main_window import Ui_Form


class MainWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui_form = Ui_Form()
        self.ui_form.setupUi(self)
        # Сервисы
        self.movement_service = MovementsService()
        self.building_service = BuildingsService()
        self.persons_service = PersonsService()
        # Инициализация UI
        self.ui_form.fromTime.setDate(QDate.currentDate())
        self.ui_form.fromTime.setTime(QTime(0, 0, 0))
        self.ui_form.toTime.setDate(QDate.currentDate().addDays(1))
        self.ui_form.toTime.setTime(QTime(0, 0, 0))
        self.ui_form.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        # Соединение поведения с отображением
        response = requests.get('http://teatrnaoboronny.ru/wp-content/uploads/2022/05/oWkh-ENj71CpD1wTtHc25d7mBI3grzMfm8OOKzE334SDmGYGXeMT7-zux_T7NW5J0v5pNf06JElnnFUp53XPUuwh-500x354.jpg')
        pixmap= QPixmap()
        pixmap.loadFromData(response.content)
        self.ui_form.lastPersonLabel.setPixmap(pixmap.scaled(200, 200))
        buildings = self.building_service.get_all()
        for b in buildings: self.ui_form.buildingSelect.addItem(b.name, b.id_)
        self.table_manager = TableManager(self.ui_form.tableView, self.movement_service)
        self.ui_form.updateMovements.clicked.connect(lambda: self.table_manager.get_all_and_set_data(
            self.ui_form.buildingSelect.currentData(), 
            "T".join(self.ui_form.fromTime.text().split(" ")),
            "T".join(self.ui_form.toTime.text().split(" "))
        ))
        self.ui_form.openBarrier1.clicked.connect(lambda: self.movement_service.create_action("1", 1, "enter"))
