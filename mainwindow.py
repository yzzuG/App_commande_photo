# This Python file uses the following encoding: utf-8

# .\.qtcreator\Python_3_13_2venv\Scripts\activate
# pyside6-uic form.ui -o ui_form.p
# pyside6-uic dialog.ui -o ui_dialog.p
# pyside6-uic fili.ui -o ui_fili.p
# pyinstaller --noconfirm --windowed --icon=icone.ico --add-data=M.A.PHOTO.png:ressources -n MA_Photo_commande_V2_0 mainwindow.py



import sys
import os
import time
import shutil
import pandas as pd
import smtplib
from PIL import Image, ExifTags
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFileSystemModel, QListWidgetItem, QFileDialog,
    QDialog, QVBoxLayout, QLineEdit, QLabel, QPushButton, QMessageBox,QInputDialog
)
from PySide6.QtGui import QPixmap, QImage, QPainter, QPainterPath, QIcon, QFont, QColor
from PySide6.QtCore import Qt, QSize, QRect

from ui_form import Ui_MainWindow
from ui_dialog import Ui_Dialog
from ui_fili import Ui_Fili

# EXIF pour orientation
EXIF_ORIENTATION_TAG = next((k for k, v in ExifTags.TAGS.items() if v == "Orientation"), None)

selected_images = []
data_save_folder = "C:"
admin_password = ""
photos_folder ="C:"
fili_clair_path = ""
fili_sombre_path = ""
restrict_mode = 0

calcul_tarif_auto = 0
tarif_multiple_1 = 0
tarif_multiple_2 = 0
tarif_multiple_3 = 0
tarif_multiple_4 = 0
tarif_multiple_tour_5 = 0
tarif_multiple_tour_6 = 0

tarif_1 = 0
tarif_2 = 0
tarif_3 = 0
tarif_4 = 0
tarif_5 = 0
tarif_6 = 0

tarif_supp = 0


def corriger_orientation(image_pil):
    try:
        exif = image_pil._getexif()
        if exif is not None:
            for tag, value in exif.items():
                key = ExifTags.TAGS.get(tag, tag)
                if key == 'Orientation':
                    if value == 3:
                        image_pil = image_pil.rotate(180, expand=True)
                    elif value == 6:
                        image_pil = image_pil.rotate(270, expand=True)
                    elif value == 8:
                        image_pil = image_pil.rotate(90, expand=True)
    except Exception as e:
        print(f"Erreur EXIF : {e}")
    return image_pil

def pil_to_qimage(pil_image):
    pil_image = pil_image.convert("RGBA")
    data = pil_image.tobytes("raw", "RGBA")
    qimage = QImage(data, pil_image.width, pil_image.height, QImage.Format_RGBA8888)
    return qimage


def add_watermark(image):
    #image = corriger_orientation(image).convert('RGBA')

    watermark_width = int(image.width * 0.3)


    global fili_clair_path
    watermark_path = fili_clair_path

    try:
        watermark = Image.open(watermark_path).convert("RGBA")
        watermark_height = int(watermark_width * (watermark.height / watermark.width))
        watermark = watermark.resize((watermark_width, watermark_height), Image.LANCZOS)
    except Exception as e:
        print(f"Erreur ouverture watermark : {e}")
        return

    position = ((image.width - watermark_width) // 2, image.height - watermark_height - 20)

    watermarked = image.copy()
    watermarked.paste(watermark, position, watermark)
    watermarked = watermarked.convert("RGB")

    return watermarked


class FormulaireHandler:
    def __init__(self, ui):
        self.ui = ui


        self.ui.button_nouveau_formulaire.clicked.connect(self.nouveau_formulaire)
        self.ui.button_charger_formulaire.clicked.connect(self.charger_formulaire)
        self.ui.button_sauvegarder_formulaire.clicked.connect(self.sauvegarder_formulaire)
        self.ui.button_quitter_formulaire.clicked.connect(self.quitter_formulaire)

        self.ui.label_id.setHidden(True);
        self.ui.label_nom.setHidden(True);
        self.ui.label_prenom.setHidden(True);
        self.ui.label_email.setHidden(True);
        self.ui.label_telephone.setHidden(True);
        self.ui.label_photos.setHidden(True);
        self.ui.label_paiement.setHidden(True);
        self.ui.label_prix.setHidden(True);
        self.ui.label_remarque.setHidden(True);
        self.ui.label_type.setHidden(True);
        self.ui.comboBox_type.setHidden(True);
        self.ui.lineEdit_id.setHidden(True);
        self.ui.lineEdit_nom.setHidden(True);
        self.ui.lineEdit_prenom.setHidden(True);
        self.ui.lineEdit_email.setHidden(True);
        self.ui.lineEdit_telephone.setHidden(True);
        self.ui.lineEdit_photos.setHidden(True);
        self.ui.lineEdit_prix.setHidden(True);
        self.ui.comboBox_paiement.setHidden(True);
        self.ui.textEdit_remarque.setHidden(True);
        self.ui.button_sauvegarder_formulaire.setHidden(True);
        self.ui.button_quitter_formulaire.setHidden(True);
        self.ui.button_selectionner.setHidden(True)
        self.ui.button_nouveau_formulaire.setHidden(False)
        self.ui.button_charger_formulaire.setHidden(False)



    def nouveau_formulaire(self):
        self.ui.label_id.setHidden(False);
        self.ui.label_nom.setHidden(False);
        self.ui.label_prenom.setHidden(False);
        self.ui.label_email.setHidden(False);
        self.ui.label_telephone.setHidden(False);
        self.ui.label_photos.setHidden(False);
        self.ui.label_paiement.setHidden(False);
        self.ui.label_prix.setHidden(False);
        self.ui.label_remarque.setHidden(False);
        self.ui.label_type.setHidden(False);
        self.ui.comboBox_type.setHidden(False);
        self.ui.lineEdit_id.setHidden(False);
        self.ui.lineEdit_nom.setHidden(False);
        self.ui.lineEdit_prenom.setHidden(False);
        self.ui.lineEdit_email.setHidden(False);
        self.ui.lineEdit_telephone.setHidden(False);
        self.ui.comboBox_paiement.setHidden(False);
        self.ui.lineEdit_photos.setHidden(False);
        self.ui.textEdit_remarque.setHidden(False);
        self.ui.lineEdit_prix.setHidden(False);
        self.ui.button_sauvegarder_formulaire.setHidden(False);
        self.ui.button_quitter_formulaire.setHidden(False);
        self.ui.button_selectionner.setHidden(False)
        self.ui.button_nouveau_formulaire.setHidden(True)
        self.ui.button_charger_formulaire.setHidden(True)

        self.ui.lineEdit_id.clear()
        self.ui.lineEdit_nom.clear()
        self.ui.lineEdit_prenom.clear()
        self.ui.lineEdit_email.clear()
        self.ui.lineEdit_telephone.clear()
        self.ui.lineEdit_photos.clear()
        self.ui.comboBox_paiement.setCurrentIndex(0)
        self.ui.textEdit_remarque.clear()

        now = datetime.now()
        id_commande = now.strftime("%d%m%y_%H%M%S")
        self.ui.lineEdit_id.setText(id_commande)

    def charger_formulaire(self):
        global data_save_folder
        fichier = f"{data_save_folder}\\formulaire.xlsx"

        if not os.path.exists(fichier):
            QMessageBox.warning(None, "Erreur", f"Fichier non trouvé : {fichier}")
            return

        # Demande ID
        id_commande, ok1 = QInputDialog.getText(None, "Chargement", "Entrez l'ID de la commande :",flags=Qt.WindowStaysOnTopHint)
        if not ok1 or not id_commande:
            return

        # Demande Nom
        nom_client, ok2 = QInputDialog.getText(None, "Chargement", "Entrez le nom du client :",flags=Qt.WindowStaysOnTopHint)
        if not ok2 or not nom_client:
            return

        try:
            self.ui.label_id.setHidden(False);
            self.ui.label_nom.setHidden(False);
            self.ui.label_prenom.setHidden(False);
            self.ui.label_email.setHidden(False);
            self.ui.label_telephone.setHidden(False);
            self.ui.label_photos.setHidden(False);
            self.ui.label_paiement.setHidden(False);
            self.ui.label_prix.setHidden(False);
            self.ui.label_remarque.setHidden(False);
            self.ui.label_type.setHidden(False);
            self.ui.comboBox_type.setHidden(False);
            self.ui.lineEdit_id.setHidden(False);
            self.ui.lineEdit_nom.setHidden(False);
            self.ui.lineEdit_prenom.setHidden(False);
            self.ui.lineEdit_email.setHidden(False);
            self.ui.lineEdit_telephone.setHidden(False);
            self.ui.lineEdit_photos.setHidden(False);
            self.ui.comboBox_paiement.setHidden(False);
            self.ui.textEdit_remarque.setHidden(False);
            self.ui.lineEdit_prix.setHidden(False);
            self.ui.button_sauvegarder_formulaire.setHidden(False);
            self.ui.button_quitter_formulaire.setHidden(False);
            self.ui.button_selectionner.setHidden(False)
            self.ui.button_nouveau_formulaire.setHidden(True)
            self.ui.button_charger_formulaire.setHidden(True)


            df = pd.read_excel(fichier)

            # Vérification colonnes
            if not {"ID", "Nom"}.issubset(df.columns):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.warning)
                msg.setWindowTitle("Erreur")
                msg.setText("Le fichier ne contient pas les colonnes 'ID' et 'Nom'")
                msg.setWindowFlags(Qt.WindowStaysOnTopHint)
                msg.exec()
                return

            # Filtrage
            resultats = df[(df["ID"].astype(str) == id_commande.strip()) & (df["Nom"].str.lower() == nom_client.strip().lower())]

            if resultats.empty:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Aucun résultat")
                msg.setText("Aucune commande trouvée avec ces informations.")
                msg.setWindowFlags(Qt.WindowStaysOnTopHint)
                msg.exec()
                return

            row = resultats.iloc[0]


            dossier_base = f"{data_save_folder}\\Commandes"
            id_nom = f"{id_commande}_{nom_client}"
            chemin_dossier_commande = os.path.join(dossier_base, id_nom)
            chemin_dossier_temp = os.path.join(dossier_base, "temp")
            extensions_image = ['.jpg', '.jpeg', '.png']

            # Sauvegarde des photos dans un dossier temporaire
            if not os.path.exists(chemin_dossier_temp):
                os.makedirs(chemin_dossier_temp)

            # Copier les images sélectionnées
            try:
                for fichier in os.listdir(chemin_dossier_commande):
                    selected_item = os.path.join(chemin_dossier_commande, fichier)
                    nom_fichier = os.path.basename(selected_item)
                    destination = os.path.join(chemin_dossier_temp, nom_fichier)
                    shutil.copy2(selected_item, destination)
            except Exception as e:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Erreur copie images")
                msg.setText(f"Une erreur est survenue lors de la copie des images : {e}")
                msg.setWindowFlags(Qt.WindowStaysOnTopHint)
                msg.exec()



            for fichier in os.listdir(chemin_dossier_temp):
                chemin_fichier = os.path.join(chemin_dossier_temp, fichier)

                # Vérifie si c'est un fichier et si son extension est une image
                if os.path.isfile(chemin_fichier) and any(fichier.lower().endswith(ext) for ext in extensions_image):
                    # Crée un nouvel item pour chaque image
                    item = QListWidgetItem(fichier)
                    pixmap = QPixmap(chemin_fichier).scaled(50, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                    icon = QPixmap(pixmap)

                    selected_images.append(chemin_fichier)

                    item.setText(os.path.basename(chemin_fichier))
                    item.setIcon(icon)
                    item.setData(1000, chemin_fichier)
                    self.ui.listWidgetPhotos.addItem(item)


            self.ui.lineEdit_id.setText(str(row["ID"]))
            self.ui.lineEdit_nom.setText(str(row["Nom"]))
            self.ui.lineEdit_prenom.setText(str(row.get("Prénom", "")))
            self.ui.lineEdit_email.setText(str(row.get("Email", "")))
            telephone = row.get("Téléphone", "")
            if isinstance(telephone, str) and telephone.startswith("'+33"):
                telephone = telephone[4:]  # enlève le préfixe '+33'
            self.ui.lineEdit_telephone.setText(telephone)
            self.ui.lineEdit_photos.setText(str(row.get("Photos", "")))
            self.ui.comboBox_paiement.setCurrentText(str(row.get("Paiement", "")))
            self.ui.lineEdit_prix.setText(str(row.get("Tarif", "")))
            self.ui.textEdit_remarque.setPlainText(str(row.get("Remarque", "")))

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Succès")
            msg.setText("Commande chargée avec succès.")
            msg.setWindowFlags(Qt.WindowStaysOnTopHint)
            msg.exec()

        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Erreur")
            msg.setText(f"Erreur lors du chargement : {e}")
            msg.setWindowFlags(Qt.WindowStaysOnTopHint)
            msg.exec()

    def envoyer_mail(self, commande):
        # Configuration du compte expéditeur
        expediteur = "mailautomatique.m.a.photo@gmail.com"
        mot_de_passe = "dtfk psvo rkao kixh"
        destinataire = commande["Email"]

        sujet = f"Confirmation de commande - ID {commande['ID']}"
        contenu = f"""
    Bonjour {commande['Prénom']} {commande['Nom']},

    Voici les détails de votre commande :

    ID : {commande['ID']}
    Nom : {commande['Nom']}
    Prénom : {commande['Prénom']}
    Email : {commande['Email']}
    Téléphone : {commande['Téléphone']}
    Photos selectionnées : {commande['Photos']}
    Mode de paiement : {commande['Paiement']}
    Remarque : {commande['Remarque']}

    Les photos seront envoyées prochainements par email.

    Merci pour votre confiance.

    Photographiquement vôtre,
    """

        msg = MIMEMultipart()
        msg['From'] = expediteur
        msg['To'] = destinataire
        msg['Subject'] = sujet
        msg.attach(MIMEText(contenu, 'plain'))

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as serveur:
                serveur.login(expediteur, mot_de_passe)
                serveur.send_message(msg)

            msgQ = QMessageBox()
            msgQ.setIcon(QMessageBox.Information)
            msgQ.setWindowTitle("Email")
            msgQ.setText(f"Email envoyé à {destinataire}")
            msgQ.setWindowFlags(Qt.WindowStaysOnTopHint)
            msgQ.exec()

        except Exception as e:
            msgQ = QMessageBox()
            msgQ.setIcon(QMessageBox.Warning)
            msgQ.setWindowTitle("Erreur email")
            msgQ.setText(str(e))
            msgQ.setWindowFlags(Qt.WindowStaysOnTopHint)
            msgQ.exec()




    def sauvegarder_formulaire(self):
        global data_save_folder
        fichier = f"{data_save_folder}\\formulaire.xlsx"

        if fichier:
            try:
                # Lire le fichier existant
                if os.path.exists(fichier):
                    df = pd.read_excel(fichier)
                else:
                    df = pd.DataFrame(columns=["ID", "Nom", "Prénom", "Email", "Téléphone", "Photos", "Paiement", "Tarif", "Remarque"])

                # Ajouter la nouvelle ligne
                nouvelle_ligne = {
                    "ID": self.ui.lineEdit_id.text(),
                    "Nom": self.ui.lineEdit_nom.text(),
                    "Prénom": self.ui.lineEdit_prenom.text(),
                    "Email": self.ui.lineEdit_email.text(),
                    "Téléphone": "'+33"+self.ui.lineEdit_telephone.text(),
                    "Photos": self.ui.lineEdit_photos.text(),
                    "Paiement": self.ui.comboBox_paiement.currentText(),
                    "Tarif": self.ui.lineEdit_prix.text(),
                    "Remarque": self.ui.textEdit_remarque.toPlainText()
                }

                if nouvelle_ligne['Nom'] == "" or nouvelle_ligne['Prénom'] == "" or nouvelle_ligne['Email'] == "" or nouvelle_ligne['Email'] == "" or nouvelle_ligne['Téléphone'] == "" or nouvelle_ligne['Paiement'] == "Choisir" or nouvelle_ligne['Tarif']=="":
                    msgQ = QMessageBox()
                    msgQ.setIcon(QMessageBox.Information)
                    msgQ.setWindowTitle("Informations manquantes")
                    msgQ.setText("Des informations sont manquantes. La commande n'a pas pu être sauvegardée.")
                    msgQ.setWindowFlags(Qt.WindowStaysOnTopHint)
                    msgQ.exec()
                    return
                if nouvelle_ligne['Photos'] == "":
                    msgQ = QMessageBox()
                    msgQ.setIcon(QMessageBox.Information)
                    msgQ.setWindowTitle("Informations manquantes")
                    msgQ.setText("Vous n'avez pas sélectionné de photos... Veuillez les choisir à l'aide de du bouton \"Sélectionner\". Si vous voulez acheter un ou plusieurs tours, sélectionnez une photo du/des tours choisis et précisez votre choix dans l'espace \"remarque\".")
                    msgQ.setWindowFlags(Qt.WindowStaysOnTopHint)
                    msgQ.exec()
                    return


                df = pd.concat([df, pd.DataFrame([nouvelle_ligne])], ignore_index=True)

                # Sauvegarder dans le même fichier
                df.to_excel(fichier, index=False)


                # Création du dossier de destination
                dossier_base = f"{data_save_folder}\\Commandes"
                if not os.path.exists(dossier_base):
                    os.makedirs(dossier_base)

                id_nom = f"{nouvelle_ligne['ID']}_{nouvelle_ligne['Nom']}"
                chemin_dossier_commande = os.path.join(dossier_base, id_nom)

                if not os.path.exists(chemin_dossier_commande):
                    os.makedirs(chemin_dossier_commande)
                else :
                    for fichier in os.listdir(chemin_dossier_commande):
                        chemin_fichier = os.path.join(chemin_dossier_commande, fichier)
                        if os.path.isdir(chemin_fichier):
                            shutil.rmtree(chemin_fichier)  # Supprime le sous-répertoire
                        else:
                            os.remove(chemin_fichier)  # Supprime le fichier

                # Copier les images sélectionnées
                try:
                    for index in range(self.ui.listWidgetPhotos.count()):
                        selected_item = self.ui.listWidgetPhotos.item(index)
                        if selected_item is not None:
                            chemin_image = selected_item.data(1000)

                        nom_fichier = os.path.basename(chemin_image)
                        destination = os.path.join(chemin_dossier_commande, nom_fichier)

                        global fili_clair_path

                        image_pil = Image.open(chemin_image)
                        image_pil = corriger_orientation(image_pil)
                        if not fili_clair_path =="":
                            image_pil = add_watermark(image_pil)
                        image_pil.save(destination, quality=100)

                        #shutil.copy2(chemin_image, destination)
                except Exception as e:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setWindowTitle("Erreur copie images")
                    msg.setText(f"Une erreur est survenue lors de la copie des images : {e}")
                    msg.setWindowFlags(Qt.WindowStaysOnTopHint)
                    msg.exec()

                dossier_base = f"{data_save_folder}\\Commandes"
                chemin_dossier_temp = os.path.join(dossier_base, "temp")
                if os.path.exists(chemin_dossier_temp):
                    shutil.rmtree(chemin_dossier_temp)



                if not self.ui.lineEdit_email.text().strip() == "":
                    self.envoyer_mail(nouvelle_ligne)

                self.ui.listWidgetPhotos.clear()
                selected_images.clear()

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Succès")
                msg.setText("Informations enregistrées ! Merci pour votre commande.")
                msg.setWindowFlags(Qt.WindowStaysOnTopHint)
                msg.exec()

                self.ui.label_id.setHidden(True);
                self.ui.label_nom.setHidden(True);
                self.ui.label_prenom.setHidden(True);
                self.ui.label_email.setHidden(True);
                self.ui.label_telephone.setHidden(True);
                self.ui.label_photos.setHidden(True);
                self.ui.label_paiement.setHidden(True);
                self.ui.label_prix.setHidden(True);
                self.ui.label_remarque.setHidden(True);
                self.ui.label_type.setHidden(True);
                self.ui.comboBox_type.setHidden(True);
                self.ui.lineEdit_id.setHidden(True);
                self.ui.lineEdit_nom.setHidden(True);
                self.ui.lineEdit_prenom.setHidden(True);
                self.ui.lineEdit_email.setHidden(True);
                self.ui.lineEdit_telephone.setHidden(True);
                self.ui.lineEdit_photos.setHidden(True);
                self.ui.comboBox_paiement.setHidden(True);
                self.ui.textEdit_remarque.setHidden(True);
                self.ui.lineEdit_prix.setHidden(True);
                self.ui.button_sauvegarder_formulaire.setHidden(True);
                self.ui.button_quitter_formulaire.setHidden(True);
                self.ui.button_selectionner.setHidden(True)
                self.ui.button_nouveau_formulaire.setHidden(False)
                self.ui.button_charger_formulaire.setHidden(False)

            except Exception as e:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Erreur")
                msg.setText(f"Erreur lors de la sauvegarde : {e}")
                msg.setWindowFlags(Qt.WindowStaysOnTopHint)
                msg.exec()

    def quitter_formulaire(self):
        self.ui.label_id.setHidden(True);
        self.ui.label_nom.setHidden(True);
        self.ui.label_prenom.setHidden(True);
        self.ui.label_email.setHidden(True);
        self.ui.label_telephone.setHidden(True);
        self.ui.label_photos.setHidden(True);
        self.ui.label_paiement.setHidden(True);
        self.ui.label_prix.setHidden(True);
        self.ui.label_remarque.setHidden(True);
        self.ui.label_type.setHidden(True);
        self.ui.comboBox_type.setHidden(True);
        self.ui.lineEdit_id.setHidden(True);
        self.ui.lineEdit_nom.setHidden(True);
        self.ui.lineEdit_prenom.setHidden(True);
        self.ui.lineEdit_email.setHidden(True);
        self.ui.lineEdit_telephone.setHidden(True);
        self.ui.lineEdit_photos.setHidden(True);
        self.ui.comboBox_paiement.setHidden(True);
        self.ui.textEdit_remarque.setHidden(True);
        self.ui.lineEdit_prix.setHidden(True);
        self.ui.button_sauvegarder_formulaire.setHidden(True);
        self.ui.button_quitter_formulaire.setHidden(True);
        self.ui.button_selectionner.setHidden(True)
        self.ui.button_nouveau_formulaire.setHidden(False)
        self.ui.button_charger_formulaire.setHidden(False)


        self.ui.lineEdit_id.clear()
        self.ui.lineEdit_nom.clear()
        self.ui.lineEdit_prenom.clear()
        self.ui.lineEdit_email.clear()
        self.ui.lineEdit_telephone.clear()
        self.ui.lineEdit_photos.clear()
        self.ui.lineEdit_prix.clear()
        self.ui.comboBox_paiement.setCurrentIndex(0)
        self.ui.textEdit_remarque.clear()

        self.ui.listWidgetPhotos.clear()
        selected_images.clear()



#
#
#
#
#
class PasswordDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Authentification administrateur")
        self.setModal(True)
        self.setFixedSize(300, 120)
        self.setStyleSheet("background-color:rgb(71,72,73)")

        layout = QVBoxLayout()

        self.label = QLabel("Entrez le mot de passe admin :")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        self.button = QPushButton("Valider")
        self.button.clicked.connect(self.check_password)
        self.button.setStyleSheet("""QPushButton {background-color: rgb(100,101,102);
                                            color: rgb(255,255,255);
                                            border-radius: 7px;
                                            text-align: center;}
                                    QPushButton:hover {background-color: rgb(100,101,150);}
                                    QPushButton:pressed{background-color: rgb(185,0,92);}
                                    QPushButton:selected{background-color: rgb(100,101,150);}""")

        layout.addWidget(self.label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.button)
        self.setLayout(layout)

        self.password_valid = False

    def check_password(self):
        global admin_password
        if self.password_input.text() == admin_password:  # <-- Mot de passe ici
            self.password_valid = True
            self.accept()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Erreur")
            msg.setText("Mot de passe incorrect")
            msg.setWindowFlags(Qt.WindowStaysOnTopHint)
            msg.exec()

#
#
#
#
#
class DossierDialog(QDialog):
    def __init__(self, parent=None, model=None, treeView=None):
        super().__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.setWindowTitle("Espace Administrateur")

        self.model = model
        self.treeView = treeView

        self.ui.bouton_choisir.clicked.connect(self.choisir_nouveau_dossier)
        self.ui.bouton_save.clicked.connect(self.choisir_nouveau_dossier_data)
        self.ui.bouton_fermer.clicked.connect(self.fermer_application)
        self.ui.checkBox_restrict_mode.clicked.connect(self.define_restrict_mode)
        self.ui.pushButton_fili_clair.clicked.connect(self.choisir_fili_clair)
        self.ui.pushButton_fili_sombre.clicked.connect(self.choisir_fili_sombre)
        self.ui.pushButton_create_fili.clicked.connect(self.open_create_fili)
        self.ui.Tarifs_auto_checkbox.clicked.connect(self.activer_calcul_tarif)
        self.ui.tarif_checkbox_1.clicked.connect(self.set_tarif)
        self.ui.tarif_checkbox_2.clicked.connect(self.set_tarif)
        self.ui.tarif_checkbox_3.clicked.connect(self.set_tarif)
        self.ui.tarif_checkbox_4.clicked.connect(self.set_tarif)
        self.ui.tarif_checkbox_5.clicked.connect(self.set_tarif)
        self.ui.tarif_checkbox_6.clicked.connect(self.set_tarif)
        self.ui.multiple_tarifs_1.valueChanged.connect(self.set_tarif)
        self.ui.multiple_tarifs_2.valueChanged.connect(self.set_tarif)
        self.ui.multiple_tarifs_3.valueChanged.connect(self.set_tarif)
        self.ui.multiple_tarifs_4.valueChanged.connect(self.set_tarif)
        self.ui.multiple_tarifs_5.valueChanged.connect(self.set_tarif)
        self.ui.multiple_tarifs_6.valueChanged.connect(self.set_tarif)
        self.ui.tarif_1.valueChanged.connect(self.set_tarif)
        self.ui.tarif_2.valueChanged.connect(self.set_tarif)
        self.ui.tarif_3.valueChanged.connect(self.set_tarif)
        self.ui.tarif_4.valueChanged.connect(self.set_tarif)
        self.ui.tarif_5.valueChanged.connect(self.set_tarif)
        self.ui.tarif_6.valueChanged.connect(self.set_tarif)

        self.ui.tarif_checkbox_1.setEnabled(0)
        self.ui.tarif_checkbox_2.setEnabled(0)
        self.ui.tarif_checkbox_3.setEnabled(0)
        self.ui.tarif_checkbox_4.setEnabled(0)
        self.ui.tarif_checkbox_5.setEnabled(0)
        self.ui.tarif_checkbox_6.setEnabled(0)
        self.ui.tarif_1.setEnabled(0)
        self.ui.tarif_2.setEnabled(0)
        self.ui.tarif_3.setEnabled(0)
        self.ui.tarif_4.setEnabled(0)
        self.ui.tarif_5.setEnabled(0)
        self.ui.tarif_6.setEnabled(0)
        self.ui.multiple_tarifs_1.setEnabled(0)
        self.ui.multiple_tarifs_2.setEnabled(0)
        self.ui.multiple_tarifs_3.setEnabled(0)
        self.ui.multiple_tarifs_4.setEnabled(0)
        self.ui.multiple_tarifs_5.setEnabled(0)
        self.ui.multiple_tarifs_6.setEnabled(0)


        global restrict_mode
        if restrict_mode:
            self.ui.checkBox_restrict_mode.setChecked(1)

    def choisir_nouveau_dossier(self):
        dialog = QFileDialog(self)
        dialog.setWindowTitle("Choisir un dossier")
        dialog.setDirectory("D:/")
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setOption(QFileDialog.DontUseNativeDialog, True)
        dialog.setStyleSheet("""
            QFileDialog {
                background-color: #2e2e2e;  /* Fond sombre */
                font-family: 'Segoe UI';
                font-size: 14px;
                color: white;  /* Texte blanc */
                border: none;
            }

            QLabel {
                color: white;  /* Texte blanc pour les labels */
                font-weight: normal;
                font-size: 14px;
                background-color: #2e2e2e;
            }

            QPushButton {
                background-color: #4CAF50;  /* Vert pour les boutons */
                color: white;
                border-radius: 6px;
                padding: 6px 12px;
                font-weight: semi-bold;
            }

            QPushButton:hover {
                background-color: #45a049;  /* Vert foncé au survol */
            }

            QPushButton:pressed {
                background-color: #388e3c;  /* Vert encore plus foncé quand pressé */
            }

            QLineEdit, QComboBox {
                background-color: #333333;  /* Fond sombre pour les champs */
                border: 1px solid #555555;
                padding: 6px;
                border-radius: 4px;
                color: white;  /* Texte blanc dans les champs */
            }

            QTreeView, QListView {
                background-color: #333333;  /* Fond sombre pour la liste des fichiers */
                alternate-background-color: #444444;
                color: white;  /* Texte blanc dans la liste */
                show-decoration-selected: 1;
                outline: none;
            }

            QHeaderView::section {
                background-color: #444444;  /* En-têtes de colonnes foncées */
                padding: 6px;
                border: none;
                font-weight: bold;
                color: white;  /* Texte blanc pour les en-têtes */
            }

            QScrollBar:vertical, QScrollBar:horizontal {
                background: #444444;  /* Fond sombre des barres de défilement */
                border: none;
                width: 10px;
                margin: 0px;
            }

            QScrollBar::handle:vertical, QScrollBar::handle:horizontal {
                background: #777777;  /* Barre de défilement grise */
                border-radius: 4px;
                min-height: 20px;
            }

            QScrollBar::add-line, QScrollBar::sub-line {
                background: none;
                border: none;
            }

            QTreeView::item:selected {
                background-color: #0078D7;  /* Bleu pour la sélection */
                color: white;  /* Texte blanc lors de la sélection */
            }

            QTreeView::item:hover {
                background-color: #555555;  /* Gris foncé au survol */
                color: white;  /* Texte blanc au survol */
            }
        """)

        if dialog.exec():
            dossier = dialog.selectedFiles()[0]
            if dossier:
                global photos_folder
                photos_folder = dossier
                self.model.setRootPath("")  # Réinitialise temporairement
                self.model.setRootPath(photos_folder)
                self.treeView.setRootIndex(self.model.index(photos_folder))

    def choisir_nouveau_dossier_data(self):
        dialog = QFileDialog(self)
        dialog.setWindowTitle("Choisir un dossier pour gérer les commandes")
        dialog.setDirectory("D:/")
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setOption(QFileDialog.DontUseNativeDialog, True)
        dialog.setStyleSheet("""
            QFileDialog {
                background-color: #2e2e2e;  /* Fond sombre */
                font-family: 'Segoe UI';
                font-size: 14px;
                color: white;  /* Texte blanc */
                border: none;
            }

            QLabel {
                color: white;  /* Texte blanc pour les labels */
                font-weight: normal;
                font-size: 14px;
                background-color: #2e2e2e;
            }

            QPushButton {
                background-color: #4CAF50;  /* Vert pour les boutons */
                color: white;
                border-radius: 6px;
                padding: 6px 12px;
                font-weight: semi-bold;
            }

            QPushButton:hover {
                background-color: #45a049;  /* Vert foncé au survol */
            }

            QPushButton:pressed {
                background-color: #388e3c;  /* Vert encore plus foncé quand pressé */
            }

            QLineEdit, QComboBox {
                background-color: #333333;  /* Fond sombre pour les champs */
                border: 1px solid #555555;
                padding: 6px;
                border-radius: 4px;
                color: white;  /* Texte blanc dans les champs */
            }

            QTreeView, QListView {
                background-color: #333333;  /* Fond sombre pour la liste des fichiers */
                alternate-background-color: #444444;
                color: white;  /* Texte blanc dans la liste */
                show-decoration-selected: 1;
                outline: none;
            }

            QHeaderView::section {
                background-color: #444444;  /* En-têtes de colonnes foncées */
                padding: 6px;
                border: none;
                font-weight: bold;
                color: white;  /* Texte blanc pour les en-têtes */
            }

            QScrollBar:vertical, QScrollBar:horizontal {
                background: #444444;  /* Fond sombre des barres de défilement */
                border: none;
                width: 10px;
                margin: 0px;
            }

            QScrollBar::handle:vertical, QScrollBar::handle:horizontal {
                background: #777777;  /* Barre de défilement grise */
                border-radius: 4px;
                min-height: 20px;
            }

            QScrollBar::add-line, QScrollBar::sub-line {
                background: none;
                border: none;
            }

            QTreeView::item:selected {
                background-color: #0078D7;  /* Bleu pour la sélection */
                color: white;  /* Texte blanc lors de la sélection */
            }

            QTreeView::item:hover {
                background-color: #555555;  /* Gris foncé au survol */
                color: white;  /* Texte blanc au survol */
            }
        """)

        if dialog.exec():
            dossier = dialog.selectedFiles()[0]
            if dossier:
                global data_save_folder
                data_save_folder = dossier
    def choisir_fili_clair(self):
        dialog = QFileDialog(self)
        dialog.setWindowTitle("Choisir un dossier pour gérer les commandes")
        dialog.setDirectory("D:/")
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilter("Images PNG (*.png)")
        #dialog.setOption(QFileDialog.DontUseNativeDialog, True)
        dialog.setStyleSheet("""
            QFileDialog {
                background-color: #2e2e2e;  /* Fond sombre */
                font-family: 'Segoe UI';
                font-size: 14px;
                color: white;  /* Texte blanc */
                border: none;
            }
            QLabel {
                color: white;  /* Texte blanc pour les labels */
                font-weight: normal;
                font-size: 14px;
                background-color: #2e2e2e;
            }
            QPushButton {
                background-color: #4CAF50;  /* Vert pour les boutons */
                color: white;
                border-radius: 6px;
                padding: 6px 12px;
                font-weight: semi-bold;
            }
            QPushButton:hover {
                background-color: #45a049;  /* Vert foncé au survol */
            }
            QPushButton:pressed {
                background-color: #388e3c;  /* Vert encore plus foncé quand pressé */
            }
            QLineEdit, QComboBox {
                background-color: #333333;  /* Fond sombre pour les champs */
                border: 1px solid #555555;
                padding: 6px;
                border-radius: 4px;
                color: white;  /* Texte blanc dans les champs */
            }
            QTreeView, QListView {
                background-color: #333333;  /* Fond sombre pour la liste des fichiers */
                alternate-background-color: #444444;
                color: white;  /* Texte blanc dans la liste */
                show-decoration-selected: 1;
                outline: none;
            }
            QHeaderView::section {
                background-color: #444444;  /* En-têtes de colonnes foncées */
                padding: 6px;
                border: none;
                font-weight: bold;
                color: white;  /* Texte blanc pour les en-têtes */
            }
            QScrollBar:vertical, QScrollBar:horizontal {
                background: #444444;  /* Fond sombre des barres de défilement */
                border: none;
                width: 10px;
                margin: 0px;
            }
            QScrollBar::handle:vertical, QScrollBar::handle:horizontal {
                background: #777777;  /* Barre de défilement grise */
                border-radius: 4px;
                min-height: 20px;
            }
            QScrollBar::add-line, QScrollBar::sub-line {
                background: none;
                border: none;
            }
            QTreeView::item:selected {
                background-color: #0078D7;  /* Bleu pour la sélection */
                color: white;  /* Texte blanc lors de la sélection */
            }
            QTreeView::item:hover {
                background-color: #555555;  /* Gris foncé au survol */
                color: white;  /* Texte blanc au survol */
            }""")

        if dialog.exec():
            chemin = dialog.selectedFiles()[0]
            if chemin:
                global fili_clair_path
                fili_clair_path = chemin
                self.ui.lineEdit_fili_clair.setText(fili_clair_path)

    def choisir_fili_sombre(self):
        dialog = QFileDialog(self)
        dialog.setWindowTitle("Choisir un dossier pour gérer les commandes")
        dialog.setDirectory("D:/")
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilter("Images PNG (*.png)")
        #dialog.setOption(QFileDialog.DontUseNativeDialog, True)
        dialog.setStyleSheet("""
            QFileDialog {
                background-color: #2e2e2e;  /* Fond sombre */
                font-family: 'Segoe UI';
                font-size: 14px;
                color: white;  /* Texte blanc */
                border: none;
            }
            QLabel {
                color: white;  /* Texte blanc pour les labels */
                font-weight: normal;
                font-size: 14px;
                background-color: #2e2e2e;
            }
            QPushButton {
                background-color: #4CAF50;  /* Vert pour les boutons */
                color: white;
                border-radius: 6px;
                padding: 6px 12px;
                font-weight: semi-bold;
            }
            QPushButton:hover {
                background-color: #45a049;  /* Vert foncé au survol */
            }
            QPushButton:pressed {
                background-color: #388e3c;  /* Vert encore plus foncé quand pressé */
            }
            QLineEdit, QComboBox {
                background-color: #333333;  /* Fond sombre pour les champs */
                border: 1px solid #555555;
                padding: 6px;
                border-radius: 4px;
                color: white;  /* Texte blanc dans les champs */
            }
            QTreeView, QListView {
                background-color: #333333;  /* Fond sombre pour la liste des fichiers */
                alternate-background-color: #444444;
                color: white;  /* Texte blanc dans la liste */
                show-decoration-selected: 1;
                outline: none;
            }
            QHeaderView::section {
                background-color: #444444;  /* En-têtes de colonnes foncées */
                padding: 6px;
                border: none;
                font-weight: bold;
                color: white;  /* Texte blanc pour les en-têtes */
            }
            QScrollBar:vertical, QScrollBar:horizontal {
                background: #444444;  /* Fond sombre des barres de défilement */
                border: none;
                width: 10px;
                margin: 0px;
            }
            QScrollBar::handle:vertical, QScrollBar::handle:horizontal {
                background: #777777;  /* Barre de défilement grise */
                border-radius: 4px;
                min-height: 20px;
            }
            QScrollBar::add-line, QScrollBar::sub-line {
                background: none;
                border: none;
            }
            QTreeView::item:selected {
                background-color: #0078D7;  /* Bleu pour la sélection */
                color: white;  /* Texte blanc lors de la sélection */
            }
            QTreeView::item:hover {
                background-color: #555555;  /* Gris foncé au survol */
                color: white;  /* Texte blanc au survol */
            }""")

        if dialog.exec():
            chemin = dialog.selectedFiles()[0]
            if chemin:
                global fili_sombre_path
                fili_sombre_path = chemin
                self.ui.lineEdit_fili_sombre.setText(fili_sombre_path)


    def define_restrict_mode(self):
        global restrict_mode
        restrict_mode = self.ui.checkBox_restrict_mode.isChecked()

    def open_create_fili(self):
        fili_interface = Fili()
        fili_interface.exec()

    def activer_calcul_tarif(self):
        global tarif_multiple_1
        global tarif_multiple_2
        global tarif_multiple_3
        global tarif_multiple_4
        global tarif_multiple_tour_5
        global tarif_multiple_tour_6
        global tarif_1
        global tarif_2
        global tarif_3
        global tarif_4
        global tarif_5
        global tarif_6
        global tarif_supp
        global calcul_tarif_auto

        if self.ui.Tarifs_auto_checkbox.isChecked():
            calcul_tarif_auto = 1
            self.ui.tarif_checkbox_1.setEnabled(1)
            self.ui.tarif_checkbox_2.setEnabled(1)
            self.ui.tarif_checkbox_3.setEnabled(1)
            self.ui.tarif_checkbox_4.setEnabled(1)
            self.ui.tarif_checkbox_5.setEnabled(1)
            self.ui.tarif_checkbox_6.setEnabled(1)
            self.ui.tarif_1.setEnabled(1)
            self.ui.tarif_2.setEnabled(1)
            self.ui.tarif_3.setEnabled(1)
            self.ui.tarif_4.setEnabled(1)
            self.ui.tarif_5.setEnabled(1)
            self.ui.tarif_6.setEnabled(1)
            self.ui.multiple_tarifs_1.setEnabled(1)
            self.ui.multiple_tarifs_2.setEnabled(1)
            self.ui.multiple_tarifs_3.setEnabled(1)
            self.ui.multiple_tarifs_4.setEnabled(1)
            self.ui.multiple_tarifs_5.setEnabled(1)
            self.ui.multiple_tarifs_6.setEnabled(1)

            self.set_tarif()
            self.ui.frame.setStyleSheet("""
                    QLabel{
                        color:white;
                        border : none;}
                    QFrame{
                            border-radius:5px;
                            border:none}
                    QSpinBox {
                       background-color: rgb(41,42,43);
                            color:white;}
                    QDoubleSpinBox{
                            background-color:rgb(41,42,43);
                            color:white;
                            border:none;
                            border-radius:5px;}
                    QCheckBox::indicator {
                            background-color: rgb(41,42,43);
                            border: none;
                            border-radius: 5px;}
                    QCheckBox::indicator:unchecked {
                        background-color: rgb(41,42,43);}
                    QCheckBox::indicator:unchecked:hover {
                        background-color: rgb(255,0,127);}
                    QCheckBox::indicator:unchecked:pressed {
                        background-color: rgb(185,0,92); }
                    QCheckBox::indicator:checked {
                            border:4px solid rgb(101,102,103);
                        background-color: rgb(151,152,153);}
                    QCheckBox::indicator:checked:hover {
                            border:4px solid rgb(255,0,127);}
                    QCheckBox::indicator:checked:pressed {
                            border:4px solid rgb(185,0,92); }""")
        else :
            calcul_tarif_auto = 0
            self.ui.tarif_checkbox_1.setEnabled(0)
            self.ui.tarif_checkbox_2.setEnabled(0)
            self.ui.tarif_checkbox_3.setEnabled(0)
            self.ui.tarif_checkbox_4.setEnabled(0)
            self.ui.tarif_checkbox_5.setEnabled(0)
            self.ui.tarif_checkbox_6.setEnabled(0)
            self.ui.tarif_1.setEnabled(0)
            self.ui.tarif_2.setEnabled(0)
            self.ui.tarif_3.setEnabled(0)
            self.ui.tarif_4.setEnabled(0)
            self.ui.tarif_5.setEnabled(0)
            self.ui.tarif_6.setEnabled(0)
            self.ui.multiple_tarifs_1.setEnabled(0)
            self.ui.multiple_tarifs_2.setEnabled(0)
            self.ui.multiple_tarifs_3.setEnabled(0)
            self.ui.multiple_tarifs_4.setEnabled(0)
            self.ui.multiple_tarifs_5.setEnabled(0)
            self.ui.multiple_tarifs_6.setEnabled(0)
            self.ui.frame.setStyleSheet("""
                    QLabel{
                        color:rgb(160,160,160);
                        border : none;}
                    QFrame{
                            border-radius:5px;
                            border:none}
                    QSpinBox {
                       background-color: rgb(41,42,43);
                            color:rgb(160,160,160);}
                    QDoubleSpinBox{
                            background-color:rgb(41,42,43);
                            color:rgb(160,160,160);
                            border:none;
                            border-radius:5px;}
                    QCheckBox::indicator {
                            background-color: rgb(41,42,43);
                            border: none;
                            border-radius: 5px;}
                    QCheckBox::indicator:unchecked {
                        background-color: rgb(41,42,43);}
                    QCheckBox::indicator:unchecked:hover {
                        background-color: rgb(255,0,127);}
                    QCheckBox::indicator:unchecked:pressed {
                        background-color: rgb(185,0,92); }
                    QCheckBox::indicator:checked {
                            border:4px solid rgb(101,102,103);
                        background-color: rgb(151,152,153);}
                    QCheckBox::indicator:checked:hover {
                            border:4px solid rgb(255,0,127);}
                    QCheckBox::indicator:checked:pressed {
                            border:4px solid rgb(185,0,92); }""")

            tarif_multiple_1 = 0
            tarif_multiple_2 = 0
            tarif_multiple_3 = 0
            tarif_multiple_4 = 0
            tarif_multiple_tour_5 = 0
            tarif_multiple_tour_6 = 0

            tarif_1 = 0
            tarif_2 = 0
            tarif_3 = 0
            tarif_4 = 0
            tarif_5 = 0
            tarif_6 = 0

            tarif_supp = 0


    def set_tarif(self):
        global tarif_multiple_1
        global tarif_multiple_2
        global tarif_multiple_3
        global tarif_multiple_4
        global tarif_multiple_tour_5
        global tarif_multiple_tour_6
        global tarif_1
        global tarif_2
        global tarif_3
        global tarif_4
        global tarif_5
        global tarif_6
        global tarif_supp

        tarif_multiple_1 = self.ui.multiple_tarifs_1.value()
        tarif_multiple_2 = self.ui.multiple_tarifs_2.value()
        tarif_multiple_3 = self.ui.multiple_tarifs_3.value()
        tarif_multiple_4 = self.ui.multiple_tarifs_4.value()
        tarif_multiple_tour_5 = self.ui.multiple_tarifs_5.value()
        tarif_multiple_tour_6 = self.ui.multiple_tarifs_6.value()

        tarif_1 = self.ui.tarif_1.value()
        tarif_2 = self.ui.tarif_2.value()
        tarif_3 = self.ui.tarif_3.value()
        tarif_4 = self.ui.tarif_4.value()
        tarif_5 = self.ui.tarif_5.value()
        tarif_6 = self.ui.tarif_6.value()

        tarif_supp = self.ui.tarif_supp.value()


    def fermer_application(self):
        # Ferme l'application
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Confirmation de fermeture")
        msg_box.setText("Voulez-vous vraiment quitter l'application ?")
        msg_box.setIcon(QMessageBox.Question)

        # Création de boutons personnalisés
        bouton_oui = msg_box.addButton("Oui", QMessageBox.AcceptRole)
        bouton_oui.setStyleSheet("""QPushButton {background-color: rgb(100,151,102);
                                                    color: rgb(255,255,255);
                                                    border-radius: 7px;
                                                    text-align: center;}
                                            QPushButton:hover {background-color: rgb(100,101,150);}
                                            QPushButton:pressed{background-color: rgb(185,0,92);}
                                            QPushButton:selected{background-color: rgb(100,101,150);}""")
        bouton_oui.setMinimumSize(50, 30)
        bouton_non = msg_box.addButton("Non", QMessageBox.RejectRole)
        bouton_non.setStyleSheet("""QPushButton {background-color: rgb(200,101,102);
                                                    color: rgb(255,255,255);
                                                    border-radius: 7px;
                                                    text-align: center;}
                                            QPushButton:hover {background-color: rgb(100,101,150);}
                                            QPushButton:pressed{background-color: rgb(185,0,92);}
                                            QPushButton:selected{background-color: rgb(100,101,150);}""")
        bouton_non.setMinimumSize(50, 30)

        msg_box.exec()

        if msg_box.clickedButton() == bouton_oui:
            QApplication.quit()


#
#
#
#
#

class Fili(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Fili()
        self.ui.setupUi(self)
        self.setWindowTitle("Création d'un filigrane")

        # Connexions
        self.ui.selectLogoButton.clicked.connect(self.select_logo)
        self.ui.leftTextLineEdit.textChanged.connect(self.update_watermark_preview)
        self.ui.rightTextLineEdit.textChanged.connect(self.update_watermark_preview)
        self.ui.generateButton.clicked.connect(self.save_watermark)
        self.ui.fontSizeSpinBox.valueChanged.connect(self.update_watermark_preview)
        self.ui.leftTextXOffsetSlider.valueChanged.connect(self.update_watermark_preview)
        self.ui.rightTextXOffsetSlider.valueChanged.connect(self.update_watermark_preview)
        #self.ui.textYOffsetSlider.valueChanged.connect(self.update_watermark_preview)

        self.logo_path = ""

    def select_logo(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Choisir un logo", "", "Images (*.png *.jpg *.bmp)")
        if file_name:
            self.logo_path = file_name
            self.ui.logoPathLabel.setText(file_name)
            self.update_watermark_preview()

    def update_watermark_preview(self):
        if not self.logo_path:
            return

        left_text = self.ui.leftTextLineEdit.toPlainText()
        right_text = self.ui.rightTextLineEdit.toPlainText()

        pixmap = self.create_watermark_pixmap(left_text, right_text, self.logo_path)
        self.ui.filigrane_label.setPixmap(pixmap)

    def save_watermark(self):
        if not self.logo_path:
            self.ui.statusLabel.setText("Veuillez choisir un logo.")
            return

        left_text = self.ui.leftTextLineEdit.toPlainText()
        right_text = self.ui.rightTextLineEdit.toPlainText()

        # Ouvrir une boîte de dialogue pour choisir le chemin de sauvegarde
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog  # Optionnel selon ta plateforme
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Enregistrer le filigrane",
            "filigrane.png",  # Nom par défaut
            "Images PNG (*.png);;Toutes les fichiers (*)",
            options=options
        )

        # Si l'utilisateur annule, on ne fait rien
        if not file_path:
            return

        # Créer et sauvegarder le filigrane
        pixmap = self.create_watermark_pixmap(left_text, right_text, self.logo_path)
        if pixmap.save(file_path):
            self.ui.filigrane_label.setText(f"Filigrane généré : {file_path}")
        else:
            self.ui.statusLabel.setText("Erreur lors de la sauvegarde du filigrane.")

    def create_watermark_pixmap(self, left_text, right_text, logo_path):
        width, height = 1200, 250
        watermark = QPixmap(width, height)
        watermark.fill(Qt.transparent)

        painter = QPainter(watermark)
        painter.setRenderHint(QPainter.Antialiasing)

        # Logo
        logo = QPixmap(logo_path)
        if logo.isNull():
            return watermark

        logo_height = int(height * 0.8)
        logo = logo.scaledToHeight(logo_height, Qt.SmoothTransformation)
        logo_x = (width - logo.width()) // 2
        logo_y = (height - logo.height()) // 2
        painter.drawPixmap(logo_x, logo_y, logo)

        # Texte
        font_size = self.ui.fontSizeSpinBox.value()
        font = QFont("Arial", font_size)
        painter.setFont(font)
        painter.setPen(QColor(255, 255, 255))

        # Offsets
        x_offset_left = self.ui.leftTextXOffsetSlider.value()
        x_offset_right = self.ui.rightTextXOffsetSlider.value()
        y_offset = 0
        print(f"x_offset_left : {x_offset_left}, x_offset_right : {x_offset_right}")

        # Texte à gauche
        left_rect = QRect(
            20 + x_offset_left,
            y_offset,
            (width // 2) - logo.width() // 2 - 40,
            height
        )
        painter.drawText(left_rect, Qt.AlignVCenter | Qt.AlignLeft | Qt.TextWordWrap, left_text)

        # Texte à droite
        right_rect = QRect(
            (width // 2) + logo.width() // 2 + 20 + x_offset_right,
            y_offset,
            (width // 2) - logo.width() // 2 - 40,
            height
        )
        painter.drawText(right_rect, Qt.AlignVCenter | Qt.AlignRight | Qt.TextWordWrap, right_text)


        painter.end()
        return watermark



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Commande de photos")
        self.setWindowIcon(QIcon("icone.png"))


        # Menu Admin
        menu_admin = self.menuBar().addMenu("Admin")
        action_choisir_dossier = menu_admin.addAction("Espace administrateur")
        action_choisir_dossier.triggered.connect(self.ouvrir_dialogue_dossier)
        action_update_window = menu_admin.addAction("Mise à jour Admin")
        action_update_window.triggered.connect(self.maj_window)

        # Liste des chemins des images sélectionnées
        self.chemin_images = []
        self.index_image_courante = -1
        global selected_images

        # Modèle de fichiers
        self.model = QFileSystemModel()
        self.model.setRootPath('')
        self.model.setNameFilters(["*.png", "*.jpg", "*.jpeg"])
        self.model.setNameFilterDisables(False)

        self.ui.treeView.setModel(self.model)
        self.ui.treeView.setRootIndex(self.model.index("C:"))
        self.ui.treeView.setColumnHidden(1, True)  # Taille
        self.ui.treeView.setColumnHidden(2, True)  # Type
        self.ui.treeView.setColumnHidden(3, True)  # Type

        self.ui.treeView.setColumnWidth(0, 280)

        self.ui.treeView.setSortingEnabled(True)
        self.ui.treeView.sortByColumn(3, Qt.AscendingOrder)

        # Signaux
        self.ui.treeView.doubleClicked.connect(self.afficher_image)
        self.ui.button_suivant.clicked.connect(self.afficher_suivante)
        self.ui.button_precedent.clicked.connect(self.afficher_precedente)
        self.ui.button_selectionner.clicked.connect(self.toggle_selection)
        self.ui.listWidgetPhotos.doubleClicked.connect(self.afficher_image_depuis_liste)
        self.ui.pushButton_refresh.clicked.connect(self.rafraichir_dossier)


        image = QImage("_internal\\ressources\\M.A.PHOTO.png")
        pixmap = QPixmap.fromImage(image)
        pixmap = pixmap.scaledToHeight(self.ui.label_logo.height(), Qt.SmoothTransformation)
        rounded = self.rounded_pixmap(pixmap, 5)
        self.ui.label_logo.setPixmap(rounded)



        self.formulaire_handler = FormulaireHandler(self.ui)
        self.show()

    def rounded_pixmap(self, pixmap, radius):
        size = pixmap.size()
        # Crée un QPixmap transparent pour le résultat
        rounded = QPixmap(size)
        rounded.fill(Qt.transparent)
        # Prépare un QPainter avec clipping arrondi
        painter = QPainter(rounded)
        painter.setRenderHint(QPainter.Antialiasing)
        path = QPainterPath()
        path.addRoundedRect(0, 0, size.width(), size.height(), radius, radius)
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, pixmap)
        painter.end()
        return rounded

    def closeEvent(self, event):
        if event.spontaneous() and restrict_mode==1:
            event.ignore()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Information")
            msg.setText("Vous ne pouvez pas fermer l'application")
            msg.setWindowFlags(Qt.WindowStaysOnTopHint)
            msg.exec()
        else:
            event.accept()


    def afficher_image(self, index):
        if self.model.isDir(index):
            return

        chemin_image = self.model.filePath(index)
        parent_index = index.parent()

        self.chemin_images = []
        for row in range(self.model.rowCount(parent_index)):
            idx = self.model.index(row, 0, parent_index)
            if not self.model.isDir(idx):
                chemin = self.model.filePath(idx)
                ext = os.path.splitext(chemin)[1].lower()
                if ext in [".jpg", ".jpeg", ".png", ".bmp", ".gif"]:
                    self.chemin_images.append(chemin)

        try:
            self.index_image_courante = self.chemin_images.index(chemin_image)
        except ValueError:
            self.index_image_courante = -1

        self.afficher_image_depuis_chemin(chemin_image)
        self.ui.labelNomImage.setText(os.path.basename(chemin_image))
        self.update_button_color()

    def update_button_color(self):
        chemin_image = self.chemin_images[self.index_image_courante]
        if chemin_image in selected_images:
            self.ui.button_selectionner.setStyleSheet("""QPushButton {background-color: rgb(100,151,102);
                                                                    color: rgb(255,255,255);
                                                                    border-radius: 7px;
                                                                    text-align: center;}
                                                        QPushButton:hover {background-color: rgb(100,101,150);}
                                                        QPushButton:pressed{background-color: rgb(185,0,92);}
                                                        QPushButton:selected{background-color: rgb(100,101,150);}""")
        else:
            self.ui.button_selectionner.setStyleSheet("""QPushButton {background-color: rgb(100,101,102);
                                                                    color: rgb(255,255,255);
                                                                    border-radius: 7px;
                                                                    text-align: center;}
                                                        QPushButton:hover {background-color: rgb(100,101,150);}
                                                        QPushButton:pressed{background-color: rgb(185,0,92);}
                                                        QPushButton:selected{background-color: rgb(100,101,150);}""")

    def afficher_image_depuis_chemin(self, chemin_image):
        global fili_clair_path

        try:
            image_pil = Image.open(chemin_image)
            image_pil = corriger_orientation(image_pil)
            if not fili_clair_path =="":
                image_pil = add_watermark(image_pil)
            image_qt = pil_to_qimage(image_pil)
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Erreur")
            msg.setText(f"Impossible de charger l'image : {chemin_image}\n{e}")
            msg.setWindowFlags(Qt.WindowStaysOnTopHint)
            msg.exec()
            return

        pixmap = QPixmap.fromImage(image_qt)
        label_size = self.ui.labelImage.size()
        if label_size.width() == 0 or label_size.height() == 0:
            label_size = QSize(400, 400)

        self.ui.labelImage.setPixmap(pixmap.scaled(
            label_size,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        ))

    def rafraichir_dossier(self):
        global photos_folder
        try:
            global photos_folder
            if photos_folder and os.path.exists(photos_folder):
                self.model.setRootPath("")  # Réinitialise temporairement
                time.sleep(0.1)
                self.model.setRootPath(photos_folder)
                time.sleep(0.1)
                self.ui.treeView.setRootIndex(self.model.index(photos_folder))
        except Exception as e:
            print(f"Erreur lors du rafraîchissement de l'arborescence : {e}")


    def afficher_suivante(self):
        if 0 <= self.index_image_courante < len(self.chemin_images) - 1:
            self.index_image_courante += 1
            self.afficher_image_depuis_chemin(self.chemin_images[self.index_image_courante])
            self.ui.labelNomImage.setText(os.path.basename(self.chemin_images[self.index_image_courante]))
            self.update_button_color()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Right:
            self.afficher_suivante()
        if event.key() == Qt.Key_Left:
            self.afficher_precedente()

    def afficher_precedente(self):
        if self.index_image_courante > 0:
            self.index_image_courante -= 1
            self.afficher_image_depuis_chemin(self.chemin_images[self.index_image_courante])
            self.ui.labelNomImage.setText(os.path.basename(self.chemin_images[self.index_image_courante]))
            self.update_button_color()

    def toggle_selection(self):
        if self.index_image_courante == -1:
            return        

        chemin_image = self.chemin_images[self.index_image_courante]

        if chemin_image in selected_images:
            selected_images.remove(chemin_image)
            item = self.get_item_from_chemin(chemin_image)
            if item:
                self.ui.listWidgetPhotos.takeItem(self.ui.listWidgetPhotos.row(item))
            self.ui.button_selectionner.setStyleSheet("""QPushButton {background-color: rgb(100,101,102);
                                                                    color: rgb(255,255,255);
                                                                    border-radius: 7px;
                                                                    text-align: center;}
                                                        QPushButton:hover {background-color: rgb(100,101,150);}
                                                        QPushButton:pressed{background-color: rgb(185,0,92);}
                                                        QPushButton:selected{background-color: rgb(100,101,150);}""")
        else:
            selected_images.append(chemin_image)
            pixmap = QPixmap(chemin_image).scaled(50, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            icon = QPixmap(pixmap)
            item = QListWidgetItem()
            item.setText(os.path.basename(chemin_image))
            item.setIcon(icon)
            item.setData(1000, chemin_image)
            self.ui.listWidgetPhotos.addItem(item)
            self.ui.button_selectionner.setStyleSheet("""QPushButton {background-color: rgb(100,151,102);
                                                                    color: rgb(255,255,255);
                                                                    border-radius: 7px;
                                                                    text-align: center;}
                                                        QPushButton:hover {background-color: rgb(100,101,150);}
                                                        QPushButton:pressed{background-color: rgb(185,0,92);}
                                                        QPushButton:selected{background-color: rgb(100,101,150);}""")


        nom_photos_selected = ""

        for index in range(self.ui.listWidgetPhotos.count()):
            selected_item = self.ui.listWidgetPhotos.item(index)
            if selected_item is not None:
                chemin_image = selected_item.data(1000)

            nom_photos_selected = nom_photos_selected + os.path.basename(chemin_image) +";"

        self.ui.lineEdit_photos.setText(nom_photos_selected)


    def get_item_from_chemin(self, chemin_image):
        for i in range(self.ui.listWidgetPhotos.count()):
            item = self.ui.listWidgetPhotos.item(i)
            if item.data(1000) == chemin_image:
                return item
        return None

    def afficher_image_depuis_liste(self):
        selected_item = self.ui.listWidgetPhotos.currentItem()
        if selected_item:
            chemin_image = selected_item.data(1000)
            self.afficher_image_depuis_chemin(chemin_image)
            self.ui.labelNomImage.setText(os.path.basename(chemin_image))
            self.chemin_images = [chemin_image]
            self.index_image_courante = 0
            self.update_button_color()


    def ouvrir_dialogue_dossier(self):
        if restrict_mode :
            # Fenêtre de mot de passe
            dialog = PasswordDialog(self)
            if dialog.exec() and dialog.password_valid:
                dossier_dialog = DossierDialog(self, model=self.model, treeView=self.ui.treeView)
                dossier_dialog.exec()
        else :
            dossier_dialog = DossierDialog(self, model=self.model, treeView=self.ui.treeView)
            dossier_dialog.exec()

    def maj_window(self):
        if restrict_mode:
            self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
            self.showFullScreen()
            self.show()
        else:
            self.setWindowFlags(Qt.Window & ~Qt.FramelessWindowHint & ~Qt.WindowStaysOnTopHint)
            self.showNormal()

        self.show()

    def calcul_tarif(self):
        global tarif_multiple_1
        global tarif_multiple_2
        global tarif_multiple_3
        global tarif_multiple_4
        global tarif_multiple_tour_5
        global tarif_multiple_tour_6
        global tarif_1
        global tarif_2
        global tarif_3
        global tarif_4
        global tarif_5
        global tarif_6
        global tarif_supp
        global calcul_tarif_auto


#
#
#
#
#
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
