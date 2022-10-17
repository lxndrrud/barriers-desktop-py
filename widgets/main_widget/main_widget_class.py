from typing import List
from PySide6.QtWidgets import QWidget, QAbstractItemView, QGridLayout, QDialog, QLabel, QVBoxLayout
from PySide6.QtCore import QDate, QTime, Signal
from models.person import Person
import models.table_model
import models.movement
import serial_port.serial_port_controller
import serial_port.serial_port_interface
import services.movements
import services.buildings
import services.persons
import services.photos
import widgets.main_widget.ui_main_window
import widgets.personal_movement_modal.personal_movement_modal_class


class MainWidget(QWidget):
    beforeShutdown = Signal()

    def __init__(self,  ui_form: widgets.main_widget.ui_main_window.Ui_Form,
    movements_service: services.movements.MovementsService, buildings_service: services.buildings.BuildingsService,
    persons_service: services.persons.PersonsService, photos_service: services.photos.PhotosService,
    b1_controller: serial_port.serial_port_interface.ISerialPortController, 
    b2_controller: serial_port.serial_port_interface.ISerialPortController) -> None:
        super().__init__()
        self.ui_form = ui_form
        self.setLayout(QGridLayout(self))
        self.ui_form.setupUi(self)
        self.movements_service: services.movements.MovementsService = movements_service
        self.buildings_service: services.buildings.BuildingsService = buildings_service
        self.persons_service = persons_service
        self.photos_service = photos_service
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
        self.ui_form.gridLayout.setSizeConstraint(QGridLayout.SetMaximumSize)
        # Соединение обновления размера формы по размер окна 
        self.resizeEvent = lambda event: self.ui_form.layoutWidget.resize(
            event.size().width()-20, 
            event.size().height()-20)
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
        # Создание модального окна при ошибке
        self.persons_service.showException.connect(self.showErrorModal)
        self.buildings_service.showException.connect(self.showErrorModal)
        self.movements_service.showException.connect(self.showErrorModal)
        self.photos_service.showException.connect(self.showErrorModal)
        self.barrier1Controller.showException.connect(self.showErrorModal)
        self.barrier2Controller.showException.connect(self.showErrorModal)
        # Инициализация data-зависимых компонентов UI
        self.setupInfo()

    def closeEvent(self, event) -> None:
        self.beforeShutdown.emit()
        event.accept()

    def showErrorModal(self, message: str):
        errorModal = QDialog(self)
        errorModal.setModal(True)
        errorModal.setWindowTitle('Ошибка')
        label = QLabel()
        label.setText(message)
        label.setWordWrap(True)
        layout = QVBoxLayout()
        layout.addWidget(label)
        errorModal.setLayout(layout)
        errorModal.setMaximumWidth(400)
        errorModal.resize(200, 200)
        errorModal.show() 

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
        for movement in movements: mapped.append(movement.to_tuple())
        header = ('Здание', 'Событие', 'Время', 'Имя', 'Отчество', 'Фамилия', 'СКУД', 'Тип')
        self.ui_form.tableView.setModel(models.table_model.MyTableModel(self.ui_form.tableView, mapped, header))

    def setLastPerson(self, person: Person):
        if person.photo_path:
            photo = self.photos_service.get_photo(person.photo_path)
            if photo:
                self.ui_form.lastPersonLabel.setPixmap(photo)
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
                self.buildings_service,
                self.photos_service))
        personalModal.show()
        self.modals.append(personalModal)


