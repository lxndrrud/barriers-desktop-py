from PySide6.QtCore import *
from PySide6.QtGui import *

class MyTableModel(QAbstractTableModel):
    def __init__(self, parent, mylist, header, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.mylist = mylist
        self.my_object_list = [ tuple_[0] for tuple_ in self.mylist ]
        self.header = header

    def rowCount(self, parent):
        return len(self.mylist)

    def columnCount(self, parent):
        return len(self.header)

    def data(self, index, role=0):
        return self.mylist[index.row()][index.column() + 1]

    def setData(self, index, value, role) -> bool:
        self.mylist[index.row()][index.column() + 1] = value
        #self.dataChanged.emit(index.row(), index.column())
        return True

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None

    def getSelectedData(self, index: QModelIndex):
        return self.my_object_list[index.row()]

    

