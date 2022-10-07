import serial

from models.port_data import PortData


class SerialPortController:
    def __init__(self, port: str, baudrate: int) -> None:
        self.port = port
        self.baudrate = baudrate
        self.serial_port = serial.Serial(port, baudrate)

    def openPort(self):
        self.serial_port.open()

    def writeToPort(self, toWrite: str) -> None:
        self.serial_port.write(toWrite)

    def readFromPort(self) -> str:
        return self.serial_port.readline().decode('utf-8')

    def closePort(self):
        self.serial_port.close()

    def listenPort(self):
        while(self.serial_port.is_open):
            try:
                portData = self.readFromPort()
                if len(portData) == 0 :
                    continue
                if "@Code" not in portData and "@Direction" not in portData:
                    continue
                portData = PortData(portData)

            except:
                print('port exception!')
