from typing import Tuple
from .person import Person, person_from_json

class Movement:
    id_: int
    id_building: int
    building_name: str
    id_event: int
    event_name: str
    event_time: str
    id_student: int
    id_employee: int

def movement_from_json(json_dict: dict) -> Movement:
    movement = Movement()
    movement.id_ = json_dict["id"]
    movement.id_building = json_dict["id_building"]
    movement.building_name = json_dict["building_name"]
    movement.event_name = json_dict["event_name"]
    date_ = str(json_dict["event_timestamp"]).split("T")[0]
    time_ = str(json_dict["event_timestamp"]).split("T")[1].split(".")[0]
    movement.event_time = f"{date_} {time_}"
    movement.id_event = json_dict["id_event"]
    movement.id_student = json_dict["id_student"]
    movement.id_employee = json_dict["id_employee"]
    return movement

class ExtendedMovement:
    movement: Movement
    user: Person

def ext_movement_to_tuple(mv: ExtendedMovement) -> tuple:
    res = (
        mv, 
        mv.movement.building_name, 
        mv.movement.event_name, 
        mv.movement.event_time, 
        mv.user.firstname, 
        mv.user.middlename, 
        mv.user.lastname, 
        mv.user.skud_card, 
        mv.user.person_type
    )
    return res

def extended_movement_from_json(json_dict: dict) -> ExtendedMovement:
    movement = movement_from_json(json_dict['movement'])
    person_type = "Сотрудник" if movement.id_employee != 0 else (
        "Студент" if movement.id_student != 0 else "Не определено")
    person = person_from_json(json_dict['user'], person_type)
    extended = ExtendedMovement()
    extended.movement = movement
    extended.user = person
    return extended


