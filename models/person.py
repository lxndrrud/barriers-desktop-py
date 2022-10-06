

class Person:
    id_: int
    firstname: str
    middlename: str
    lastname: str
    skud_card: str
    person_type: str

def person_from_json(json_dict: dict, person_type: str) -> Person:
    person = Person()
    person.id_ = json_dict["id"]
    person.firstname = json_dict["firstname"]
    person.middlename = json_dict["middlename"]
    person.lastname = json_dict["lastname"]
    person.skud_card = json_dict['skud_card']
    person.person_type = person_type
    return person
