"""
Votre description du programme
@auteur(e)s     Mahdi Slimani Claude Bernard Lucien
@matricules     e6249382 e2236254
@date              21-05-2024

"""


import csv
import os
import json
import math
from math import radians, sin, cos, sqrt, atan2

class donnees_geo:
    #definit la ville pays latitude et longitude
    def __init__(self, ville, pays, latitude, longitude):
        self.ville = ville
        self.pays = pays
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    def __str__(self):
        return f"{self.ville}, {self.pays}, {self.latitude}, {self.longitude}"


def liredonneescsv():
    donnees = []
    with open('donnees.csv', 'r', encoding='utf-8') as f:
        lecteur_csv = csv.reader(f)
        next(lecteur_csv) #ignore la premeire ligne quand on l'affiche  
        for ligne in lecteur_csv:
            ville, pays, latitude, longitude = ligne
            donnee = donnees_geo(ville, pays, latitude, longitude)
            donnees.append(donnee)
    return donnees


donnees = liredonneescsv() #appelle la fonction pour lire les donner CSV
for donnee in donnees:
    print(donnee) #affiche chaque donnee

def ecriredonneesjson(nom_fichier, donnees):
    liste_dictionnaires = [donnee.__dict__ for donnee in donnees] #convertit les objets donneesgeo en dictionnaire.
    with open(nom_fichier, 'w', encoding='utf-8') as f1:
        json.dump(liste_dictionnaires, f1, indent = 4,ensure_ascii=False) #ecrit les dictionnaire dans un fichier JSON

def trouverdistancemin(fichier_json):
    
    def calculerdistance(ville1, ville2):
        lat1, lon1 = math.radians(ville1['latitude']), math.radians(ville1['longitude'])
        lat2, lon2 = math.radians(ville2['latitude']), math.radians(ville2['longitude'])

        r = 6371 #rayon de la terre = Km

        delta_lat = lat2 - lat1
        delta_lon = lon2 - lon1
        #calcule avec la formule 
        a = math.sin(delta_lat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(delta_lon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = r * c

        return distance

    with open(fichier_json, 'r', encoding='utf-8') as f2:
        liste_donnees = json.load(f2) #charge les données JSON dans une liste de dictionnaire.


    with open('distances.csv', 'w', newline='', encoding='utf-8') as fcsv:
        writer = csv.writer(fcsv)
        writer.writerow(['ville1', 'ville2', 'distance'])

        for i, ville1 in enumerate(liste_donnees):# parcours de chaque ville dans liste_donnees avec son index i
            for ville2 in liste_donnees[i+1:]:# parcours des ville restante dans liste_donnees a partir de l'élément suivant apres ville1
                distance = calculerdistance(ville1, ville2)  # calcul de la distance entre ville1 et ville2
                writer.writerow([f"{ville1['ville']} {ville1['pays']} {ville1['latitude']} {ville1['longitude']}",
                                 f"{ville2['ville']} {ville2['pays']} {ville2['latitude']} {ville2['longitude']}",distance])# ecrit les entete dans le fichier CSV

    print("resultats ont ete enregistres dans distances.csv.") #message de confirmation


def afficher_menu():
    print("\nMenu :")
    print("1- lire donnees du fichier CSV, creer les objets et afficher donnees")
    print("2- sauvegarder donnees dans un fichier JSON")
    print("3- lire les données du fichier JSON et faire le calcule de distance minimale entre deux ville et sauvegarder les calcul dans distances.csv")
    print("q- quitter ")

def menu():
    donnees = None

    while True:
        afficher_menu()
        choix = input("entrez un numero pour choisir une option ou 'q' pour quitter : ")

        if choix == '1':
            donnees = liredonneescsv()# lit les donnee CSV et les stockes dans la variable donnee
            print("fichier CSV :")
            for donnee in donnees:
                print(donnee)
        elif choix == '2':
            if donnees is None:
                print("vous devez d'abord lire les donnees du fichier CSV (option 1)")
            else:
                ecriredonneesjson('Sauvegarde.json', donnees)  # ecrit les donnees dans un fichier JSON
                print("donnees sauvegardées -> Sauvegarde.json")
        elif choix == '3':
            if os.path.exists('Sauvegarde.json'): # verifier l'existence du fichier JSON avant de tenter de le lire 
                trouverdistancemin('Sauvegarde.json')# calcule la distance minimale entre les ville a partir du fichier JSON
            else:
                print("vous devez d'abord sauvegarder les données dans un fichier JSON (option 2)")
        elif choix == 'q':
            print("merci, bye!")
            break
        else:
            print("choix invalide -> veuillez entrer un numéro valide.")

if __name__ == "__main__":
    menu()# appelle la fonction principale pour demarrer le programme