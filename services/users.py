import requests
from env import API_URL
from models.person import Person, person_from_json

class UsersService:
    def send_skud_info(code: str) -> Person:
        try:
            response = requests.get(API_URL + "users/skudCard", params={
                "skud_card": code
            })
            return person_from_json(response.json())
        except:
            print('user send skud card exeption')
            return Person()
