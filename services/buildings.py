from typing import List
from env import API_URL
from PySide6.QtCore import QObject, Signal
import requests

from models.building import Building


class BuildingsService(QObject):
    showException = Signal(str)

    def __init__(self) -> None:
        super().__init__()

    def get_all(self):
        try:
            response = requests.get(API_URL + "/buildings")
            if response.status_code != 200: 
                raise Exception(f"серверная ошибка -> {response.json()}")
            buildings_list: List[Building] = []
            json_ = response.json()
            if len(json_) == 0: 
                raise Exception("список корпусов для фильтра не получен!")
            for building in json_:
                buildings_list.append(Building.building_from_json(building))
            return buildings_list
        except Exception as e:
            self.showException.emit(f"Ошибка во время получения корпусов: {e}")
            return []
