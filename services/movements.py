from typing import List, Optional
import requests
from env import API_URL

from models.movement import ExtendedMovement, Movement, extended_movement_from_json, movement_from_json

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
                print(movement)
            return movement_list
        except:
            print('get all movements exception')
            return []


    def create_action(self, skud_card: str, id_building: int, event: str):
        try:
            response = requests.post(API_URL + "/movements/action", data={
                "skud_card": skud_card,
                "id_building": id_building,
                "event": event
            })
        except:
            print('post action exception')
            return
