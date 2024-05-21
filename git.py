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

def trouverdistancemin(fichier_json):
    
    def calculer_distance(ville1, ville2):
       
        lat1, lon1 = radians(ville1['latitude']), radians(ville1['longitude'])
        lat2, lon2 = radians(ville2['latitude']), radians(ville2['longitude'])

        r = 6371

        delta_lat = lat2 - lat1
        delta_lon = lon2 - lon1

        a = sin(delta_lat / 2)**2 + cos(lat1) * cos(lat2) * sin(delta_lon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = r * c

        return distance

    with open(fichier_json, 'r', encoding='utf-8') as f2:
        liste_donnees = json.load(f2)

    distance_min = None
    ville1_min = None
    ville2_min = None

    for i, ville1 in enumerate(liste_donnees):
        for ville2 in liste_donnees[i+1:]:
            distance = calculer_distance(ville1, ville2)
            if distance_min is None or distance < distance_min:
                distance_min = distance
                ville1_min = ville1
                ville2_min = ville2

    if ville1_min is not None and ville2_min is not None:
        print(f"distance minimale entre {ville1_min['ville']} et {ville2_min['ville']} := {distance_min} km")
    else:
        print("aucune distance minimale trouver")

    with open('distances.csv', 'w', newline='', encoding='utf-8') as fcsv:
        writer = csv.writer(fcsv)
        writer.writerow(['ville1', 'ville2', 'distance'])
        writer.writerow([ville1_min['ville'], ville2_min['ville'], distance_min])


