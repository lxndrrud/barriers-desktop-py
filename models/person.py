from typing import Optional

class PersonBase:
    id_: int
    firstname: str
    middlename: str
    lastname: str
    skud_card: str

    def fullname(self):
        return f"{self.lastname} {self.firstname} {self.middlename}"

    @staticmethod
    def person_base_from_json(json_dict: dict):
        person = PersonBase()
        person.id_ = int(json_dict["id"])
        person.firstname = json_dict["firstname"]
        person.middlename = json_dict["middlename"]
        person.lastname = json_dict["lastname"]
        person.skud_card = json_dict['skud_card']
        return person

class Person(PersonBase):
    person_type: str

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def person_from_json(json_dict: dict, person_type: Optional[str]=None):
        try:
            person = Person()
            person.id_ = int(json_dict["id"])
            person.firstname = json_dict["firstname"]
            person.middlename = json_dict["middlename"]
            person.lastname = json_dict["lastname"]
            person.skud_card = json_dict['skud_card']
            person.person_type = person_type if person_type != None else json_dict["type"]
            return person
        except:
            return None
