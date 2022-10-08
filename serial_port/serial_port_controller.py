from threading import Thread
from time import sleep
from types import FunctionType
from typing import Optional
import serial
import models.port_data
import services.persons
import services.movements
import utils.logger


class SerialPortController:
    def __init__(self, port: str, baudrate: int) -> None:
        self.low_level_controller = SerialLowLevelController(port, baudrate)
    
    def build(self, 
    persons_service: services.persons.PersonsService, movements_service: services.movements.MovementsService, logger: utils.logger.Logger):
        self.persons_service: services.persons.PersonsService = persons_service
        self.movements_service: services.movements.MovementsService = movements_service
        self.logger: utils.logger.Logger = logger

    def setupCallbacks(self, afterEventUpdate: FunctionType):
        self.afterEventUpdate = afterEventUpdate


    def __openBarrierTimeout(self, reader: str):
        self.low_level_controller.writeToPort("@Code=user-success;@reader=" + reader)

    def lockBarrier(self):
        self.low_level_controller.writeToPort("@Code=lock;@reader=both")

    def unlockBarrier(self):
        self.low_level_controller.writeToPort("@Code=unlock;@reader=both")

    def __alarmBarrier(self, reader: str):
        self.low_level_controller.writeToPort("@Code=user-not-found;@reader=both" + reader)

    def run(self): 
        self.thread = Thread(target=self.__listenPort)
        print(f"starting serial port controller thread {self.thread.getName()}")
        self.thread.start()
        print(f"ending serial port controller thread {self.thread.getName()}")

    def __listenPort(self):
        try: self.low_level_controller.openPort()
        except serial.SerialException as e: self.logger.writeToLogs(str(e))
        while(self.low_level_controller.isOpen()):
            try:
                portData = self.low_level_controller.readFromPort()
                if not portData or len(portData) == 0 :
                    continue
                if "@Code" not in portData and "@Direction" not in portData:
                    continue
                portData = models.port_data.PortData(portData)

                person = self.persons_service.send_skud_info(portData.code)
                if not person:
                    self.__alarmBarrier(portData.reader)
                    continue

                actionPerfomed: bool = False
                self.__openBarrierTimeout(portData.reader)
                for _ in range(350 + 100):
                    fromPort = self.low_level_controller.readFromPort()
                    
                    if fromPort == portData.reader + "-success":
                        returnCode = self.movements_service.create_action(portData)
                        if returnCode != 201:
                            (self.logger
                            .writeToLogs(f"Человек({portData.code}) прошел({portData.reader}), но не был записан"))
                        actionPerfomed = True
                    sleep(0.01)
                if not actionPerfomed:
                    self.movements_service.create_action(portData, failAction=True)
                self.afterEventUpdate()
            except:
                self.logger.writeToLogs(f"Критическая ошибка SerialPortController")
        print(f"ended {self.thread.getName()}")

    
class SerialLowLevelController:
    def __init__(self, port: str, baudrate: int) -> None:
        self.port = port
        self.baudrate = baudrate

    def openPort(self):
        self.serial_port = serial.Serial(self.port, self.baudrate)


    def writeToPort(self, toWrite: str) -> None:
        try:
            if self.serial_port.isOpen():
                self.serial_port.write(toWrite)
        except:
            pass

    def readFromPort(self) -> Optional[str]:
        try:
            if self.serial_port.is_open:
                return self.serial_port.readline().decode('utf-8')
            return None
        except:
            pass

    def closePort(self):
        try:
            self.serial_port.close()
        except: pass

    def isOpen(self):
        try:
            return self.serial_port.isOpen()
        except: 
            return False
    


