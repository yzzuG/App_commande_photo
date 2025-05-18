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
        self.bouton_save = QPushButton(Dialog)
        self.bouton_save.setObjectName(u"bouton_save")
        self.bouton_save.setGeometry(QRect(40, 90, 321, 24))
        self.bouton_save.setStyleSheet(u"QPushButton {background-color: rgb(100,101,102);\n"
"                                                    color: rgb(255,255,255);\n"
"                                                    border-radius: 7px;\n"
"                                                    text-align: center;}\n"
"                                            QPushButton:hover {background-color: rgb(100,101,150);}\n"
"                                            QPushButton:pressed{background-color: rgb(185,0,92);}\n"
"                                            QPushButton:selected{background-color: rgb(100,101,150);}")
        self.bouton_fermer = QPushButton(Dialog)
        self.bouton_fermer.setObjectName(u"bouton_fermer")
        self.bouton_fermer.setGeometry(QRect(440, 570, 121, 24))
        self.bouton_fermer.setStyleSheet(u"QPushButton {background-color: rgb(200,101,102);\n"
"                                                    color: rgb(255,255,255);\n"
"                                                    border-radius: 7px;\n"
"                                                    text-align: center;}\n"
"                                            QPushButton:hover {background-color: rgb(100,101,150);}\n"
"                                            QPushButton:pressed{background-color: rgb(185,0,92);}\n"
"                                            QPushButton:selected{background-color: rgb(100,101,150);}")
        self.bouton_choisir = QPushButton(Dialog)
        self.bouton_choisir.setObjectName(u"bouton_choisir")
        self.bouton_choisir.setGeometry(QRect(40, 20, 321, 24))
        self.bouton_choisir.setStyleSheet(u"QPushButton {background-color: rgb(100,101,102);\n"
"                                                        color: rgb(255,255,255);\n"
"                                                        border-radius: 7px;\n"
"                                                        text-align: center;}\n"
"                                            QPushButton:hover {background-color: rgb(100,101,150);}\n"
"                                            QPushButton:pressed{background-color: rgb(185,0,92);}\n"
"                                            QPushButton:selected{background-color: rgb(100,101,150);}")
        self.checkBox_restrict_mode = QCheckBox(Dialog)
        self.checkBox_restrict_mode.setObjectName(u"checkBox_restrict_mode")
        self.checkBox_restrict_mode.setGeometry(QRect(850, 530, 131, 22))
        self.checkBox_restrict_mode.setStyleSheet(u"color: white;")
        self.lineEdit_fili_clair = QLineEdit(Dialog)
        self.lineEdit_fili_clair.setObjectName(u"lineEdit_fili_clair")
        self.lineEdit_fili_clair.setGeometry(QRect(530, 30, 231, 24))
        self.lineEdit_fili_clair.setStyleSheet(u"border:none;\n"
"border-radius : 5px;\n"
"background-color:rgb(101,102,103);color:#FFFFFF;")
        self.lineEdit_fili_clair.setReadOnly(True)
        self.label_fili_clair = QLabel(Dialog)
        self.label_fili_clair.setObjectName(u"label_fili_clair")
        self.label_fili_clair.setGeometry(QRect(530, 10, 81, 16))
        self.label_fili_clair.setStyleSheet(u"color: white;")
        self.pushButton_fili_clair = QPushButton(Dialog)
        self.pushButton_fili_clair.setObjectName(u"pushButton_fili_clair")
        self.pushButton_fili_clair.setGeometry(QRect(770, 30, 80, 24))
        self.pushButton_fili_clair.setStyleSheet(u"QPushButton {background-color: rgb(100,101,102);\n"
"                                                    color: rgb(255,255,255);\n"
"                                                    border-radius: 7px;\n"
"                                                    text-align: center;}\n"
"                                            QPushButton:hover {background-color: rgb(100,101,150);}\n"
"                                            QPushButton:pressed{background-color: rgb(185,0,92);}\n"
"                                            QPushButton:selected{background-color: rgb(100,101,150);}")
        self.pushButton_fili_sombre = QPushButton(Dialog)
        self.pushButton_fili_sombre.setObjectName(u"pushButton_fili_sombre")
        self.pushButton_fili_sombre.setGeometry(QRect(770, 210, 80, 24))
        self.pushButton_fili_sombre.setStyleSheet(u"QPushButton {background-color: rgb(100,101,102);\n"
"                                                    color: rgb(255,255,255);\n"
"                                                    border-radius: 7px;\n"
"                                                    text-align: center;}\n"
"                                            QPushButton:hover {background-color: rgb(100,101,150);}\n"
"                                            QPushButton:pressed{background-color: rgb(185,0,92);}\n"
"                                            QPushButton:selected{background-color: rgb(100,101,150);}")
        self.label_fili_sombre = QLabel(Dialog)
        self.label_fili_sombre.setObjectName(u"label_fili_sombre")
        self.label_fili_sombre.setGeometry(QRect(530, 190, 101, 16))
        self.label_fili_sombre.setStyleSheet(u"color: white;")
        self.lineEdit_fili_sombre = QLineEdit(Dialog)
        self.lineEdit_fili_sombre.setObjectName(u"lineEdit_fili_sombre")
        self.lineEdit_fili_sombre.setGeometry(QRect(530, 210, 231, 24))
        self.lineEdit_fili_sombre.setStyleSheet(u"border:none;\n"
"border-radius : 5px;\n"
"background-color:rgb(101,102,103);color:#FFFFFF;")
        self.lineEdit_fili_sombre.setReadOnly(True)
        self.pushButton_create_fili = QPushButton(Dialog)
        self.pushButton_create_fili.setObjectName(u"pushButton_create_fili")
        self.pushButton_create_fili.setGeometry(QRect(850, 480, 141, 41))
        self.pushButton_create_fili.setStyleSheet(u"QPushButton {background-color: rgb(100,101,102);\n"
"                                                    color: rgb(255,255,255);\n"
"                                                    border-radius: 7px;\n"
"                                                    text-align: center;}\n"
"                                            QPushButton:hover {background-color: rgb(100,101,150);}\n"
"                                            QPushButton:pressed{background-color: rgb(185,0,92);}\n"
"                                            QPushButton:selected{background-color: rgb(100,101,150);}")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.bouton_save.setText(QCoreApplication.translate("Dialog", u"Choisir un nouveau dossier sauvegarde", None))
        self.bouton_fermer.setText(QCoreApplication.translate("Dialog", u"Fermer l'interface", None))
        self.bouton_choisir.setText(QCoreApplication.translate("Dialog", u"Choisir un nouveau dossier de photo", None))
        self.checkBox_restrict_mode.setText(QCoreApplication.translate("Dialog", u"Mode restreint", None))
        self.label_fili_clair.setText(QCoreApplication.translate("Dialog", u"Filigrane clair : ", None))
        self.pushButton_fili_clair.setText(QCoreApplication.translate("Dialog", u"Parcourir", None))
        self.pushButton_fili_sombre.setText(QCoreApplication.translate("Dialog", u"Parcourir", None))
        self.label_fili_sombre.setText(QCoreApplication.translate("Dialog", u"Filigrane sombre : ", None))
        self.pushButton_create_fili.setText(QCoreApplication.translate("Dialog", u"Cr\u00e9ation de filigrane", None))
    # retranslateUi

