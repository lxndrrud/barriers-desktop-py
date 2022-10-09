from typing import List
from env import API_URL
import requests

from models.building import Building, building_from_json


class BuildingsService:
    def get_all(self):
        try:
            response = requests.get(API_URL + "/buildings")
            buildings_list: List[Building] = []
            json_ = response.json()
            if len(json_) == 0: return []
            for building in json_:
                buildings_list.append(building_from_json(building))
            return buildings_list
        except Exception as e:
            print(f'get all buildings: {e}')
            return []
