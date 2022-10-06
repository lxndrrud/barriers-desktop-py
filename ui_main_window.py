# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDateTimeEdit, QGroupBox,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableView, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1200, 800)
        self.tableWidget = QTableView(Form)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(1, 31, 821, 641))
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(840, 10, 351, 659))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setBaseSize(QSize(200, 0))
        self.updateMovements = QPushButton(self.groupBox)
        self.updateMovements.setObjectName(u"updateMovements")
        self.updateMovements.setGeometry(QRect(0, 220, 111, 25))
        self.openBarrier1 = QPushButton(self.groupBox)
        self.openBarrier1.setObjectName(u"openBarrier1")
        self.openBarrier1.setGeometry(QRect(0, 250, 111, 25))
        self.closeBarrier1 = QPushButton(self.groupBox)
        self.closeBarrier1.setObjectName(u"closeBarrier1")
        self.closeBarrier1.setGeometry(QRect(0, 280, 111, 25))
        self.openBarrier2 = QPushButton(self.groupBox)
        self.openBarrier2.setObjectName(u"openBarrier2")
        self.openBarrier2.setGeometry(QRect(0, 310, 111, 25))
        self.closeBarrier2 = QPushButton(self.groupBox)
        self.closeBarrier2.setObjectName(u"closeBarrier2")
        self.closeBarrier2.setGeometry(QRect(0, 340, 111, 25))
        self.dateTimeEdit = QDateTimeEdit(self.groupBox)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setGeometry(QRect(10, 60, 194, 26))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 40, 67, 17))
        self.dateTimeEdit_2 = QDateTimeEdit(self.groupBox)
        self.dateTimeEdit_2.setObjectName(u"dateTimeEdit_2")
        self.dateTimeEdit_2.setGeometry(QRect(10, 120, 194, 26))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 100, 67, 17))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0422\u0443\u0440\u043d\u0438\u043a\u0435\u0442\u044b \u041b\u0413\u041f\u0423", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u041a\u043e\u043d\u0442\u0440\u043e\u043b\u044c", None))
        self.updateMovements.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.openBarrier1.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c 1", None))
        self.closeBarrier1.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c 1", None))
        self.openBarrier2.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c 2", None))
        self.closeBarrier2.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c 2", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041e\u0442", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0414\u043e", None))
    # retranslateUi

