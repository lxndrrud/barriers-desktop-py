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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHeaderView, QLabel,
    QSizePolicy, QTableView, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1072, 738)
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

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0447\u0435\u043b\u043e\u0432\u0435\u043a\u0435", None))
        self.personPhoto.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u041f\u0435\u0440\u0441\u043e\u043d\u0430\u043b\u044c\u043d\u044b\u0435 \u043f\u0435\u0440\u0435\u043c\u0435\u0449\u0435\u043d\u0438\u044f", None))
    # retranslateUi

