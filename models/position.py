class Position:
    id_: int 
    title: str
    department_title: str
    date_drop: str

    @staticmethod
    def position_from_json(json_dict: dict):
        position = Position()
        position.id_ = json_dict['id']
        position.title = json_dict['title']
        position.department_title = json_dict['department_title']
        position.date_drop = json_dict['date_drop']
        return position

