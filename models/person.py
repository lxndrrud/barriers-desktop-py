from typing import Optional


class Person:
    id_: int
    firstname: str
    middlename: str
    lastname: str
    skud_card: str
    person_type: str

def person_from_json(json_dict: dict, person_type: Optional[str]=None) -> Person:
    person = Person()
    person.id_ = int(json_dict["id"])
    person.firstname = json_dict["firstname"]
    person.middlename = json_dict["middlename"]
    person.lastname = json_dict["lastname"]
    person.skud_card = json_dict['skud_card']
    person.person_type = person_type if person_type != None else json_dict["type"]
    return person
