from typing import Optional
import requests

from env import API_URL
from models.person import Person, person_from_json

class PersonsService:
    def send_skud_info(self, code: str) -> Optional[Person]:
        try:
            response = requests.get(API_URL + "/users/skudCard", params={
                "skud_card": code
            })
            return person_from_json(response.json())
        except Exception as e:
            print(f'user send card: {e}')
            return None
