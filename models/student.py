from typing import List
from models.group import Group
from models.person import Person


class Student:
    person: Person
    groups: List[Group]

    @staticmethod
    def student_from_json(json_dict: dict):
        try:
            person = Person.person_from_json(json_dict["student"])
            groups = [ Group.group_from_json(group) for group in json_dict["groups"] ]
            student = Student()
            student.groups = groups
            student.person = person
            return student
        except Exception as e:
            print(f"parse student: {e}") 
            return None
