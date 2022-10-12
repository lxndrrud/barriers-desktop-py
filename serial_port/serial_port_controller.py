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
    indicateStatus = Signal(bool)
    showException = Signal(str)

    def __init__(self, port: str, baudrate: int) -> None:
        super().__init__()
        self.low_level_controller = SerialLowLevelController(port, baudrate)
    
    def build(self, 
    persons_service: services.persons.PersonsService, movements_service: services.movements.MovementsService, logger: utils.logger.Logger):
        self.persons_service: services.persons.PersonsService = persons_service
        self.movements_service: services.movements.MovementsService = movements_service
        self.logger: utils.logger.Logger = logger
        self.low_level_controller.build(logger)

    def __openBarrierTimeout(self, reader: str):
        check = self.low_level_controller.writeToPort("@Code=user-success;@reader=" + reader)
        if not check: self.showException.emit("high level {self.low_level_controller.port}->Турникет не открыт->Ошибка записи в порт!")

    def lockBarrier(self):
        check = self.low_level_controller.writeToPort("@Code=lock;@reader=both")
        if not check : self.showException.emit("high level {self.low_level_controller.port}->Турникет не закрыт->Ошибка записи в порт!")

    def unlockBarrier(self):
        check = self.low_level_controller.writeToPort("@Code=unlock;@reader=both")
        if not check: self.showException.emit("high level {self.low_level_controller.port}->Турникет не открыт->Ошибка записи в порт!") 

    def stopExecution(self): self.low_level_controller.closePort()

    def __alarmBarrier(self):
        check = self.low_level_controller.writeToPort("@Code=user-not-found;@reader=both")
        if not check: 
            self.showException.emit(f"high level {self.low_level_controller.port}->Турникет не подал звуковой сигнал->Ошибка записи в порт!")

    def run(self): 
        self.thread = Thread(target=self.__listenPort)
        self.thread.start()

    def __isOpen(self):
        value_ = self.low_level_controller.isOpen()
        self.indicateStatus.emit(value_)
        if not value_: self.showException.emit(f"Порт {self.low_level_controller.port} закрыт!")
        return value_

    def __validatePortData(self, portData: str):
        if not portData or len(portData) == 0:
            return False
        if "@Code" not in portData and "@Direction" not in portData:
            return False
        return True


    def __listenPort(self):
        try: self.low_level_controller.openPort()
        except serial.SerialException as e: 
            self.logger.writeToLogs(f"high level {self.low_level_controller.port}: {e}")
        while(self.__isOpen()):
            sleep(0.01)
            try:
                # Получить и проверить данные с порта
                strPortData = self.low_level_controller.readFromPort()
                if not self.__validatePortData(strPortData): 
                    continue
                portData = models.port_data.PortData(strPortData)
                # Найти человека по карте и проверить валидность
                person = self.persons_service.send_skud_info(portData.code)
                if not person:
                    self.__alarmBarrier()
                    continue
                self.setLastPerson.emit(person)
                # Проверка совершенного действия, раз в 100 мс
                actionPerfomed: bool = False
                self.__openBarrierTimeout(portData.reader)
                for _ in range(35 + 10):
                    fromPort = self.low_level_controller.readFromPort()
                    if fromPort and portData.reader + "-success" in fromPort:
                        returnCode = self.movements_service.create_action(portData)
                        if returnCode != 201:
                            (self.showException
                            .emit(f"high level {self.low_level_controller.port}: Человек({portData.code}) прошел({portData.reader}), но не был записан"))
                            (self.logger
                            .writeToLogs(f"high level {self.low_level_controller.port}: Человек({portData.code}) прошел({portData.reader}), но не был записан"))
                        actionPerfomed = True
                        break
                # Записать неудачу при проходе, если турникет не прокручен
                if not actionPerfomed:
                    self.movements_service.create_action(portData, failAction=True)
                # Запросить обновление виджета
                self.afterEventUpdated.emit()
            except Exception as e:
                self.showException.emit(f"high level {self.low_level_controller.port} listen: {e}")
                self.logger.writeToLogs(f"high level {self.low_level_controller.port} listen: {e}")

    
class SerialLowLevelController:
    def __init__(self, port: str, baudrate: int) -> None:
        self.port = port
        self.baudrate = baudrate

    def build(self, logger: utils.logger.Logger):
        self.logger = logger

    def openPort(self):
        self.serial_port = serial.Serial(self.port, self.baudrate, timeout=0.1)

    def writeToPort(self, toWrite: str) -> bool:
        try:
            if self.serial_port.isOpen():
                self.serial_port.write(bytes(toWrite, encoding="utf-8"))
                return True
            return False
        except Exception as e:
            self.logger.writeToLogs(f"low level {self.port} write to port: {e}")
            self.serial_port.close()
            return False

    def readFromPort(self) -> Optional[str]:
        try:
            if self.serial_port.is_open:
                haveRead = self.serial_port.readline().decode('utf-8').strip()
                return haveRead
            return None
        except Exception as e:
            self.logger.writeToLogs(f"low level {self.port} read from port: {e}")
            self.serial_port.close()
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
    


