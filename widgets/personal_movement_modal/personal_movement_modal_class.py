from typing import Optional
from PySide6.QtWidgets import QWidget, QAbstractItemView, QDialog
from PySide6.QtCore import QDate, QTime, Signal, QStringListModel
from models.employee import Employee
import models.movement
from models.student import Student
import models.table_model
import models.list_model
import services.buildings
import services.movements
import services.persons
import services.photos
import widgets.personal_movement_modal.ui_personal_movement_modal


class PersonalMovementModal(QDialog):
    def __init__(self, id_student: int, id_employee: int, 
    movements_service: services.movements.MovementsService, persons_service: services.persons.PersonsService, 
    buildings_service: services.buildings.BuildingsService, photos_service: services.photos.PhotosService) -> None:
        super().__init__()
        self.id_student = id_student
        self.id_employee = id_employee
        self.student: Optional[Student] = None
        self.employee: Optional[Employee] = None
        self.movements_service = movements_service
        self.persons_service = persons_service
        self.buildings_service = buildings_service
        self.photos_service = photos_service
        self.ui_form = widgets.personal_movement_modal.ui_personal_movement_modal.Ui_Form()
        self.ui_form.setupUi(self)
        self.setup()

    def setup(self):
        # Инициализация UI
        self.ui_form.infoListView.setModel(QStringListModel(self.ui_form.infoListView))
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
        # Загрузить информацию о человеке
        self.loadPerson()
        # Загрузить здания
        buildings = self.buildings_service.get_all()
        for b in buildings: self.ui_form.buildingSelect.addItem(b.name, b.id_)
        # Загрузить передвижения
        self.updateMovements()

    def loadPerson(self):
        if self.id_employee != 0:
            self.employee = self.persons_service.get_employee_info(self.id_employee)
            self.ui_form.personFullname.setText(self.employee.person.fullname())
            self.ui_form.typePerson.setText(self.employee.person.person_type)
            self.ui_form.skudCard.setText(self.employee.person.skud_card)
            self.__loadLastPersonInfoContent(self.employee.positions)
            if self.employee.person.photo_path:
                photo = self.photos_service.get_photo(self.employee.person.photo_path)
                if photo:
                    self.ui_form.personPhoto.setPixmap(photo.scaled(self.ui_form.personPhoto.size()))
        elif self.id_student != 0:
            self.student = self.persons_service.get_student_info(self.id_student)
            self.ui_form.personFullname.setText(self.student.person.fullname())
            self.ui_form.typePerson.setText(self.student.person.person_type)
            self.ui_form.skudCard.setText(self.student.person.skud_card)
            self.__loadLastPersonInfoContent(self.student.groups)
            if self.student.person.photo_path:
                photo = self.photos_service.get_photo(self.student.person.photo_path)
                if photo:
                    self.ui_form.personPhoto.setPixmap(photo.scaled(self.ui_form.personPhoto.size()))
        else: self.close()

    def __loadLastPersonInfoContent(self, content):
        model: QStringListModel = self.ui_form.infoListView.model()
        list_ = []
        for item in content:
            list_.append(item.toString())
        model.setStringList(list_)

    def updateMovements(self):
        movements = self.movements_service.get_all_personal(
            self.id_employee, self.id_student, 
            self.ui_form.buildingSelect.currentData(), 
            "T".join(self.ui_form.fromTime.text().split(" ")),
            "T".join(self.ui_form.toTime.text().split(" "))
        )
        mapped = []
        for movement in movements: mapped.append(movement.to_tuple())
        header = ('Здание', 'Событие', 'Время')
        self.ui_form.tableView.setModel(models.table_model.MyTableModel(self.ui_form.tableView, mapped, header))


