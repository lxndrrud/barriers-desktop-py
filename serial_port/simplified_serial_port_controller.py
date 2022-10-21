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
        self._low_level_controller = serial_port.low_level_controller.SerialLowLevelController(port, baudrate)
    
    def build(self, 
    persons_service: services.persons.PersonsService, movements_service: services.movements.MovementsService, 
    logger: utils.logger.Logger):
        self.persons_service: services.persons.PersonsService = persons_service
        self.movements_service: services.movements.MovementsService = movements_service
        self.logger: utils.logger.Logger = logger
        self._low_level_controller.build(logger)

    def lockBarrier(self):
        pass

    def unlockBarrier(self):
        pass

    def _listenPort(self):
        # Цикл прослушки
        while(self._isOpen()):
            try:
                # Получить и проверить данные с порта
                strPortData = self._low_level_controller.readFromPort()
                if not self._validatePortData(strPortData): 
                    continue
                portData = models.port_data.PortData(strPortData)
                # Найти человека по карте и проверить валидность
                person = self.persons_service.send_skud_info(portData.code)
                if not person:
                    self._alarmBarrier(portData.reader)
                    continue
                # Запустить callback отрисовки последнего отсканированного чела
                self.setLastPerson.emit(person)
                # Создать перемещение на сервере
                returnCode = self.movements_service.create_action(portData)
                if returnCode != 201:
                    (self.showException
                    .emit(f"simplified high level {self._low_level_controller.port}: Человек({portData.code}) прошел({portData.reader}), но не был записан"))
                    (self.logger
                    .writeToLogs(f"simplified high level {self._low_level_controller.port}: Человек({portData.code}) прошел({portData.reader}), но не был записан"))
                # Запустить callback обновления таблицы перемещений
                self.afterEventUpdated.emit()
            except Exception as e:
                self.showException.emit(f"simplified high level {self._low_level_controller.port} listen: {e}")
                self.logger.writeToLogs(f"simplified high level {self._low_level_controller.port} listen: {e}")
    
