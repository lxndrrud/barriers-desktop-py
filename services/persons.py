from typing import Optional
import requests
from PySide6.QtCore import QObject, Signal
from env import API_URL
from models.employee import Employee
from models.person import Person
from models.student import Student

class PersonsService(QObject):
    showException = Signal(str)

    def __init__(self) -> None:
        super().__init__()

    def send_skud_info(self, code: str) -> Optional[Person]:
        try:
            response = requests.get(API_URL + "/users/skudCard", params={
                "skud_card": code
            })
            person = Person.person_from_json(response.json())
            if not person: 
                raise Exception("Информация о человеке не найдена!")
            return person
        except Exception as e:
            self.showException.emit(e)
            return None

    def get_employee_info(self, id_employee: int):
        try:
            response = requests.get(API_URL + "/users/employee", params={
                "id_employee": id_employee
            })
            employee = Employee.employee_from_json(response.json())
            if not employee:
                raise Exception("Информация о сотруднике не найдена!")
            return employee
        except Exception as e:
            self.showException.emit(e)
            return None

    def get_student_info(self, id_student: int):
        try:
            response = requests.get(API_URL + "/users/student", params={
                "id_student": id_student
            })
            student = Student.student_from_json(response.json())
            if not student: 
                raise Exception("Информация о студенте не найдена!")
            return student
        except Exception as e:
            self.showException.emit(e)
            return None
