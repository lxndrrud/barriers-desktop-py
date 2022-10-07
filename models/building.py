
class Building:
    id_: int
    name: str

def building_from_json(json_dict: dict) -> Building:
    building = Building()
    building.id_ = json_dict['id']
    building.name = json_dict['name']
    return building