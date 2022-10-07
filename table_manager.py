from models.table_model import MyTableModel
from services.movements import MovementsService
from models.movement import ext_movement_to_tuple
from PySide6.QtWidgets import QTableView

class TableManager:
    widget: QTableView
    movementService: MovementsService
    
    def __init__(self, widget: QTableView, movementsService: MovementsService) -> None:
        self.movementService = movementsService
        self.widget = widget
        self.widget.setModel(MyTableModel(self.widget, [("kek", "kek","kek", "kek", "kek","kek", "kek","kek")]))
        #self.get_all_and_set_data()

    def get_all_and_set_data(self, id_building=None, from_=None, to_=None):
        movements_list = self.movementService.get_all(id_building, from_, to_)
        mapped = []
        for movement in movements_list: mapped.append(ext_movement_to_tuple(movement))
        self.widget.setModel(MyTableModel(self.widget, mapped or [("kek", "kek","kek", "kek", "kek","kek", "kek","kek")]))
        
