from time import sleep
import serial
import models.port_data
import services.persons
import services.movements
import utils.logger
import serial_port.low_level_controller
import serial_port.serial_port_interface

class SerialPortController(serial_port.serial_port_interface.ISerialPortController):
    def __init__(self, port: str, baudrate: int) -> None:
        super().__init__()
        self._low_level_controller = serial_port.low_level_controller.SerialLowLevelController(port, baudrate)
    
    def build(self, 
    persons_service: services.persons.PersonsService, movements_service: services.movements.MovementsService, logger: utils.logger.Logger):
        self.persons_service: services.persons.PersonsService = persons_service
        self.movements_service: services.movements.MovementsService = movements_service
        self.logger: utils.logger.Logger = logger
        self._low_level_controller.build(logger)

    def __openBarrierTimeout(self, reader: str):
        check = self._low_level_controller.writeToPort("@Code=user-success;@reader=" + reader)
        if not check: self.showException.emit(f"high level {self._low_level_controller.port}->Турникет не открыт->Ошибка записи в порт!")

    def lockBarrier(self):
        check = self._low_level_controller.writeToPort("@Code=lock;@reader=both")
        if not check : self.showException.emit(f"high level {self._low_level_controller.port}->Турникет не закрыт->Ошибка записи в порт!")

    def unlockBarrier(self):
        check = self._low_level_controller.writeToPort("@Code=unlock;@reader=both")
        if not check: self.showException.emit(f"high level {self._low_level_controller.port}->Турникет не открыт->Ошибка записи в порт!") 

    def _listenPort(self):
        """
        try: self._low_level_controller.openPort()
        except serial.SerialException as e: 
            self.logger.writeToLogs(f"high level {self._low_level_controller.port}: {e}")
        """
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
                self.setLastPerson.emit(person)
                # Проверка совершенного действия, раз в 100 мс
                actionPerfomed: bool = False
                self.__openBarrierTimeout(portData.reader)
                for _ in range(35 + 10):
                    fromPort = self._low_level_controller.readFromPort()
                    if fromPort and portData.reader + "-success" in fromPort:
                        returnCode = self.movements_service.create_action(portData)
                        if returnCode != 201:
                            (self.showException
                            .emit(f"high level {self._low_level_controller.port}: Человек({portData.code}) прошел({portData.reader}), но не был записан"))
                            (self.logger
                            .writeToLogs(f"high level {self._low_level_controller.port}: Человек({portData.code}) прошел({portData.reader}), но не был записан"))
                        actionPerfomed = True
                        break
                # Записать неудачу при проходе, если турникет не прокручен
                if not actionPerfomed:
                    self.movements_service.create_action(portData, failAction=True)
                # Запросить обновление виджета
                self.afterEventUpdated.emit()
            except Exception as e:
                self.showException.emit(f"high level {self._low_level_controller.port} listen: {e}")
                self.logger.writeToLogs(f"high level {self._low_level_controller.port} listen: {e}")

    


