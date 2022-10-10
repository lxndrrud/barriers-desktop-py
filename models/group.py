class Group:
    id_: int
    title: str
    course: str
    department_title: str

    @staticmethod
    def group_from_json(json_dict: dict):
        group = Group()
        group.id_ = json_dict['id']
        group.title = json_dict['title']
        group.course = json_dict['course']
        group.department_title = json_dict['department_title']
        return group
