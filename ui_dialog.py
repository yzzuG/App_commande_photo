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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1000, 600)
        Dialog.setMinimumSize(QSize(1000, 600))
        Dialog.setMaximumSize(QSize(1000, 600))
        Dialog.setStyleSheet(u"background-color:rgb(71,72,73)")
        self.bouton_choisir = QPushButton(Dialog)
        self.bouton_choisir.setObjectName(u"bouton_choisir")
        self.bouton_choisir.setGeometry(QRect(20, 10, 321, 24))
        self.bouton_choisir.setStyleSheet(u"QPushButton {background-color: rgb(100,101,102);\n"
"                                                        color: rgb(255,255,255);\n"
"                                                        border-radius: 7px;\n"
"                                                        text-align: center;}\n"
"                                            QPushButton:hover {background-color: rgb(100,101,150);}\n"
"                                            QPushButton:pressed{background-color: rgb(185,0,92);}\n"
"                                            QPushButton:selected{background-color: rgb(100,101,150);}")
        self.bouton_save = QPushButton(Dialog)
        self.bouton_save.setObjectName(u"bouton_save")
        self.bouton_save.setGeometry(QRect(20, 50, 321, 24))
        self.bouton_save.setStyleSheet(u"QPushButton {background-color: rgb(100,101,102);\n"
"                                                        color: rgb(255,255,255);\n"
"                                                        border-radius: 7px;\n"
"                                                        text-align: center;}\n"
"                                            QPushButton:hover {background-color: rgb(100,101,150);}\n"
"                                            QPushButton:pressed{background-color: rgb(185,0,92);}\n"
"                                            QPushButton:selected{background-color: rgb(100,101,150);}")
        self.checkBox_restrict_mode = QCheckBox(Dialog)
        self.checkBox_restrict_mode.setObjectName(u"checkBox_restrict_mode")
        self.checkBox_restrict_mode.setGeometry(QRect(860, 530, 111, 22))
        self.bouton_fermer = QPushButton(Dialog)
        self.bouton_fermer.setObjectName(u"bouton_fermer")
        self.bouton_fermer.setGeometry(QRect(430, 550, 141, 41))
        self.bouton_fermer.setStyleSheet(u"QPushButton {background-color: rgb(200,101,102);\n"
"                                                    color: rgb(255,255,255);\n"
"                                                    border-radius: 7px;\n"
"                                                    text-align: center;}\n"
"                                            QPushButton:hover {background-color: rgb(100,101,150);}\n"
"                                            QPushButton:pressed{background-color: rgb(185,0,92);}\n"
"                                            QPushButton:selected{background-color: rgb(100,101,150);}")
        self.lineEdit_fili_clair = QLineEdit(Dialog)
        self.lineEdit_fili_clair.setObjectName(u"lineEdit_fili_clair")
        self.lineEdit_fili_clair.setGeometry(QRect(580, 40, 321, 24))
        self.lineEdit_fili_clair.setStyleSheet(u"background-color:rgb(41,42,43);\n"
"border-radius: 5px;\n"
"color: rgb(255,255,255);\n"
"border:none;")
        self.lineEdit_fili_sombre = QLineEdit(Dialog)
        self.lineEdit_fili_sombre.setObjectName(u"lineEdit_fili_sombre")
        self.lineEdit_fili_sombre.setGeometry(QRect(580, 100, 321, 24))
        self.lineEdit_fili_sombre.setStyleSheet(u"background-color:rgb(41,42,43);\n"
"border-radius: 5px;\n"
"color: rgb(255,255,255);\n"
"border:none;")
        self.pushButton_fili_clair = QPushButton(Dialog)
        self.pushButton_fili_clair.setObjectName(u"pushButton_fili_clair")
        self.pushButton_fili_clair.setGeometry(QRect(910, 40, 80, 24))
        self.pushButton_fili_clair.setStyleSheet(u"QPushButton {background-color: rgb(100,101,102);\n"
"                                                        color: rgb(255,255,255);\n"
"                                                        border-radius: 7px;\n"
"                                                        text-align: center;}\n"
"                                            QPushButton:hover {background-color: rgb(100,101,150);}\n"
"                                            QPushButton:pressed{background-color: rgb(185,0,92);}\n"
"                                            QPushButton:selected{background-color: rgb(100,101,150);}")
        self.pushButton_fili_sombre = QPushButton(Dialog)
        self.pushButton_fili_sombre.setObjectName(u"pushButton_fili_sombre")
        self.pushButton_fili_sombre.setGeometry(QRect(910, 100, 80, 24))
        self.pushButton_fili_sombre.setStyleSheet(u"QPushButton {background-color: rgb(100,101,102);\n"
"                                                        color: rgb(255,255,255);\n"
"                                                        border-radius: 7px;\n"
"                                                        text-align: center;}\n"
"                                            QPushButton:hover {background-color: rgb(100,101,150);}\n"
"                                            QPushButton:pressed{background-color: rgb(185,0,92);}\n"
"                                            QPushButton:selected{background-color: rgb(100,101,150);}")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(580, 20, 101, 16))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(580, 80, 101, 16))
        self.pushButton_create_fili = QPushButton(Dialog)
        self.pushButton_create_fili.setObjectName(u"pushButton_create_fili")
        self.pushButton_create_fili.setGeometry(QRect(850, 560, 131, 24))
        self.pushButton_create_fili.setStyleSheet(u"QPushButton {background-color: rgb(100,101,102);\n"
"                                                        color: rgb(255,255,255);\n"
"                                                        border-radius: 7px;\n"
"                                                        text-align: center;}\n"
"                                            QPushButton:hover {background-color: rgb(100,101,150);}\n"
"                                            QPushButton:pressed{background-color: rgb(185,0,92);}\n"
"                                            QPushButton:selected{background-color: rgb(100,101,150);}")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.bouton_choisir.setText(QCoreApplication.translate("Dialog", u"Choisir un nouveau dossier de photo", None))
        self.bouton_save.setText(QCoreApplication.translate("Dialog", u"Choisir un nouveau dossier de photo", None))
        self.checkBox_restrict_mode.setText(QCoreApplication.translate("Dialog", u"restrict_mode", None))
        self.bouton_fermer.setText(QCoreApplication.translate("Dialog", u"Fermer l'interface", None))
        self.pushButton_fili_clair.setText(QCoreApplication.translate("Dialog", u"Parcourir", None))
        self.pushButton_fili_sombre.setText(QCoreApplication.translate("Dialog", u"Parcourir", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Filigrane clair", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Filigrane sombre", None))
        self.pushButton_create_fili.setText(QCoreApplication.translate("Dialog", u"Cr\u00e9er un filigrane", None))
    # retranslateUi

