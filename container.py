import serial_port.serial_port_controller
import serial_port.simplified_serial_port_controller
import services.buildings
import services.movements
import services.persons
import services.photos
import widgets.main_widget.ui_main_window
import widgets.main_widget.main_widget_class
import utils.logger
from env import BARRIER_1_PORT, BARRIER_2_PORT, BAUDRATE


def build_app():
    movements_service = services.movements.MovementsService()
    buildings_service = services.buildings.BuildingsService()
    persons_service = services.persons.PersonsService()
    photos_service = services.photos.PhotosService()
    logger = utils.logger.Logger()

    """
    barrier1Controller = serial_port.serial_port_controller.SerialPortController(BARRIER_1_PORT, BAUDRATE)
    barrier1Controller.build(persons_service, movements_service, logger)
    barrier2Controller = serial_port.serial_port_controller.SerialPortController(BARRIER_2_PORT, BAUDRATE)
    barrier2Controller.build(persons_service, movements_service, logger)
    """
    barrier1Controller = (serial_port.simplified_serial_port_controller
        .SimplifiedPortController(BARRIER_1_PORT, BAUDRATE))
    barrier1Controller.build(persons_service, movements_service, logger)
    barrier2Controller = (serial_port.simplified_serial_port_controller
        .SimplifiedPortController(BARRIER_2_PORT, BAUDRATE))
    barrier2Controller.build(persons_service, movements_service, logger)
    

    main_ui_form = widgets.main_widget.ui_main_window.Ui_Form()
    
    m_widget = widgets.main_widget.main_widget_class.MainWidget(main_ui_form, 
        movements_service, buildings_service, persons_service, photos_service,
        barrier1Controller, barrier2Controller)

    return m_widget

    
