# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_personal_movement_modal.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QGroupBox,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableView, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1200, 900)
        self.personPhoto = QLabel(Form)
        self.personPhoto.setObjectName(u"personPhoto")
        self.personPhoto.setGeometry(QRect(20, 10, 200, 200))
        self.personPhoto.setAutoFillBackground(True)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 230, 771, 481))
        self.tableView = QTableView(self.groupBox)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(0, 20, 771, 461))
        self.personFullname = QTextEdit(Form)
        self.personFullname.setObjectName(u"personFullname")
        self.personFullname.setGeometry(QRect(240, 10, 371, 31))
        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(800, 230, 321, 261))
        self.fromTime = QDateTimeEdit(self.groupBox_2)
        self.fromTime.setObjectName(u"fromTime")
        self.fromTime.setGeometry(QRect(60, 50, 194, 26))
        self.fromTime.setDateTime(QDateTime(QDate(2022, 1, 1), QTime(15, 0, 0)))
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 30, 67, 17))
        self.toTime = QDateTimeEdit(self.groupBox_2)
        self.toTime.setObjectName(u"toTime")
        self.toTime.setGeometry(QRect(60, 100, 194, 26))
        self.toTime.setDateTime(QDateTime(QDate(2022, 1, 1), QTime(9, 0, 0)))
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 80, 67, 17))
        self.buildingSelect = QComboBox(self.groupBox_2)
        self.buildingSelect.setObjectName(u"buildingSelect")
        self.buildingSelect.setGeometry(QRect(60, 130, 191, 25))
        self.updateMovements = QPushButton(self.groupBox_2)
        self.updateMovements.setObjectName(u"updateMovements")
        self.updateMovements.setGeometry(QRect(60, 180, 191, 25))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0447\u0435\u043b\u043e\u0432\u0435\u043a\u0435", None))
        self.personPhoto.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u041f\u0435\u0440\u0441\u043e\u043d\u0430\u043b\u044c\u043d\u044b\u0435 \u043f\u0435\u0440\u0435\u043c\u0435\u0449\u0435\u043d\u0438\u044f", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u0424\u0438\u043b\u044c\u0442\u0440", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041e\u0442", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0414\u043e", None))
        self.updateMovements.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
    # retranslateUi

