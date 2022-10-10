from .person import Person

class Movement:
    id_: int
    id_building: int
    building_name: str
    id_event: int
    event_name: str
    event_time: str
    id_student: int
    id_employee: int

    def to_tuple(self) -> tuple:
        res = (
            self, 
            self.building_name, 
            self.event_name, 
            self.event_time, 
        )
        return res

    @staticmethod
    def movement_from_json(json_dict: dict):
        try:
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
        except Exception as e:
            print(f"parse movement: {e}")
            return None

class ExtendedMovement:
    movement: Movement
    user: Person

    def to_tuple(self) -> tuple:
        res = (
            self, 
            self.movement.building_name, 
            self.movement.event_name, 
            self.movement.event_time, 
            self.user.firstname, 
            self.user.middlename, 
            self.user.lastname, 
            self.user.skud_card, 
            self.user.person_type
        )
        return res

    @staticmethod
    def extended_movement_from_json(json_dict: dict):
        try:
            movement = Movement.movement_from_json(json_dict['movement'])
            person_type = "Сотрудник" if movement.id_employee != 0 else (
                "Студент" if movement.id_student != 0 else "Не определено")
            person = Person.person_from_json(json_dict['user'], person_type)
            extended = ExtendedMovement()
            extended.movement = movement
            extended.user = person
            return extended
        except Exception as e:
            print(f"parse extended movement: {e}")
            return None


