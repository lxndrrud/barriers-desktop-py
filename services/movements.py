import json
from typing import List, Optional
import requests

from models.movement import ExtendedMovement, Movement, extended_movement_from_json, movement_from_json

class MovementsService:
    base_url: str

    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def get_all(self):
        try:
            response = requests.get(self.base_url + "/movements")
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
            response = requests.post(self.base_url + "/movements/action", data={
                "skud_card": skud_card,
                "id_building": id_building,
                "event": event
            })
        except:
            print('post action exception')
            return
