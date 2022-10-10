from typing import List
from models.person import Person
from models.position import Position

class Employee:
    person: Person
    positions: List[Position]

    @staticmethod
    def employee_from_json(json_dict: dict):
        try:
            person = Person.person_from_json(json_dict["employee"])
            positions = [ Position.position_from_json(position) for position in json_dict['positions'] ]
            employee = Employee()
            employee.person = person
            employee.positions = positions
            return employee
        except Exception as e:
            print(f"parse employee {e}")
            return None
