from typing import Optional

class PersonBase:
    id_: int
    firstname: str
    middlename: str
    lastname: str
    skud_card: Optional[str]
    photo_path: Optional[str]

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
        person.photo_path = json_dict['photo_path']
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
            person.skud_card = json_dict.get("skud_card", None)
            person.photo_path = json_dict.get("photo_path", None)
            person.person_type = person_type if person_type != None else json_dict["type"]
            return person
        except Exception as e:
            return None
