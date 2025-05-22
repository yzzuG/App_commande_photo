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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QDialog,
    QDoubleSpinBox, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpinBox, QWidget)

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
        self.lineEdit_fili_clair.setGeometry(QRect(530, 40, 371, 24))
        self.lineEdit_fili_clair.setStyleSheet(u"background-color:rgb(41,42,43);\n"
"border-radius: 5px;\n"
"color: rgb(255,255,255);\n"
"border:none;")
        self.lineEdit_fili_sombre = QLineEdit(Dialog)
        self.lineEdit_fili_sombre.setObjectName(u"lineEdit_fili_sombre")
        self.lineEdit_fili_sombre.setGeometry(QRect(530, 100, 371, 24))
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
        self.label_fili_clair = QLabel(Dialog)
        self.label_fili_clair.setObjectName(u"label_fili_clair")
        self.label_fili_clair.setGeometry(QRect(530, 20, 101, 16))
        self.label_fili_sombre = QLabel(Dialog)
        self.label_fili_sombre.setObjectName(u"label_fili_sombre")
        self.label_fili_sombre.setGeometry(QRect(530, 80, 101, 16))
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
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 160, 291, 271))
        self.frame.setStyleSheet(u"QLabel{\n"
"	color:rgb(160,160,160);\n"
"	border : none;\n"
"}\n"
"\n"
"QFrame{\n"
"	border-radius:5px;\n"
"	border:none\n"
"}\n"
"\n"
"QSpinBox {\n"
"   background-color: rgb(41,42,43);\n"
"	color:rgb(160,160,160);\n"
"}\n"
"\n"
"QDoubleSpinBox{\n"
"	background-color:rgb(41,42,43);\n"
"	color:rgb(160,160,160);\n"
"	border:none;\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QCheckBox::indicator {\n"
"	background-color: rgb(41,42,43);\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: rgb(41,42,43);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    background-color: rgb(255,0,127);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed {\n"
"    background-color: rgb(185,0,92);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	border:4px solid rgb(101,102,103);\n"
"    background-color: rgb(151,152,153);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"	border:4px solid rgb(255,0,127);\n"
"}\n"
"\n"
"QCheckBox::in"
                        "dicator:checked:pressed {\n"
"	border:4px solid rgb(185,0,92);\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.photo_label_1 = QLabel(self.frame)
        self.photo_label_1.setObjectName(u"photo_label_1")
        self.photo_label_1.setGeometry(QRect(130, 60, 49, 25))
        self.photo_label_4 = QLabel(self.frame)
        self.photo_label_4.setObjectName(u"photo_label_4")
        self.photo_label_4.setGeometry(QRect(130, 150, 49, 25))
        self.tarif_supp = QDoubleSpinBox(self.frame)
        self.tarif_supp.setObjectName(u"tarif_supp")
        self.tarif_supp.setGeometry(QRect(180, 240, 61, 25))
        self.tarif_supp.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.tarif_supp.setMaximum(100.000000000000000)
        self.tarif_supp.setSingleStep(0.010000000000000)
        self.tarif_supp.setValue(4.000000000000000)
        self.devise_4 = QLabel(self.frame)
        self.devise_4.setObjectName(u"devise_4")
        self.devise_4.setGeometry(QRect(250, 150, 21, 25))
        self.photo_label_3 = QLabel(self.frame)
        self.photo_label_3.setObjectName(u"photo_label_3")
        self.photo_label_3.setGeometry(QRect(130, 120, 49, 25))
        self.tarif_checkbox_1 = QCheckBox(self.frame)
        self.tarif_checkbox_1.setObjectName(u"tarif_checkbox_1")
        self.tarif_checkbox_1.setGeometry(QRect(12, 60, 16, 25))
        self.tarif_6 = QSpinBox(self.frame)
        self.tarif_6.setObjectName(u"tarif_6")
        self.tarif_6.setGeometry(QRect(180, 210, 61, 25))
        self.tarif_6.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.tarif_6.setMinimum(1)
        self.tarif_6.setMaximum(100)
        self.devise_2 = QLabel(self.frame)
        self.devise_2.setObjectName(u"devise_2")
        self.devise_2.setGeometry(QRect(250, 90, 21, 25))
        self.tarif_checkbox_5 = QCheckBox(self.frame)
        self.tarif_checkbox_5.setObjectName(u"tarif_checkbox_5")
        self.tarif_checkbox_5.setGeometry(QRect(12, 180, 16, 25))
        self.photo_label_7 = QLabel(self.frame)
        self.photo_label_7.setObjectName(u"photo_label_7")
        self.photo_label_7.setGeometry(QRect(10, 240, 161, 25))
        self.tarif_checkbox_2 = QCheckBox(self.frame)
        self.tarif_checkbox_2.setObjectName(u"tarif_checkbox_2")
        self.tarif_checkbox_2.setGeometry(QRect(12, 90, 16, 25))
        self.devise_5 = QLabel(self.frame)
        self.devise_5.setObjectName(u"devise_5")
        self.devise_5.setGeometry(QRect(250, 180, 21, 25))
        self.multiple_tarifs_6 = QSpinBox(self.frame)
        self.multiple_tarifs_6.setObjectName(u"multiple_tarifs_6")
        self.multiple_tarifs_6.setGeometry(QRect(50, 210, 71, 25))
        self.multiple_tarifs_6.setReadOnly(False)
        self.multiple_tarifs_6.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.multiple_tarifs_6.setMinimum(2)
        self.multiple_tarifs_6.setMaximum(5)
        self.multiple_tarifs_4 = QSpinBox(self.frame)
        self.multiple_tarifs_4.setObjectName(u"multiple_tarifs_4")
        self.multiple_tarifs_4.setGeometry(QRect(50, 150, 71, 25))
        self.multiple_tarifs_4.setReadOnly(False)
        self.multiple_tarifs_4.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.multiple_tarifs_4.setMinimum(4)
        self.multiple_tarifs_4.setMaximum(30)
        self.multiple_tarifs_4.setValue(12)
        self.tarif_1 = QSpinBox(self.frame)
        self.tarif_1.setObjectName(u"tarif_1")
        self.tarif_1.setGeometry(QRect(180, 60, 61, 25))
        self.tarif_1.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.tarif_1.setMinimum(1)
        self.tarif_1.setMaximum(100)
        self.tarif_1.setValue(6)
        self.devise_3 = QLabel(self.frame)
        self.devise_3.setObjectName(u"devise_3")
        self.devise_3.setGeometry(QRect(250, 120, 21, 25))
        self.tarif_3 = QSpinBox(self.frame)
        self.tarif_3.setObjectName(u"tarif_3")
        self.tarif_3.setGeometry(QRect(180, 120, 61, 25))
        self.tarif_3.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.tarif_3.setMinimum(1)
        self.tarif_3.setMaximum(100)
        self.tarif_3.setValue(30)
        self.tarif_checkbox_4 = QCheckBox(self.frame)
        self.tarif_checkbox_4.setObjectName(u"tarif_checkbox_4")
        self.tarif_checkbox_4.setGeometry(QRect(12, 150, 16, 25))
        self.photo_label_2 = QLabel(self.frame)
        self.photo_label_2.setObjectName(u"photo_label_2")
        self.photo_label_2.setGeometry(QRect(130, 90, 49, 25))
        self.tarif_checkbox_6 = QCheckBox(self.frame)
        self.tarif_checkbox_6.setObjectName(u"tarif_checkbox_6")
        self.tarif_checkbox_6.setGeometry(QRect(12, 210, 16, 25))
        self.photo_label_6 = QLabel(self.frame)
        self.photo_label_6.setObjectName(u"photo_label_6")
        self.photo_label_6.setGeometry(QRect(130, 210, 49, 25))
        self.tarif_5 = QSpinBox(self.frame)
        self.tarif_5.setObjectName(u"tarif_5")
        self.tarif_5.setGeometry(QRect(180, 180, 61, 25))
        self.tarif_5.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.tarif_5.setMinimum(1)
        self.tarif_5.setMaximum(100)
        self.label_tarifs = QLabel(self.frame)
        self.label_tarifs.setObjectName(u"label_tarifs")
        self.label_tarifs.setGeometry(QRect(10, 40, 41, 16))
        self.multiple_tarifs_2 = QSpinBox(self.frame)
        self.multiple_tarifs_2.setObjectName(u"multiple_tarifs_2")
        self.multiple_tarifs_2.setGeometry(QRect(50, 90, 71, 25))
        self.multiple_tarifs_2.setReadOnly(False)
        self.multiple_tarifs_2.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.multiple_tarifs_2.setMinimum(2)
        self.multiple_tarifs_2.setMaximum(5)
        self.multiple_tarifs_2.setSingleStep(3)
        self.devise_7 = QLabel(self.frame)
        self.devise_7.setObjectName(u"devise_7")
        self.devise_7.setGeometry(QRect(250, 240, 21, 25))
        self.multiple_tarifs_5 = QSpinBox(self.frame)
        self.multiple_tarifs_5.setObjectName(u"multiple_tarifs_5")
        self.multiple_tarifs_5.setGeometry(QRect(50, 180, 71, 25))
        self.multiple_tarifs_5.setReadOnly(False)
        self.multiple_tarifs_5.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.multiple_tarifs_5.setMinimum(1)
        self.multiple_tarifs_5.setMaximum(1)
        self.devise = QLabel(self.frame)
        self.devise.setObjectName(u"devise")
        self.devise.setGeometry(QRect(250, 60, 21, 25))
        self.tarif_4 = QSpinBox(self.frame)
        self.tarif_4.setObjectName(u"tarif_4")
        self.tarif_4.setGeometry(QRect(180, 150, 61, 25))
        self.tarif_4.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.tarif_4.setMinimum(1)
        self.tarif_4.setMaximum(100)
        self.tarif_checkbox_3 = QCheckBox(self.frame)
        self.tarif_checkbox_3.setObjectName(u"tarif_checkbox_3")
        self.tarif_checkbox_3.setGeometry(QRect(12, 120, 16, 25))
        self.tarif_2 = QSpinBox(self.frame)
        self.tarif_2.setObjectName(u"tarif_2")
        self.tarif_2.setGeometry(QRect(180, 90, 61, 25))
        self.tarif_2.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.tarif_2.setMinimum(1)
        self.tarif_2.setMaximum(100)
        self.tarif_2.setValue(15)
        self.multiple_tarifs_1 = QSpinBox(self.frame)
        self.multiple_tarifs_1.setObjectName(u"multiple_tarifs_1")
        self.multiple_tarifs_1.setGeometry(QRect(50, 60, 71, 25))
        self.multiple_tarifs_1.setReadOnly(True)
        self.multiple_tarifs_1.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.multiple_tarifs_1.setMinimum(1)
        self.multiple_tarifs_1.setMaximum(1)
        self.photo_label_5 = QLabel(self.frame)
        self.photo_label_5.setObjectName(u"photo_label_5")
        self.photo_label_5.setGeometry(QRect(130, 180, 49, 25))
        self.multiple_tarifs_3 = QSpinBox(self.frame)
        self.multiple_tarifs_3.setObjectName(u"multiple_tarifs_3")
        self.multiple_tarifs_3.setGeometry(QRect(50, 120, 71, 25))
        self.multiple_tarifs_3.setReadOnly(False)
        self.multiple_tarifs_3.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.multiple_tarifs_3.setMinimum(3)
        self.multiple_tarifs_3.setMaximum(15)
        self.multiple_tarifs_3.setValue(8)
        self.devise_6 = QLabel(self.frame)
        self.devise_6.setObjectName(u"devise_6")
        self.devise_6.setGeometry(QRect(250, 210, 21, 25))
        self.Tarifs_auto_checkbox = QCheckBox(self.frame)
        self.Tarifs_auto_checkbox.setObjectName(u"Tarifs_auto_checkbox")
        self.Tarifs_auto_checkbox.setGeometry(QRect(10, 10, 221, 22))

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
        self.label_fili_clair.setText(QCoreApplication.translate("Dialog", u"Filigrane clair :", None))
        self.label_fili_sombre.setText(QCoreApplication.translate("Dialog", u"Filigrane sombre :", None))
        self.pushButton_create_fili.setText(QCoreApplication.translate("Dialog", u"Cr\u00e9er un filigrane", None))
        self.photo_label_1.setText(QCoreApplication.translate("Dialog", u"Photo :", None))
        self.photo_label_4.setText(QCoreApplication.translate("Dialog", u"Photos :", None))
        self.devise_4.setText(QCoreApplication.translate("Dialog", u"\u20ac", None))
        self.photo_label_3.setText(QCoreApplication.translate("Dialog", u"Photos :", None))
        self.tarif_checkbox_1.setText("")
        self.devise_2.setText(QCoreApplication.translate("Dialog", u"\u20ac", None))
        self.tarif_checkbox_5.setText("")
        self.photo_label_7.setText(QCoreApplication.translate("Dialog", u"Photos supl\u00e9mentaires :", None))
        self.tarif_checkbox_2.setText("")
        self.devise_5.setText(QCoreApplication.translate("Dialog", u"\u20ac", None))
        self.devise_3.setText(QCoreApplication.translate("Dialog", u"\u20ac", None))
        self.tarif_checkbox_4.setText("")
        self.photo_label_2.setText(QCoreApplication.translate("Dialog", u"Photos :", None))
        self.tarif_checkbox_6.setText("")
        self.photo_label_6.setText(QCoreApplication.translate("Dialog", u"Tours :", None))
        self.label_tarifs.setText(QCoreApplication.translate("Dialog", u"Tarifs :", None))
        self.devise_7.setText(QCoreApplication.translate("Dialog", u"\u20ac", None))
        self.devise.setText(QCoreApplication.translate("Dialog", u"\u20ac", None))
        self.tarif_checkbox_3.setText("")
        self.photo_label_5.setText(QCoreApplication.translate("Dialog", u"Tour :", None))
        self.devise_6.setText(QCoreApplication.translate("Dialog", u"\u20ac", None))
        self.Tarifs_auto_checkbox.setText(QCoreApplication.translate("Dialog", u"Calcul automatique des tarifs", None))
    # retranslateUi

