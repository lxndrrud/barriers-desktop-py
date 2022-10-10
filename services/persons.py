from typing import Optional
import requests

from env import API_URL
from models.person import Person, person_from_json

class PersonsService:
    def send_skud_info(self, code: str) -> Optional[Person]:
        try:
            response = requests.get(API_URL + "/users/skudCard", params={
                "skud_card": code
            })
            return person_from_json(response.json())
        except Exception as e:
            print(f'user send card: {e}')
            return None

    def get_employee_info(self, id_employee: int):
        try:
            response = requests.get(API_URL + "/users/employee", params={
                "id_employee": id_employee
            })
            print(response.json())
            return response.json()
        except Exception as e:
            print(f'get employee info: {e}')
            return None

    def get_student_info(self, id_student: int):
        try:
            response = requests.get(API_URL + "/users/student", params={
                "id_student": id_student
            })
            print(response.json())
            return response.json()
        except Exception as e:
            print(f'get student info: {e}')
            return None
