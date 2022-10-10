from PySide6.QtWidgets import QWidget, QAbstractItemView
from PySide6.QtCore import QDate, QTime, Signal
import models.movement
import models.table_model
import services.buildings
import services.movements
import services.persons
import widgets.personal_movement_modal.ui_personal_movement_modal


class PersonalMovementModal(QWidget):
    def __init__(self, id_student: int, id_employee: int, 
    movements_service: services.movements.MovementsService, persons_service: services.persons.PersonsService, 
    buildings_service: services.buildings.BuildingsService) -> None:
        super().__init__()
        self.id_student = id_student
        self.id_employee = id_employee
        self.movements_service = movements_service
        self.persons_service = persons_service
        self.buildings_service = buildings_service
        self.ui_form = widgets.personal_movement_modal.ui_personal_movement_modal.Ui_Form()
        self.ui_form.setupUi(self)
        self.setup()

    def setup(self):
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

    def setupInfo(self):
        # Загрузить здания
        buildings = self.buildings_service.get_all()
        for b in buildings: self.ui_form.buildingSelect.addItem(b.name, b.id_)
        # Загрузить информацию о человеке
        self.loadPerson()
        # Загрузить передвижения
        self.updateMovements()

    def loadPerson(self):
        if self.id_employee != 0:
            person = self.persons_service.get_employee_info(self.id_employee)
        elif self.id_student != 0:
            person = self.persons_service.get_student_info(self.id_student)
        else: return

    def updateMovements(self):
        movements = self.movements_service.get_all_personal(
            self.id_employee, self.id_student, 
            self.ui_form.buildingSelect.currentData(), 
            "T".join(self.ui_form.fromTime.text().split(" ")),
            "T".join(self.ui_form.toTime.text().split(" "))
        )
        mapped = []
        for movement in movements: mapped.append(models.movement.movement_to_tuple(movement))
        header = ('Здание', 'Событие', 'Время')
        self.ui_form.tableView.setModel(models.table_model.MyTableModel(self.ui_form.tableView, mapped, header))


