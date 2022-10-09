from threading import Thread
from time import sleep
from typing import Optional
import serial
from models.person import Person
import models.port_data
import services.persons
import services.movements
import utils.logger
from PySide6.QtCore import QObject, Signal


class SerialPortController(QObject):
    afterEventUpdated = Signal()
    setLastPerson = Signal(Person)

    def __init__(self, port: str, baudrate: int) -> None:
        super().__init__()
        self.low_level_controller = SerialLowLevelController(port, baudrate)
    
    def build(self, 
    persons_service: services.persons.PersonsService, movements_service: services.movements.MovementsService, logger: utils.logger.Logger):
        self.persons_service: services.persons.PersonsService = persons_service
        self.movements_service: services.movements.MovementsService = movements_service
        self.logger: utils.logger.Logger = logger

    def __openBarrierTimeout(self, reader: str):
        self.low_level_controller.writeToPort("@Code=user-success;@reader=" + reader)

    def lockBarrier(self):
        self.low_level_controller.writeToPort("@Code=lock;@reader=both")

    def unlockBarrier(self):
        self.low_level_controller.writeToPort("@Code=unlock;@reader=both")

    def stopExecution(self): self.low_level_controller.closePort()

    def __alarmBarrier(self):
        self.low_level_controller.writeToPort("@Code=user-not-found;@reader=both")

    def run(self): 
        self.thread = Thread(target=self.__listenPort)
        print(f"starting serial port controller thread {self.thread.getName()}")
        self.thread.start()
        print(f"ending serial port controller thread {self.thread.getName()}")

    def __listenPort(self):
        try: self.low_level_controller.openPort()
        except serial.SerialException as e: self.logger.writeToLogs(str(e))
        while(self.low_level_controller.isOpen()):
            sleep(0.01)
            try:
                portData = self.low_level_controller.readFromPort()
                if portData: print(portData)
                if not portData or len(portData) == 0:
                    continue
                if "@Code" not in portData and "@Direction" not in portData:
                    continue
                portData = models.port_data.PortData(portData)
                # Найти человека по карте и проверить валидность
                person = self.persons_service.send_skud_info(portData.code)
                if not person:
                    self.__alarmBarrier()
                    continue
                self.setLastPerson.emit(person)

                actionPerfomed: bool = False
                self.__openBarrierTimeout(portData.reader)
                for _ in range(35 + 10):
                    fromPort = self.low_level_controller.readFromPort()
                    if fromPort and portData.reader + "-success" in fromPort:
                        returnCode = self.movements_service.create_action(portData)
                        if returnCode != 201:
                            (self.logger
                            .writeToLogs(f"Человек({portData.code}) прошел({portData.reader}), но не был записан"))
                        actionPerfomed = True
                        break
                if not actionPerfomed:
                    self.movements_service.create_action(portData, failAction=True)
                self.afterEventUpdated.emit()
            except Exception as e:
                print('serial listen to port: ', e)
                self.logger.writeToLogs(str(e))
        print(f"ended {self.thread.getName()}")

    
class SerialLowLevelController:
    def __init__(self, port: str, baudrate: int) -> None:
        self.port = port
        self.baudrate = baudrate

    def openPort(self):
        self.serial_port = serial.Serial(self.port, self.baudrate, timeout=0.1)


    def writeToPort(self, toWrite: str) -> None:
        try:
            if self.serial_port.isOpen():
                self.serial_port.write(bytes(toWrite, encoding="utf-8"))
                #self.serial_port.cancel_write()
        except Exception as e:
            print(f'Write exc: {e}')

    def readFromPort(self) -> Optional[str]:
        try:
            if self.serial_port.is_open:
                haveRead = self.serial_port.readline().decode('utf-8').strip()
                return haveRead
            return None
        except Exception as e:
            print(f'Read exc: {e}')
            return None

    def closePort(self):
        try:
            self.serial_port.close()
        except: pass

    def isOpen(self):
        try:
            return self.serial_port.isOpen()
        except: 
            return False
    


