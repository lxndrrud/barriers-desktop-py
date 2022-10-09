from typing import List, Optional
import requests
from env import API_URL, ID_BUILDING

from models.movement import ExtendedMovement, Movement, extended_movement_from_json, movement_from_json
from models.port_data import PortData

class MovementsService:
    def get_all(self, id_building: int=None, from_: str=None, to_: str=None):
        try:
            response = requests.get(API_URL + "/movements", params={
                "id_building": id_building,
                "from": from_,
                "to": to_
            })
            json_ = response.json()
            movement_list: List[ExtendedMovement] = []
            if len(json_) == 0:
                return []
            for movement in json_:
                movement_list.append(extended_movement_from_json(movement))
            return movement_list
        except Exception as e:
            print(f'get all movements: {e}')
            return []


    def create_action(self, portData: PortData, failAction=False):
        try:
            response = requests.post(API_URL + "/movements/action", data={
                "skud_card": portData.code,
                "id_building": ID_BUILDING,
                "event": (portData.reader if not failAction else "fail")
            })
            return response.status_code
        except Exception as e:
            print(f'post action: {e}')
            return 500
