from typing import List, Optional
import requests
from env import API_URL, ID_BUILDING
from PySide6.QtCore import QObject, Signal

from models.movement import ExtendedMovement, Movement
from models.port_data import PortData

class MovementsService(QObject):
    showException = Signal(str)

    def __init__(self) -> None:
        super().__init__()

    def get_all(self, id_building: int=None, from_: str=None, to_: str=None):
        try:
            response = requests.get(API_URL + "/movements", params={
                "id_building": id_building,
                "from": from_,
                "to": to_
            })
            if response.status_code != 200: 
                raise Exception(f"серверная ошибка -> {response.json()}")
            json_ = response.json()
            movement_list: List[ExtendedMovement] = []
            if len(json_) == 0:
                return []
            for movement in json_:
                movement_list.append(ExtendedMovement.extended_movement_from_json(movement))
            return movement_list
        except Exception as e:
            self.showException.emit(f"Ошибка во время получения перемещений {e}")
            return []

    def get_all_personal(self, id_employee: int=None, id_student: int=None, 
    id_building: int=None, from_: str=None, to_: str=None):
        try:
            response = requests.get(API_URL + "/movements/user", params={
                'id_employee': id_employee,
                'id_student': id_student,
                'id_building': id_building,
                'from': from_,
                'to': to_
            })
            if response.status_code != 200: 
                raise Exception(f"серверная ошибка -> {response.json()}")
            json_ = response.json()
            movement_list: List[Movement] = []
            if len(json_) == 0:
                return []
            for movement in json_:
                movement_list.append(Movement.movement_from_json(movement))
            return movement_list
        except Exception as e:
            self.showException.emit(f"Ошибка во время получения перемещений: {e}")
            return []



    def create_action(self, portData: PortData, failAction=False):
        try:
            response = requests.post(API_URL + "/movements/action", data={
                "skud_card": portData.code,
                "id_building": ID_BUILDING,
                "event": (portData.reader if not failAction else "fail")
            })
            if response.status_code != 201: 
                raise Exception(f"серверная ошибка -> запись перемещения не создана!")
            return response.status_code
        except Exception as e:
            self.showException.emit(f"Ошибка во время создания перемещения: {e}")
            return 500
