from threading import Thread
from typing import Optional
from PySide6.QtCore import QObject, Signal
from models.person import Person
import services.persons
import services.movements
import utils.logger
import serial_port.low_level_controller


class ISerialPortController(QObject):
    afterEventUpdated = Signal()
    setLastPerson = Signal(Person)
    indicateStatus = Signal(bool)
    showException = Signal(str)
    _low_level_controller: serial_port.low_level_controller.SerialLowLevelController
    _thread: Optional[Thread] = None

    def build(self, 
    persons_service: services.persons.PersonsService, movements_service: services.movements.MovementsService, 
    logger: utils.logger.Logger):
        pass

    def _isOpen(self):
        value_ = self._low_level_controller.isOpen()
        self.indicateStatus.emit(value_)
        if not value_: self.showException.emit(f"Порт {self._low_level_controller.port} закрыт!")
        return value_

    def _validatePortData(self, portData: str):
        if not portData or len(portData) == 0:
            return False
        if len(portData.split(";")) != 2:
            return False
        if "@Code" not in portData or "@Direction" not in portData:
            return False
        return True

    def _alarmBarrier(self, reader: str):
        check = self._low_level_controller.writeToPort(f"@Code=user-not-found;@reader={reader}")
        if not check: 
            self.showException.emit(f"high level {self._low_level_controller.port}->Турникет не подал звуковой сигнал->Ошибка записи в порт!")

    def openPort(self):
        if not self._thread:
            try: self._low_level_controller.openPort()
            except Exception as e: print(f"open port exception: {e}")
            self.run()

    def _listenPort(self):
        pass

    def lockBarrier(self):
       pass

    def unlockBarrier(self):
        pass

    def stopExecution(self):
        self._low_level_controller.closePort()

    def run(self):
        self._thread = Thread(target=self._listenPort)
        self._thread.start()
        self._thread = None

