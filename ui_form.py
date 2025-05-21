# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHeaderView, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTextEdit,
    QTreeView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1911, 1055)
        MainWindow.setMinimumSize(QSize(1200, 940))
        MainWindow.setMaximumSize(QSize(1000000, 1000000))
        MainWindow.setStyleSheet(u"background-color:rgb(41,42,43);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(9)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.frame_photo_selectionnees = QFrame(self.centralwidget)
        self.frame_photo_selectionnees.setObjectName(u"frame_photo_selectionnees")
        self.frame_photo_selectionnees.setMinimumSize(QSize(0, 236))
        self.frame_photo_selectionnees.setMaximumSize(QSize(16777215, 236))
        self.frame_photo_selectionnees.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color:rgb(71,72,73);\n"
"	border-radius:5px;\n"
"	color:#FFFFFF;\n"
"}\n"
"\n"
"/* VERTICAL SCORLLBAR */\n"
"QScrollBar:vertical {\n"
"	border:none;\n"
"	background-color: rgb(71,72,73);\n"
"	width: 15px;\n"
"	margin: 12px 3px 12px 3px;\n"
"	border-radius: 0px;\n"
"}\n"
"/*HANDL BAR VERTICAL */\n"
"QScrollBar::handle:vertical{\n"
"	background-color: rgb(101,102,103);\n"
"	min-height: 30px;\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover{\n"
"	background-color: rgb(101,102,140);\n"
"}\n"
"QScrollBar::handle:vertical:pressed{\n"
"	background-color: rgb(185,0,92);\n"
"}\n"
"/*BTN TOP - SCROLLBAR - VERTICAL*/\n"
"QScrollBar:sub-line:vertical {\n"
"	border:none;\n"
"	background-color: rgb(101,102,140);\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar:sub-line:ve"
                        "rtical:hover {\n"
"	background-color: rgb(255,0,127);\n"
"}\n"
"\n"
"QScrollBar:sub-line:vertical:pressed {\n"
"	background-color: rgb(185,0,92);\n"
"}\n"
"/*BTN BOTTOM - SCROLLBAR - VERTICAL */\n"
"QScrollBar:add-line:vertical {\n"
"	border:none;\n"
"	background-color: rgb(101,102,140);\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar:add-line:vertical:hover {\n"
"	background-color: rgb(255,0,127);\n"
"}\n"
"\n"
"QScrollBar:add-line:vertical:pressed {\n"
"	background-color: rgb(185,0,92);\n"
"}\n"
"/* RESET ARROW - VERTICAL */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background:none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{\n"
"	background: none;\n"
"}\n"
"\n"
"\n"
"/*********************************************/\n"
"/* HORIZONTAL SCORLLBA"
                        "R */\n"
"QScrollBar:horizontal {\n"
"	border:none;\n"
"	background-color: rgb(73,74,75);\n"
"	height: 15px;\n"
"	margin: 3px 12px 3px 12px;\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"/*HANDL BAR HORIZONTAL */\n"
"QScrollBar::handle:horizontal{\n"
"	background-color: rgb(101,102,103);\n"
"	min-width: 30px;\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover{\n"
"	background-color: rgb(101,102,140);\n"
"}\n"
"QScrollBar::handle:horizontal:pressed{\n"
"	background-color: rgb(185,0,92);\n"
"}\n"
"\n"
"/*BTN LEFT - SCROLLBAR - HORIZONTAL */\n"
"QScrollBar:sub-line:horizontal {\n"
"	border:none;\n"
"	background-color: rgb(101,102,140);\n"
"	width: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar:sub-line:horizontal:hover {\n"
"	background-color: rgb(255,0,127);\n"
"}\n"
"\n"
"QScrollBar:sub-line:horizontal:p"
                        "ressed {\n"
"	background-color: rgb(185,0,92);\n"
"}\n"
"\n"
"/*BTN RIGHT - SCROLLBAR - HORIZONTAL */\n"
"QScrollBar:add-line:horizontal {\n"
"	border:none;\n"
"	background-color: rgb(101,102,140);\n"
"	width: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar:add-line:horizontal:hover {\n"
"	background-color: rgb(255,0,127);\n"
"}\n"
"\n"
"QScrollBar:add-line:horizontal:pressed {\n"
"	background-color: rgb(185,0,92);\n"
"}\n"
"\n"
"\n"
"/* RESET ARROW - HORIZONTAL */\n"
"QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"	background:none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal{\n"
"	background: none;\n"
"}")
        self.frame_photo_selectionnees.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_photo_selectionnees.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_photo_selectionnees)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label__photo_selectionnees = QLabel(self.frame_photo_selectionnees)
        self.label__photo_selectionnees.setObjectName(u"label__photo_selectionnees")
        self.label__photo_selectionnees.setMinimumSize(QSize(0, 30))
        self.label__photo_selectionnees.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(12)
        self.label__photo_selectionnees.setFont(font)
        self.label__photo_selectionnees.setStyleSheet(u"border-radius:0px;\n"
"border-top-left-radius: 5px;\n"
"border-top-right-radius: 5px;\n"
"\n"
"background-color:rgb(81, 82, 83);\n"
"color:#FFFFFF;")
        self.label__photo_selectionnees.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label__photo_selectionnees, 0, 0, 1, 1)

        self.listWidgetPhotos = QListWidget(self.frame_photo_selectionnees)
        self.listWidgetPhotos.setObjectName(u"listWidgetPhotos")
        self.listWidgetPhotos.setMinimumSize(QSize(0, 200))
        self.listWidgetPhotos.setMaximumSize(QSize(16777215, 200))
        self.listWidgetPhotos.setStyleSheet(u"color: #FFFFFF;")

        self.gridLayout_3.addWidget(self.listWidgetPhotos, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_photo_selectionnees, 2, 1, 1, 2)

        self.frame_formulaire = QFrame(self.centralwidget)
        self.frame_formulaire.setObjectName(u"frame_formulaire")
        self.frame_formulaire.setMinimumSize(QSize(400, 0))
        self.frame_formulaire.setMaximumSize(QSize(400, 16777215))
        self.frame_formulaire.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color:rgb(71,72,73);\n"
"	border-radius:5px;\n"
"	color:#FFFFFF;\n"
"}")
        self.frame_formulaire.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_formulaire.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame_formulaire)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 401, 30))
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setMaximumSize(QSize(16777215, 30))
        self.label.setFont(font)
        self.label.setStyleSheet(u"border-radius:0px;\n"
"border-top-left-radius: 5px;\n"
"border-top-right-radius: 5px;\n"
"\n"
"background-color:rgb(81, 82, 83);\n"
"color:#FFFFFF;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button_nouveau_formulaire = QPushButton(self.frame_formulaire)
        self.button_nouveau_formulaire.setObjectName(u"button_nouveau_formulaire")
        self.button_nouveau_formulaire.setGeometry(QRect(20, 40, 170, 50))
        self.button_nouveau_formulaire.setMinimumSize(QSize(170, 50))
        self.button_nouveau_formulaire.setMaximumSize(QSize(170, 50))
        font1 = QFont()
        font1.setPointSize(10)
        self.button_nouveau_formulaire.setFont(font1)
        self.button_nouveau_formulaire.setStyleSheet(u"/* QPush BUTTON */\n"
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
        self.button_charger_formulaire = QPushButton(self.frame_formulaire)
        self.button_charger_formulaire.setObjectName(u"button_charger_formulaire")
        self.button_charger_formulaire.setGeometry(QRect(210, 40, 170, 50))
        self.button_charger_formulaire.setMinimumSize(QSize(170, 50))
        self.button_charger_formulaire.setMaximumSize(QSize(170, 50))
        self.button_charger_formulaire.setFont(font1)
        self.button_charger_formulaire.setStyleSheet(u"/* QPush BUTTON */\n"
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
        self.label_nom = QLabel(self.frame_formulaire)
        self.label_nom.setObjectName(u"label_nom")
        self.label_nom.setGeometry(QRect(20, 110, 161, 16))
        self.label_prenom = QLabel(self.frame_formulaire)
        self.label_prenom.setObjectName(u"label_prenom")
        self.label_prenom.setGeometry(QRect(220, 110, 161, 16))
        self.label_email = QLabel(self.frame_formulaire)
        self.label_email.setObjectName(u"label_email")
        self.label_email.setGeometry(QRect(20, 180, 361, 16))
        self.label_telephone = QLabel(self.frame_formulaire)
        self.label_telephone.setObjectName(u"label_telephone")
        self.label_telephone.setGeometry(QRect(20, 250, 361, 16))
        self.label_paiement = QLabel(self.frame_formulaire)
        self.label_paiement.setObjectName(u"label_paiement")
        self.label_paiement.setGeometry(QRect(20, 390, 361, 16))
        self.comboBox_paiement = QComboBox(self.frame_formulaire)
        self.comboBox_paiement.addItem("")
        self.comboBox_paiement.addItem("")
        self.comboBox_paiement.addItem("")
        self.comboBox_paiement.addItem("")
        self.comboBox_paiement.addItem("")
        self.comboBox_paiement.addItem("")
        self.comboBox_paiement.addItem("")
        self.comboBox_paiement.setObjectName(u"comboBox_paiement")
        self.comboBox_paiement.setGeometry(QRect(20, 410, 231, 31))
        self.comboBox_paiement.setStyleSheet(u"/* COMBO BOX */\n"
"QComboBox {\n"
"	border: none;\n"
"    padding: 1px 20px 1px 3px;\n"
"    background-color: rgb(101,102,103);\n"
"	border-radius: 5px;\n"
"	color:#FFFFFF;\n"
"}\n"
"\n"
"QComboBox:hover { \n"
"	background-color: rgb(101,102,150);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox:selected{\n"
"	background-color: rgb(101,102,150);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView{\n"
"    border: 2px solid rgb(73,74,75);\n"
"    selection-background-color: rgb(101,102,103);\n"
"}")
        self.textEdit_remarque = QTextEdit(self.frame_formulaire)
        self.textEdit_remarque.setObjectName(u"textEdit_remarque")
        self.textEdit_remarque.setGeometry(QRect(20, 480, 361, 71))
        self.textEdit_remarque.setStyleSheet(u"background-color: rgb(101,102,103);color:#FFFFFF;")
        self.label_remarque = QLabel(self.frame_formulaire)
        self.label_remarque.setObjectName(u"label_remarque")
        self.label_remarque.setGeometry(QRect(20, 460, 361, 16))
        self.button_sauvegarder_formulaire = QPushButton(self.frame_formulaire)
        self.button_sauvegarder_formulaire.setObjectName(u"button_sauvegarder_formulaire")
        self.button_sauvegarder_formulaire.setGeometry(QRect(40, 570, 160, 50))
        self.button_sauvegarder_formulaire.setMinimumSize(QSize(160, 50))
        self.button_sauvegarder_formulaire.setMaximumSize(QSize(160, 50))
        self.button_sauvegarder_formulaire.setFont(font)
        self.button_sauvegarder_formulaire.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(100,150,102);\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 7px;\n"
"    text-align: center;}\n"
"QPushButton:hover {\n"
"	background-color: rgb(100,101,150);}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(185,0,92);}\n"
"QPushButton:selected{\n"
"	background-color: rgb(100,101,150);}")
        self.lineEdit_nom = QLineEdit(self.frame_formulaire)
        self.lineEdit_nom.setObjectName(u"lineEdit_nom")
        self.lineEdit_nom.setGeometry(QRect(20, 130, 161, 31))
        self.lineEdit_nom.setStyleSheet(u"border:none;\n"
"border-radius : 5px;\n"
"background-color:rgb(101,102,103);color:#FFFFFF;")
        self.lineEdit_prenom = QLineEdit(self.frame_formulaire)
        self.lineEdit_prenom.setObjectName(u"lineEdit_prenom")
        self.lineEdit_prenom.setGeometry(QRect(220, 130, 161, 31))
        self.lineEdit_prenom.setStyleSheet(u"border:none;\n"
"border-radius : 5px;\n"
"background-color:rgb(101,102,103);color:#FFFFFF;")
        self.lineEdit_email = QLineEdit(self.frame_formulaire)
        self.lineEdit_email.setObjectName(u"lineEdit_email")
        self.lineEdit_email.setGeometry(QRect(20, 200, 361, 31))
        self.lineEdit_email.setStyleSheet(u"border:none;\n"
"border-radius : 5px;\n"
"background-color:rgb(101,102,103);color:#FFFFFF;")
        self.lineEdit_telephone = QLineEdit(self.frame_formulaire)
        self.lineEdit_telephone.setObjectName(u"lineEdit_telephone")
        self.lineEdit_telephone.setGeometry(QRect(20, 270, 361, 31))
        self.lineEdit_telephone.setStyleSheet(u"border:none;\n"
"border-radius : 5px;\n"
"background-color:rgb(101,102,103);color:#FFFFFF;")
        self.label_id = QLabel(self.frame_formulaire)
        self.label_id.setObjectName(u"label_id")
        self.label_id.setGeometry(QRect(20, 40, 361, 16))
        self.lineEdit_id = QLineEdit(self.frame_formulaire)
        self.lineEdit_id.setObjectName(u"lineEdit_id")
        self.lineEdit_id.setGeometry(QRect(20, 60, 361, 31))
        self.lineEdit_id.setStyleSheet(u"border:none;\n"
"border-radius : 5px;\n"
"background-color:rgb(101,102,103);\n"
"color:#FFFFFF;")
        self.lineEdit_id.setReadOnly(True)
        self.button_quitter_formulaire = QPushButton(self.frame_formulaire)
        self.button_quitter_formulaire.setObjectName(u"button_quitter_formulaire")
        self.button_quitter_formulaire.setGeometry(QRect(210, 570, 151, 50))
        self.button_quitter_formulaire.setMinimumSize(QSize(100, 50))
        self.button_quitter_formulaire.setMaximumSize(QSize(160, 50))
        self.button_quitter_formulaire.setFont(font)
        self.button_quitter_formulaire.setAutoFillBackground(False)
        self.button_quitter_formulaire.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(200,101,102);\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 7px;\n"
"    text-align: center;}\n"
"QPushButton:hover {\n"
"	background-color: rgb(100,101,150);}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(185,0,92);}\n"
"QPushButton:selected{\n"
"	background-color: rgb(100,101,150);}")
        self.button_quitter_formulaire.setLocale(QLocale(QLocale.French, QLocale.France))
        self.label_photos = QLabel(self.frame_formulaire)
        self.label_photos.setObjectName(u"label_photos")
        self.label_photos.setGeometry(QRect(20, 320, 361, 16))
        self.lineEdit_photos = QLineEdit(self.frame_formulaire)
        self.lineEdit_photos.setObjectName(u"lineEdit_photos")
        self.lineEdit_photos.setGeometry(QRect(20, 340, 361, 31))
        self.lineEdit_photos.setStyleSheet(u"border:none;\n"
"border-radius : 5px;\n"
"background-color:rgb(101,102,103);color:#FFFFFF;")
        self.lineEdit_photos.setReadOnly(True)
        self.lineEdit_prix = QLineEdit(self.frame_formulaire)
        self.lineEdit_prix.setObjectName(u"lineEdit_prix")
        self.lineEdit_prix.setGeometry(QRect(270, 410, 111, 31))
        self.lineEdit_prix.setStyleSheet(u"border:none;\n"
"border-radius : 5px;\n"
"background-color:rgb(101,102,103);color:#FFFFFF;")
        self.lineEdit_prix.setReadOnly(False)
        self.label_prix = QLabel(self.frame_formulaire)
        self.label_prix.setObjectName(u"label_prix")
        self.label_prix.setGeometry(QRect(270, 390, 71, 20))

        self.gridLayout.addWidget(self.frame_formulaire, 0, 3, 2, 1)

        self.label_logo = QLabel(self.centralwidget)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setMinimumSize(QSize(400, 236))
        self.label_logo.setMaximumSize(QSize(400, 236))
        self.label_logo.setStyleSheet(u"")

        self.gridLayout.addWidget(self.label_logo, 2, 3, 1, 1)

        self.frame_affichage = QFrame(self.centralwidget)
        self.frame_affichage.setObjectName(u"frame_affichage")
        self.frame_affichage.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color:rgb(71,72,73);\n"
"	border-radius:5px;\n"
"	color:#FFFFFF;\n"
"}")
        self.frame_affichage.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_affichage.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_affichage)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.labelImage = QLabel(self.frame_affichage)
        self.labelImage.setObjectName(u"labelImage")
        self.labelImage.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.labelImage, 1, 0, 1, 5)

        self.labelNomImage = QLabel(self.frame_affichage)
        self.labelNomImage.setObjectName(u"labelNomImage")
        self.labelNomImage.setMinimumSize(QSize(0, 30))
        self.labelNomImage.setMaximumSize(QSize(16777215, 30))
        self.labelNomImage.setFont(font)
        self.labelNomImage.setStyleSheet(u"color:#FFFFFF;")
        self.labelNomImage.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.labelNomImage, 0, 0, 1, 5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 3, 3, 1, 1)

        self.button_precedent = QPushButton(self.frame_affichage)
        self.button_precedent.setObjectName(u"button_precedent")
        self.button_precedent.setMinimumSize(QSize(80, 50))
        self.button_precedent.setMaximumSize(QSize(80, 50))
        self.button_precedent.setFont(font)
        self.button_precedent.setStyleSheet(u"/* QPush BUTTON */\n"
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

        self.gridLayout_4.addWidget(self.button_precedent, 3, 0, 1, 1)

        self.button_suivant = QPushButton(self.frame_affichage)
        self.button_suivant.setObjectName(u"button_suivant")
        self.button_suivant.setMinimumSize(QSize(80, 50))
        self.button_suivant.setMaximumSize(QSize(80, 50))
        self.button_suivant.setFont(font)
        self.button_suivant.setStyleSheet(u"/* QPush BUTTON */\n"
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

        self.gridLayout_4.addWidget(self.button_suivant, 3, 4, 1, 1)

        self.button_selectionner = QPushButton(self.frame_affichage)
        self.button_selectionner.setObjectName(u"button_selectionner")
        self.button_selectionner.setMinimumSize(QSize(150, 50))
        self.button_selectionner.setMaximumSize(QSize(150, 50))
        self.button_selectionner.setFont(font)
        self.button_selectionner.setStyleSheet(u"/* QPush BUTTON */\n"
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

        self.gridLayout_4.addWidget(self.button_selectionner, 3, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 3, 1, 1, 1)


        self.gridLayout.addWidget(self.frame_affichage, 0, 1, 2, 2)

        self.frame_dossier = QFrame(self.centralwidget)
        self.frame_dossier.setObjectName(u"frame_dossier")
        self.frame_dossier.setMinimumSize(QSize(300, 0))
        self.frame_dossier.setMaximumSize(QSize(300, 16777215))
        self.frame_dossier.setStyleSheet(u"	background-color:rgb(71,72,73);\n"
"	border-radius:5px;\n"
"	color:#FFFFFF;\n"
"\n"
"")
        self.frame_dossier.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_dossier.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_dossier)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.treeView = QTreeView(self.frame_dossier)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setStyleSheet(u"QTreeView{background-color:rgb(71,72,73);}\n"
"\n"
"/* VERTICAL SCORLLBAR */\n"
"QScrollBar:vertical {\n"
"	border:none;\n"
"	background-color: rgb(71,72,73);\n"
"	width: 15px;\n"
"	margin: 12px 3px 12px 3px;\n"
"	border-radius: 0px;\n"
"}\n"
"/*HANDL BAR VERTICAL */\n"
"QScrollBar::handle:vertical{\n"
"	background-color: rgb(101,102,103);\n"
"	min-height: 30px;\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover{\n"
"	background-color: rgb(101,102,140);\n"
"}\n"
"QScrollBar::handle:vertical:pressed{\n"
"	background-color: rgb(185,0,92);\n"
"}\n"
"/*BTN TOP - SCROLLBAR - VERTICAL*/\n"
"QScrollBar:sub-line:vertical {\n"
"	border:none;\n"
"	background-color: rgb(101,102,140);\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar:sub-line:vertical:hover {\n"
"	background-color: rgb(255,0,127);\n"
""
                        "}\n"
"\n"
"QScrollBar:sub-line:vertical:pressed {\n"
"	background-color: rgb(185,0,92);\n"
"}\n"
"/*BTN BOTTOM - SCROLLBAR - VERTICAL */\n"
"QScrollBar:add-line:vertical {\n"
"	border:none;\n"
"	background-color: rgb(101,102,140);\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar:add-line:vertical:hover {\n"
"	background-color: rgb(255,0,127);\n"
"}\n"
"\n"
"QScrollBar:add-line:vertical:pressed {\n"
"	background-color: rgb(185,0,92);\n"
"}\n"
"/* RESET ARROW - VERTICAL */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background:none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{\n"
"	background: none;\n"
"}\n"
"\n"
"\n"
"/*********************************************/\n"
"/* HORIZONTAL SCORLLBAR */\n"
"QScrollBar:horizontal {\n"
"	border:none;\n"
"	ba"
                        "ckground-color: rgb(73,74,75);\n"
"	height: 15px;\n"
"	margin: 3px 12px 3px 12px;\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"/*HANDL BAR HORIZONTAL */\n"
"QScrollBar::handle:horizontal{\n"
"	background-color: rgb(101,102,103);\n"
"	min-width: 30px;\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover{\n"
"	background-color: rgb(101,102,140);\n"
"}\n"
"QScrollBar::handle:horizontal:pressed{\n"
"	background-color: rgb(185,0,92);\n"
"}\n"
"\n"
"/*BTN LEFT - SCROLLBAR - HORIZONTAL */\n"
"QScrollBar:sub-line:horizontal {\n"
"	border:none;\n"
"	background-color: rgb(101,102,140);\n"
"	width: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar:sub-line:horizontal:hover {\n"
"	background-color: rgb(255,0,127);\n"
"}\n"
"\n"
"QScrollBar:sub-line:horizontal:pressed {\n"
"	background-color: rgb(185,0,92);\n"
"}\n"
"\n"
""
                        "/*BTN RIGHT - SCROLLBAR - HORIZONTAL */\n"
"QScrollBar:add-line:horizontal {\n"
"	border:none;\n"
"	background-color: rgb(101,102,140);\n"
"	width: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar:add-line:horizontal:hover {\n"
"	background-color: rgb(255,0,127);\n"
"}\n"
"\n"
"QScrollBar:add-line:horizontal:pressed {\n"
"	background-color: rgb(185,0,92);\n"
"}\n"
"\n"
"\n"
"/* RESET ARROW - HORIZONTAL */\n"
"QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"	background:none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal{\n"
"	background: none;\n"
"}")

        self.gridLayout_2.addWidget(self.treeView, 0, 0, 1, 1)

        self.pushButton_refresh = QPushButton(self.frame_dossier)
        self.pushButton_refresh.setObjectName(u"pushButton_refresh")
        self.pushButton_refresh.setMinimumSize(QSize(0, 30))
        self.pushButton_refresh.setStyleSheet(u"/* QPush BUTTON */\n"
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

        self.gridLayout_2.addWidget(self.pushButton_refresh, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_dossier, 0, 0, 3, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1911, 21))
        self.menubar.setStyleSheet(u"QMenuBar {\n"
"  spacing : 10px;\n"
"background-color:rgb(71,72,73);\n"
"color:white;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"  /* when selected using mouse or keyboard */\n"
"  background-color: rgb(101,102,140);\n"
" border-radius:5px;\n"
"}\n"
"\n"
"QMenuBar::item:pressed {\n"
"  /* when selected using mouse or keyboard */\n"
"  background-color: rgb(185,0,92);\n"
" border-radius:5px;\n"
"}")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setStyleSheet(u"QStatusBar{background-color: rgb(71,72,73);}")
        self.statusbar.setSizeGripEnabled(True)
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.button_nouveau_formulaire, self.button_charger_formulaire)
        QWidget.setTabOrder(self.button_charger_formulaire, self.lineEdit_nom)
        QWidget.setTabOrder(self.lineEdit_nom, self.lineEdit_prenom)
        QWidget.setTabOrder(self.lineEdit_prenom, self.lineEdit_email)
        QWidget.setTabOrder(self.lineEdit_email, self.lineEdit_telephone)
        QWidget.setTabOrder(self.lineEdit_telephone, self.lineEdit_photos)
        QWidget.setTabOrder(self.lineEdit_photos, self.comboBox_paiement)
        QWidget.setTabOrder(self.comboBox_paiement, self.textEdit_remarque)
        QWidget.setTabOrder(self.textEdit_remarque, self.button_sauvegarder_formulaire)
        QWidget.setTabOrder(self.button_sauvegarder_formulaire, self.button_quitter_formulaire)
        QWidget.setTabOrder(self.button_quitter_formulaire, self.button_precedent)
        QWidget.setTabOrder(self.button_precedent, self.button_suivant)
        QWidget.setTabOrder(self.button_suivant, self.button_selectionner)
        QWidget.setTabOrder(self.button_selectionner, self.treeView)
        QWidget.setTabOrder(self.treeView, self.listWidgetPhotos)
        QWidget.setTabOrder(self.listWidgetPhotos, self.lineEdit_id)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label__photo_selectionnees.setText(QCoreApplication.translate("MainWindow", u"Photo(s) s\u00e9lectionn\u00e9e(s)", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Formulaire de commande", None))
        self.button_nouveau_formulaire.setText(QCoreApplication.translate("MainWindow", u"Nouvelle commande", None))
        self.button_charger_formulaire.setText(QCoreApplication.translate("MainWindow", u"Modifier une commande", None))
        self.label_nom.setText(QCoreApplication.translate("MainWindow", u"Nom :", None))
        self.label_prenom.setText(QCoreApplication.translate("MainWindow", u"Pr\u00e9nom :", None))
        self.label_email.setText(QCoreApplication.translate("MainWindow", u"Email :", None))
        self.label_telephone.setText(QCoreApplication.translate("MainWindow", u"Num\u00e9ro de t\u00e9l\u00e9phone :", None))
        self.label_paiement.setText(QCoreApplication.translate("MainWindow", u"Mode de paiement :", None))
        self.comboBox_paiement.setItemText(0, QCoreApplication.translate("MainWindow", u"Choisir", None))
        self.comboBox_paiement.setItemText(1, QCoreApplication.translate("MainWindow", u"Wero", None))
        self.comboBox_paiement.setItemText(2, QCoreApplication.translate("MainWindow", u"Lydia", None))
        self.comboBox_paiement.setItemText(3, QCoreApplication.translate("MainWindow", u"Paypal", None))
        self.comboBox_paiement.setItemText(4, QCoreApplication.translate("MainWindow", u"Virement bancaire", None))
        self.comboBox_paiement.setItemText(5, QCoreApplication.translate("MainWindow", u"Esp\u00e8ce", None))
        self.comboBox_paiement.setItemText(6, QCoreApplication.translate("MainWindow", u"Ch\u00e8que", None))

        self.label_remarque.setText(QCoreApplication.translate("MainWindow", u"Remarque ou demande particuli\u00e8re :", None))
        self.button_sauvegarder_formulaire.setText(QCoreApplication.translate("MainWindow", u"Sauvergarder", None))
        self.label_id.setText(QCoreApplication.translate("MainWindow", u"ID de commande :", None))
        self.button_quitter_formulaire.setText(QCoreApplication.translate("MainWindow", u"Abandonner", None))
        self.label_photos.setText(QCoreApplication.translate("MainWindow", u"Photos choisis : ", None))
        self.label_prix.setText(QCoreApplication.translate("MainWindow", u"Tarif :", None))
        self.label_logo.setText("")
        self.labelImage.setText(QCoreApplication.translate("MainWindow", u"Selectionner une photo", None))
        self.labelNomImage.setText(QCoreApplication.translate("MainWindow", u"Nom de la photo", None))
        self.button_precedent.setText(QCoreApplication.translate("MainWindow", u"Pr\u00e9c\u00e9dent", None))
        self.button_suivant.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
        self.button_selectionner.setText(QCoreApplication.translate("MainWindow", u"Selectionner", None))
        self.pushButton_refresh.setText(QCoreApplication.translate("MainWindow", u"Rafraichir", None))
    # retranslateUi

