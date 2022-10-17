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
    low_level_controller: serial_port.low_level_controller.SerialLowLevelController

    def build(self, 
    persons_service: services.persons.PersonsService, movements_service: services.movements.MovementsService, 
    logger: utils.logger.Logger):
        pass

    def _isOpen(self):
        value_ = self.low_level_controller.isOpen()
        self.indicateStatus.emit(value_)
        if not value_: self.showException.emit(f"Порт {self.low_level_controller.port} закрыт!")
        return value_

    def _validatePortData(self, portData: str):
        if not portData or len(portData) == 0:
            return False
        if len(portData.split(";")) != 2:
            return False
        if "@Code" not in portData and "@Direction" not in portData:
            return False
        return True

    def lockBarrier(self):
       pass

    def unlockBarrier(self):
        pass

    def stopExecution(self):
        pass

    def run(self): 
        pass