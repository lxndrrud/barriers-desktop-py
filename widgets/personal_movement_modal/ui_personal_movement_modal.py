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
    QHeaderView, QLabel, QListView, QPushButton,
    QSizePolicy, QTableView, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1150, 750)
        Form.setMinimumSize(QSize(1150, 750))
        Form.setMaximumSize(QSize(1150, 750))
        self.personPhoto = QLabel(Form)
        self.personPhoto.setObjectName(u"personPhoto")
        self.personPhoto.setGeometry(QRect(20, 10, 200, 200))
        self.personPhoto.setAutoFillBackground(False)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 230, 771, 481))
        self.tableView = QTableView(self.groupBox)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(0, 20, 771, 461))
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
        self.list = QGroupBox(Form)
        self.list.setObjectName(u"list")
        self.list.setGeometry(QRect(240, 70, 371, 141))
        self.infoListView = QListView(self.list)
        self.infoListView.setObjectName(u"infoListView")
        self.infoListView.setGeometry(QRect(0, 20, 371, 121))
        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(640, 70, 151, 51))
        self.skudCard = QTextEdit(self.groupBox_3)
        self.skudCard.setObjectName(u"skudCard")
        self.skudCard.setGeometry(QRect(0, 20, 151, 31))
        self.skudCard.setReadOnly(True)
        self.groupBox_4 = QGroupBox(Form)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(240, 0, 371, 51))
        self.personFullname = QTextEdit(self.groupBox_4)
        self.personFullname.setObjectName(u"personFullname")
        self.personFullname.setGeometry(QRect(0, 20, 371, 31))
        self.personFullname.setReadOnly(True)
        self.groupBox_5 = QGroupBox(Form)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(640, 0, 151, 51))
        self.typePerson = QTextEdit(self.groupBox_5)
        self.typePerson.setObjectName(u"typePerson")
        self.typePerson.setGeometry(QRect(0, 20, 151, 31))
        self.typePerson.setReadOnly(True)

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
        self.list.setTitle(QCoreApplication.translate("Form", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0433\u0440\u0443\u043f\u043f\u0430\u0445/\u0434\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044f\u0445", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"\u0421\u041a\u0423\u0414", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"\u0424\u0418\u041e", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Form", u"\u0422\u0438\u043f", None))
    # retranslateUi

