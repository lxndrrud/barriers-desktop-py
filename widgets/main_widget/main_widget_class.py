from typing import List
from PySide6.QtWidgets import QWidget, QAbstractItemView, QGridLayout
from PySide6.QtCore import QDate, QTime, Signal
from PySide6.QtGui import QFont
from models.person import Person
import models.table_model
import models.movement
import serial_port.serial_port_controller
import services.movements
import services.buildings
from services.persons import PersonsService
import widgets.main_widget.ui_main_window
import widgets.personal_movement_modal.personal_movement_modal_class


class MainWidget(QWidget):
    beforeShutdown = Signal()

    def __init__(self,  ui_form: widgets.main_widget.ui_main_window.Ui_Form,
    movements_service: services.movements.MovementsService, buildings_service: services.buildings.BuildingsService,
    persons_service: PersonsService,
    b1_controller: serial_port.serial_port_controller.SerialPortController, 
    b2_controller: serial_port.serial_port_controller.SerialPortController) -> None:
        super().__init__()
        self.ui_form = ui_form
        self.setLayout(QGridLayout(self))
        self.ui_form.setupUi(self)
        self.movements_service: services.movements.MovementsService = movements_service
        self.buildings_service: services.buildings.BuildingsService = buildings_service
        self.persons_service = persons_service
        self.barrier1Controller = b1_controller
        self.barrier1Controller.setParent(self)
        self.barrier2Controller = b2_controller
        self.barrier2Controller.setParent(self)
        self.modals: List[widgets.personal_movement_modal.personal_movement_modal_class.PersonalMovementModal] = []
        self.build()
        

    def build(self):
        # Инициализация UI
        self.ui_form.fromTime.setDate(QDate.currentDate())
        self.ui_form.fromTime.setTime(QTime(0, 0, 0))
        self.ui_form.toTime.setDate(QDate.currentDate().addDays(1))
        self.ui_form.toTime.setTime(QTime(0, 0, 0))
        self.ui_form.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        ## Инициализация data-зависимых компонентов UI
        self.setupInfo()
        # Обновление передвижений
        self.ui_form.updateMovements.clicked.connect(self.updateMovements)
        # Персональные передвижения
        self.ui_form.personMovementsButton.clicked.connect(self.getPersonalMovementsModal)
        # Открытие/закрытие турникетов
        self.ui_form.closeBarrier1.clicked.connect(self.barrier1Controller.lockBarrier)
        self.ui_form.closeBarrier2.clicked.connect(self.barrier2Controller.lockBarrier)
        self.ui_form.openBarrier1.clicked.connect(self.barrier1Controller.unlockBarrier)
        self.ui_form.openBarrier2.clicked.connect(self.barrier2Controller.unlockBarrier)
        # Отключение перед выходом из приложения
        self.barrier1Controller.afterEventUpdated.connect(self.updateMovements)
        self.beforeShutdown.connect(self.barrier1Controller.stopExecution)
        self.barrier2Controller.afterEventUpdated.connect(self.updateMovements)
        self.beforeShutdown.connect(self.barrier2Controller.stopExecution)
        # Вывод последнего просканированного человека
        self.barrier1Controller.setLastPerson.connect(self.setLastPerson)
        self.barrier2Controller.setLastPerson.connect(self.setLastPerson)
        # Индикация подключения к порту
        self.barrier1Controller.indicateStatus.connect(lambda status: (
            self.ui_form.barrier1Indicator.setText("ВКЛ" if status else "ВЫКЛ")
        ))
        self.barrier2Controller.indicateStatus.connect(lambda status: (
            self.ui_form.barrier2Indicator.setText("ВКЛ" if status else "ВЫКЛ")
        ))

    def closeEvent(self, event) -> None:
        self.beforeShutdown.emit()
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

    def setLastPerson(self, person: Person):
        # TODO: Нужно добавить сюда фото человека через QPixmap в QLabel
        self.ui_form.lastPersonFullname.setText(f"{person.lastname} {person.firstname} {person.middlename}")

    def getPersonalMovementsModal(self):
        # Получение индекса выбранного передвижения
        index_ = self.ui_form.tableView.selectedIndexes()[0] if (self.ui_form.tableView.selectedIndexes()) else None
        if not index_: return
        movement: models.movement.ExtendedMovement = (self.ui_form.tableView.model()
            .getSelectedData(self.ui_form.tableView.selectedIndexes()[0]))
        personalModal = (widgets.personal_movement_modal.personal_movement_modal_class
            .PersonalMovementModal(
                movement.movement.id_student, 
                movement.movement.id_employee,
                self.movements_service,
                self.persons_service,
                self.buildings_service))
        personalModal.show()
        self.modals.append(personalModal)


