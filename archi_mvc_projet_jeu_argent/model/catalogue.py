import csv
from model.jeu import Jeu


class Catalogue:
    def __init__(self, chemin_csv):
        self.jeux = self.charger_csv(chemin_csv)

    def charger_csv(self, chemin):
    jeux = []

    with open(chemin, newline="", encoding="utf-8") as fichier:
        lecteur = csv.DictReader(fichier)

        for ligne in lecteur:
            nom = ligne["jeu"]

            prix = int(ligne["prix"].replace(" ", "").replace(" ", ""))
            unites = int(ligne["unites"].replace(" ", "").replace(" ", ""))

            gains = {}

            for colonne, valeur in ligne.items():
                if colonne in ("jeu", "prix", "unites", "total_gains"):
                    continue

                if valeur and valeur.strip():
                    gain = int(colonne.replace(" ", "").replace(" ", ""))
                    nb = int(valeur.replace(" ", "").replace(" ", ""))
                    gains[gain] = nb

            jeux.append(Jeu(nom, prix, unites, gains))

    return jeux


    def get_jeu(self, nom):
        for jeu in self.jeux:
            if jeu.nom == nom:
                return jeu
        return None
