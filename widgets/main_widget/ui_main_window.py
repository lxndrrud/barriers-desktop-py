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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QGroupBox,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableView, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1200, 841)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(840, 10, 351, 591))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setBaseSize(QSize(200, 0))
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 40, 321, 261))
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
        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(20, 440, 151, 111))
        self.openBarrier1 = QPushButton(self.groupBox_3)
        self.openBarrier1.setObjectName(u"openBarrier1")
        self.openBarrier1.setGeometry(QRect(20, 40, 111, 25))
        self.closeBarrier1 = QPushButton(self.groupBox_3)
        self.closeBarrier1.setObjectName(u"closeBarrier1")
        self.closeBarrier1.setGeometry(QRect(20, 70, 111, 25))
        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(190, 440, 151, 111))
        self.openBarrier2 = QPushButton(self.groupBox_4)
        self.openBarrier2.setObjectName(u"openBarrier2")
        self.openBarrier2.setGeometry(QRect(20, 40, 111, 25))
        self.closeBarrier2 = QPushButton(self.groupBox_4)
        self.closeBarrier2.setObjectName(u"closeBarrier2")
        self.closeBarrier2.setGeometry(QRect(20, 70, 111, 25))
        self.groupBox_6 = QGroupBox(self.groupBox)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(20, 320, 321, 80))
        self.personMovementsButton = QPushButton(self.groupBox_6)
        self.personMovementsButton.setObjectName(u"personMovementsButton")
        self.personMovementsButton.setGeometry(QRect(60, 40, 191, 25))
        self.tableView = QTableView(Form)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(10, 30, 811, 571))
        font = QFont()
        font.setPointSize(8)
        font.setKerning(True)
        self.tableView.setFont(font)
        self.tableView.setShowGrid(True)
        self.tableView.setSortingEnabled(True)
        self.tableView.setCornerButtonEnabled(False)
        self.groupBox_5 = QGroupBox(Form)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(10, 610, 811, 221))
        self.lastPersonLabel = QLabel(self.groupBox_5)
        self.lastPersonLabel.setObjectName(u"lastPersonLabel")
        self.lastPersonLabel.setGeometry(QRect(0, 20, 200, 200))
        self.lastPersonLabel.setAutoFillBackground(True)
        self.lastPersonLabel.setOpenExternalLinks(True)
        self.lastPersonLabel.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
        self.lastPersonFullname = QTextEdit(self.groupBox_5)
        self.lastPersonFullname.setObjectName(u"lastPersonFullname")
        self.lastPersonFullname.setGeometry(QRect(220, 30, 401, 31))
        self.lastPersonFullname.setReadOnly(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0422\u0443\u0440\u043d\u0438\u043a\u0435\u0442\u044b \u041b\u0413\u041f\u0423", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u041a\u043e\u043d\u0442\u0440\u043e\u043b\u044c", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u0424\u0438\u043b\u044c\u0442\u0440", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041e\u0442", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0414\u043e", None))
        self.updateMovements.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"\u0422\u0443\u0440\u043d\u0438\u043a\u0435\u0442 #1", None))
        self.openBarrier1.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c 1", None))
        self.closeBarrier1.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c 1", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"\u0422\u0443\u0440\u043d\u0438\u043a\u0435\u0442 #2", None))
        self.openBarrier2.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c 2", None))
        self.closeBarrier2.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c 2", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Form", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043d\u0430 \u0447\u0435\u043b\u043e\u0432\u0435\u043a\u0430", None))
        self.personMovementsButton.setText(QCoreApplication.translate("Form", u"\u041f\u0435\u0440\u0435\u043c\u0435\u0449\u0435\u043d\u0438\u044f", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Form", u"\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0439 \u043f\u0440\u043e\u0441\u043a\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0447\u0435\u043b\u043e\u0432\u0435\u043a", None))
        self.lastPersonLabel.setText("")
    # retranslateUi

