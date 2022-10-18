from PySide6.QtCore import *
from PySide6.QtGui import *

class MyListModel(QAbstractListModel):
    def __init__(self, parent, mylist, *args):
        QAbstractListModel.__init__(self, parent, *args)
        self.mylist = [ x.toString() for x in mylist ] 
        self.my_object_list = mylist

    def rowCount(self, parent):
        return len(self.mylist)

    def data(self, index, role=0):
        return self.mylist[index.row()]

    def setData(self, index, value, role) -> bool:
        self.mylist[index.row()] = value
        #self.dataChanged.emit(index.row(), index.column())
        return True

    def getSelectedData(self, index: QModelIndex):
        return self.my_object_list[index.row()]

    

