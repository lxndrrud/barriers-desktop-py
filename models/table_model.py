from PySide6.QtCore import *
from PySide6.QtGui import *

class MyTableModel(QAbstractTableModel):
    def __init__(self, parent, mylist, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.mylist = mylist
        self.header = ('Здание', 'Событие', 'Время', 'Имя', 'Отчество', 'Фамилия', 'СКУД', 'Тип')

    def rowCount(self, parent):
        return len(self.mylist)

    def columnCount(self, parent):
        return len(self.header)

    def data(self, index, role=0):
        return self.mylist[index.row()][index.column()]

    def setData(self, index, value, role) -> bool:
        self.mylist[index.row()][index.column()] = value
        self.dataChanged.emit(index, index)
        return True

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None

    

