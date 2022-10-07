class PortData:
    code: str
    reader: str

    def __init__(self, raw_port_info: str) -> None:
        variables = raw_port_info.split(";")
        self.code = variables[0].split("=")[1].strip()
        self.reader = variables[1].split("=")[1].strip()
