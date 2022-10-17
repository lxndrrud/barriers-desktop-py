from threading import Thread
from time import sleep
import serial
import serial_port.serial_port_interface
import serial_port.low_level_controller
import services.movements
import services.persons
import services.movements
import utils.logger
import models.port_data

class SimplifiedPortController(serial_port.serial_port_interface.ISerialPortController):
    def __init__(self, port: str, baudrate: int) -> None:
        super().__init__()
        self.low_level_controller = serial_port.low_level_controller.SerialLowLevelController(port, baudrate)
    
    def build(self, 
    persons_service: services.persons.PersonsService, movements_service: services.movements.MovementsService, 
    logger: utils.logger.Logger):
        self.persons_service: services.persons.PersonsService = persons_service
        self.movements_service: services.movements.MovementsService = movements_service
        self.logger: utils.logger.Logger = logger
        self.low_level_controller.build(logger)

    def lockBarrier(self):
        pass

    def unlockBarrier(self):
        pass

    def stopExecution(self):
        self.low_level_controller.closePort()


    def run(self): 
        self.thread = Thread(target=self.__listenPort)
        self.thread.start()

    def __listenPort(self):
        try: self.low_level_controller.openPort()
        except serial.SerialException as e: 
            self.logger.writeToLogs(f"simplified high level {self.low_level_controller.port}: {e}")
        while(self._isOpen()):
            sleep(0.01)
            try:
                # Получить и проверить данные с порта
                strPortData = self.low_level_controller.readFromPort()
                if not self._validatePortData(strPortData): 
                    continue
                portData = models.port_data.PortData(strPortData)
                # Найти человека по карте и проверить валидность
                person = self.persons_service.send_skud_info(portData.code)
                if not person:
                    self.showException.emit(f"simplified high level {self.low_level_controller.port}: Человек не найден!")
                    continue
                self.setLastPerson.emit(person)
                
                returnCode = self.movements_service.create_action(portData)
                if returnCode != 201:
                    (self.showException
                    .emit(f"simplified high level {self.low_level_controller.port}: Человек({portData.code}) прошел({portData.reader}), но не был записан"))
                    (self.logger
                    .writeToLogs(f"simplified high level {self.low_level_controller.port}: Человек({portData.code}) прошел({portData.reader}), но не был записан"))
                # Запросить обновление виджета
                self.afterEventUpdated.emit()
            except Exception as e:
                self.showException.emit(f"simplified high level {self.low_level_controller.port} listen: {e}")
                self.logger.writeToLogs(f"simplified high level {self.low_level_controller.port} listen: {e}")
    