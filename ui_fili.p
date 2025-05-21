# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fili.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPlainTextEdit,
    QPushButton, QSizePolicy, QSlider, QSpinBox,
    QWidget)

class Ui_Fili(object):
    def setupUi(self, Fili):
        if not Fili.objectName():
            Fili.setObjectName(u"Fili")
        Fili.resize(1241, 542)
        Fili.setMinimumSize(QSize(1241, 542))
        Fili.setMaximumSize(QSize(1241, 16777215))
        Fili.setStyleSheet(u"background-color:rgb(71,72,73)")
        self.filigrane_label = QLabel(Fili)
        self.filigrane_label.setObjectName(u"filigrane_label")
        self.filigrane_label.setGeometry(QRect(20, 220, 1200, 250))
        self.filigrane_label.setStyleSheet(u"background-color:rgb(41,42,43)")
        self.filigrane_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.selectLogoButton = QPushButton(Fili)
        self.selectLogoButton.setObjectName(u"selectLogoButton")
        self.selectLogoButton.setGeometry(QRect(30, 30, 101, 31))
        self.selectLogoButton.setStyleSheet(u"/* QPush BUTTON */\n"
"QPushButton {\n"
"	background-color: rgb(100,101,102);\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 7px;\n"
"    text-align: center;}\n"
"QPushButton:hover {\n"
"	background-color: rgb(100,101,150);}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(185,0,92);}\n"
"QPushButton:selected{\n"
"	background-color: rgb(100,101,150);}")
        self.generateButton = QPushButton(Fili)
        self.generateButton.setObjectName(u"generateButton")
        self.generateButton.setGeometry(QRect(580, 500, 80, 24))
        self.generateButton.setStyleSheet(u"/* QPush BUTTON */\n"
"QPushButton {\n"
"	background-color: rgb(100,101,102);\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 7px;\n"
"    text-align: center;}\n"
"QPushButton:hover {\n"
"	background-color: rgb(100,101,150);}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(185,0,92);}\n"
"QPushButton:selected{\n"
"	background-color: rgb(100,101,150);}")
        self.fontSizeSpinBox = QSpinBox(Fili)
        self.fontSizeSpinBox.setObjectName(u"fontSizeSpinBox")
        self.fontSizeSpinBox.setGeometry(QRect(570, 180, 121, 25))
        self.fontSizeSpinBox.setMinimum(6)
        self.fontSizeSpinBox.setMaximum(72)
        self.fontSizeSpinBox.setValue(24)
        self.leftTextXOffsetSlider = QSlider(Fili)
        self.leftTextXOffsetSlider.setObjectName(u"leftTextXOffsetSlider")
        self.leftTextXOffsetSlider.setGeometry(QRect(20, 190, 501, 20))
        self.leftTextXOffsetSlider.setMinimum(-300)
        self.leftTextXOffsetSlider.setMaximum(300)
        self.leftTextXOffsetSlider.setSingleStep(10)
        self.leftTextXOffsetSlider.setValue(140)
        self.leftTextXOffsetSlider.setOrientation(Qt.Orientation.Horizontal)
        self.leftTextXOffsetSlider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.rightTextXOffsetSlider = QSlider(Fili)
        self.rightTextXOffsetSlider.setObjectName(u"rightTextXOffsetSlider")
        self.rightTextXOffsetSlider.setGeometry(QRect(720, 190, 501, 20))
        self.rightTextXOffsetSlider.setMinimum(-300)
        self.rightTextXOffsetSlider.setMaximum(300)
        self.rightTextXOffsetSlider.setSingleStep(10)
        self.rightTextXOffsetSlider.setValue(-80)
        self.rightTextXOffsetSlider.setOrientation(Qt.Orientation.Horizontal)
        self.rightTextXOffsetSlider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.leftTextLineEdit = QPlainTextEdit(Fili)
        self.leftTextLineEdit.setObjectName(u"leftTextLineEdit")
        self.leftTextLineEdit.setGeometry(QRect(130, 100, 281, 70))
        self.rightTextLineEdit = QPlainTextEdit(Fili)
        self.rightTextLineEdit.setObjectName(u"rightTextLineEdit")
        self.rightTextLineEdit.setGeometry(QRect(830, 100, 281, 70))
        self.logoPathLabel = QLabel(Fili)
        self.logoPathLabel.setObjectName(u"logoPathLabel")
        self.logoPathLabel.setGeometry(QRect(150, 35, 491, 21))

        self.retranslateUi(Fili)

        QMetaObject.connectSlotsByName(Fili)
    # setupUi

    def retranslateUi(self, Fili):
        Fili.setWindowTitle(QCoreApplication.translate("Fili", u"Dialog", None))
        self.filigrane_label.setText(QCoreApplication.translate("Fili", u"Filigrane", None))
        self.selectLogoButton.setText(QCoreApplication.translate("Fili", u"Choisir le logo", None))
        self.generateButton.setText(QCoreApplication.translate("Fili", u"Sauvegarder", None))
        self.logoPathLabel.setText("")
    # retranslateUi

