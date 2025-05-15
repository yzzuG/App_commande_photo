# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frame.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QPushButton, QSizePolicy,
    QWidget)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(300, 200)
        Frame.setMinimumSize(QSize(300, 200))
        Frame.setMaximumSize(QSize(300, 200))
        Frame.setStyleSheet(u"background-color:rgb(71,72,73)")
        self.bouton_choisir = QPushButton(Frame)
        self.bouton_choisir.setObjectName(u"bouton_choisir")
        self.bouton_choisir.setGeometry(QRect(30, 30, 231, 24))
        self.bouton_choisir.setStyleSheet(u"QPushButton {background-color: rgb(100,101,102);\n"
"                                                        color: rgb(255,255,255);\n"
"                                                        border-radius: 7px;\n"
"                                                        text-align: center;}\n"
"                                            QPushButton:hover {background-color: rgb(100,101,150);}\n"
"                                            QPushButton:pressed{background-color: rgb(185,0,92);}\n"
"                                            QPushButton:selected{background-color: rgb(100,101,150);}")
        self.bouton_save = QPushButton(Frame)
        self.bouton_save.setObjectName(u"bouton_save")
        self.bouton_save.setGeometry(QRect(30, 70, 231, 24))
        self.bouton_save.setStyleSheet(u"QPushButton {background-color: rgb(100,101,102);\n"
"                                                    color: rgb(255,255,255);\n"
"                                                    border-radius: 7px;\n"
"                                                    text-align: center;}\n"
"                                            QPushButton:hover {background-color: rgb(100,101,150);}\n"
"                                            QPushButton:pressed{background-color: rgb(185,0,92);}\n"
"                                            QPushButton:selected{background-color: rgb(100,101,150);}")
        self.bouton_fermer = QPushButton(Frame)
        self.bouton_fermer.setObjectName(u"bouton_fermer")
        self.bouton_fermer.setGeometry(QRect(90, 160, 111, 24))
        self.bouton_fermer.setStyleSheet(u"QPushButton {background-color: rgb(200,101,102);\n"
"                                                    color: rgb(255,255,255);\n"
"                                                    border-radius: 7px;\n"
"                                                    text-align: center;}\n"
"                                            QPushButton:hover {background-color: rgb(100,101,150);}\n"
"                                            QPushButton:pressed{background-color: rgb(185,0,92);}\n"
"                                            QPushButton:selected{background-color: rgb(100,101,150);}")

        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.bouton_choisir.setText(QCoreApplication.translate("Frame", u"Choisir un nouveau dossier de photo", None))
        self.bouton_save.setText(QCoreApplication.translate("Frame", u"Choisir un nouveau dossier sauvegarde", None))
        self.bouton_fermer.setText(QCoreApplication.translate("Frame", u"Fermer l'interface", None))
    # retranslateUi

