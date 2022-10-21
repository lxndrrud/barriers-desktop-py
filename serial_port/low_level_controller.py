from typing import Optional
import serial
import utils.logger

class SerialLowLevelController:
    def __init__(self, port: str, baudrate: int) -> None:
        self.port = port
        self.baudrate = baudrate

    def build(self, logger: utils.logger.Logger):
        self.logger = logger

    def openPort(self):
        self.serial_port = serial.Serial(self.port, self.baudrate, timeout=0.7)

    def writeToPort(self, toWrite: str) -> bool:
        try:
            if self.serial_port.isOpen():
                self.serial_port.write(bytes(toWrite, encoding="utf-8"))
                return True
            return False
        except Exception as e:
            self.logger.writeToLogs(f"low level {self.port} write to port: {e}")
            return False

    def readFromPort(self) -> Optional[str]:
        try:
            if self.serial_port.is_open:
                haveRead = self.serial_port.readline().decode('utf-8').strip()
                return haveRead
            return None
        except Exception as e:
            self.logger.writeToLogs(f"low level {self.port} read from port: {e}")
            return None

    def closePort(self):
        try:
            self.serial_port.close()
        except Exception as e:
            self.logger.writeToLogs(f"low level {self.port} close port: {e}")

    def isOpen(self):
        try:
            return self.serial_port.isOpen()
        except Exception as e: 
            self.logger.writeToLogs(f"low level {self.port} port isOpen: {e}")
            return False
