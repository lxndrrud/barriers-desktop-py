from PySide6.QtWidgets import QWidget, QAbstractItemView
from PySide6.QtCore import QDate, QTime
import models.table_model
import models.movement
import serial_port.serial_port_controller
import services.movements
import services.buildings
import widgets.main_widget.ui_main_window


class MainWidget(QWidget):
    def __init__(self,  ui_form: widgets.main_widget.ui_main_window.Ui_Form,
    movements_service: services.movements.MovementsService, buildings_service: services.buildings.BuildingsService,
    b1_controller: serial_port.serial_port_controller.SerialPortController, 
    b2_controller: serial_port.serial_port_controller.SerialPortController) -> None:
        super().__init__()
        self.ui_form = ui_form
        self.ui_form.setupUi(self)
        self.movements_service: services.movements.MovementsService = movements_service
        self.buildings_service: services.buildings.BuildingsService = buildings_service
        self.barrier1Controller = b1_controller
        self.barrier2Controller = b2_controller
        self.build()
        

    def build(self):
        # Инициализация UI
        self.ui_form.fromTime.setDate(QDate.currentDate())
        self.ui_form.fromTime.setTime(QTime(0, 0, 0))
        self.ui_form.toTime.setDate(QDate.currentDate().addDays(1))
        self.ui_form.toTime.setTime(QTime(0, 0, 0))
        self.ui_form.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        # Инициализация data-зависимых компонентов UI
        self.setupInfo()
        self.ui_form.updateMovements.clicked.connect(self.updateMovements)
        self.ui_form.closeBarrier1.clicked.connect(self.barrier1Controller.lockBarrier)
        self.ui_form.closeBarrier2.clicked.connect(self.barrier2Controller.lockBarrier)
        self.ui_form.openBarrier1.clicked.connect(self.barrier1Controller.unlockBarrier)
        self.ui_form.openBarrier2.clicked.connect(self.barrier2Controller.unlockBarrier)

    def closeEvent(self, event) -> None:
        self.barrier1Controller.low_level_controller.closePort()
        self.barrier2Controller.low_level_controller.closePort()
        event.accept()

    def setupInfo(self):
        # Загрузить здания
        buildings = self.buildings_service.get_all()
        for b in buildings: self.ui_form.buildingSelect.addItem(b.name, b.id_)
        # Загрузить передвижения
        self.updateMovements()


    def updateMovements(self):
        movements = self.movements_service.get_all(
            self.ui_form.buildingSelect.currentData(),
            "T".join(self.ui_form.fromTime.text().split(" ")),
            "T".join(self.ui_form.toTime.text().split(" "))
        )
        mapped = []
        for movement in movements: mapped.append(models.movement.ext_movement_to_tuple(movement))
        header = ('Здание', 'Событие', 'Время', 'Имя', 'Отчество', 'Фамилия', 'СКУД', 'Тип')
        self.ui_form.tableView.setModel(models.table_model.MyTableModel(self.ui_form.tableView, mapped, header))

