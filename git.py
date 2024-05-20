import csv
import json
from math import radians, sin, cos, sqrt, atan2

class donnees_geo:
    def __init__(self, ville, pays, latitude, longitude):
        self.ville = ville
        self.pays = pays
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    def __str__(self):
        return f"{self.ville}, {self.pays}, {self.latitude}, {self.longitude}"


def lire_donnees_csv():
    donnees = []
    with open('donnees.csv', 'r', encoding='utf-8') as f:
        lecteur_csv = csv.reader(f)
        next(lecteur_csv)  
        for ligne in lecteur_csv:
            ville, pays, latitude, longitude = ligne
            donnee = donnees_geo(ville, pays, latitude, longitude)
            donnees.append(donnee)
    return donnees


donnees = lire_donnees_csv()
for donnee in donnees:
    print(donnee)

def ecriredonneesjson(nom_fichier, donnees):
    liste_dictionnaires = [donnee.__dict__ for donnee in donnees]
    with open(nom_fichier, 'w', encoding='utf-8') as f1:
        json.dump(liste_dictionnaires, f1, indent = 4)
