
class Building:
    id_: int
    name: str

    @staticmethod
    def building_from_json(json_dict: dict):
        building = Building()
        building.id_ = json_dict['id']
        building.name = json_dict['name']
        return building