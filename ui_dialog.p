# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(300, 200)
        Dialog.setMinimumSize(QSize(300, 200))
        Dialog.setMaximumSize(QSize(300, 200))
        Dialog.setStyleSheet(u"background-color:rgb(71,72,73)")
        self.bouton_save = QPushButton(Dialog)
        self.bouton_save.setObjectName(u"bouton_save")
        self.bouton_save.setGeometry(QRect(40, 60, 231, 24))
        self.bouton_save.setStyleSheet(u"QPushButton {background-color: rgb(100,101,102);\n"
"                                                    color: rgb(255,255,255);\n"
"                                                    border-radius: 7px;\n"
"                                                    text-align: center;}\n"
"                                            QPushButton:hover {background-color: rgb(100,101,150);}\n"
"                                            QPushButton:pressed{background-color: rgb(185,0,92);}\n"
"                                            QPushButton:selected{background-color: rgb(100,101,150);}")
        self.bouton_fermer = QPushButton(Dialog)
        self.bouton_fermer.setObjectName(u"bouton_fermer")
        self.bouton_fermer.setGeometry(QRect(100, 150, 111, 24))
        self.bouton_fermer.setStyleSheet(u"QPushButton {background-color: rgb(200,101,102);\n"
"                                                    color: rgb(255,255,255);\n"
"                                                    border-radius: 7px;\n"
"                                                    text-align: center;}\n"
"                                            QPushButton:hover {background-color: rgb(100,101,150);}\n"
"                                            QPushButton:pressed{background-color: rgb(185,0,92);}\n"
"                                            QPushButton:selected{background-color: rgb(100,101,150);}")
        self.bouton_choisir = QPushButton(Dialog)
        self.bouton_choisir.setObjectName(u"bouton_choisir")
        self.bouton_choisir.setGeometry(QRect(40, 20, 231, 24))
        self.bouton_choisir.setStyleSheet(u"QPushButton {background-color: rgb(100,101,102);\n"
"                                                        color: rgb(255,255,255);\n"
"                                                        border-radius: 7px;\n"
"                                                        text-align: center;}\n"
"                                            QPushButton:hover {background-color: rgb(100,101,150);}\n"
"                                            QPushButton:pressed{background-color: rgb(185,0,92);}\n"
"                                            QPushButton:selected{background-color: rgb(100,101,150);}")
        self.restrict_mode = QCheckBox(Dialog)
        self.restrict_mode.setObjectName(u"restrict_mode")
        self.restrict_mode.setGeometry(QRect(40, 110, 131, 22))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.bouton_save.setText(QCoreApplication.translate("Dialog", u"Choisir un nouveau dossier sauvegarde", None))
        self.bouton_fermer.setText(QCoreApplication.translate("Dialog", u"Fermer l'interface", None))
        self.bouton_choisir.setText(QCoreApplication.translate("Dialog", u"Choisir un nouveau dossier de photo", None))
        self.restrict_mode.setText(QCoreApplication.translate("Dialog", u"Mode restreint", None))
    # retranslateUi

