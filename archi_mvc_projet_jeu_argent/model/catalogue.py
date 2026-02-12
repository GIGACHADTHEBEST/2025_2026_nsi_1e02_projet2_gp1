import csv
from model.jeu import Jeu


class Catalogue:
    def __init__(self, fichier_csv):
        self.jeux = []
        self.charger_csv(fichier_csv)

    def nettoyer_nombre(self, valeur):
        if not valeur:
            return 0
        valeur = "".join(valeur.split())
        return int(valeur)

    def charger_csv(self, fichier_csv):
        with open(fichier_csv, encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader)

            montants = header[4:]  # colonnes des gains

            for ligne in reader:
                nom = ligne[0]
                prix = self.nettoyer_nombre(ligne[1])
                unites = self.nettoyer_nombre(ligne[2])

                gains_dict = {}

                for i, nb_gagnants in enumerate(ligne[4:]):
                    if nb_gagnants:
                        montant = self.nettoyer_nombre(montants[i])
                        gains_dict[montant] = self.nettoyer_nombre(nb_gagnants)

                jeu = Jeu(nom, prix, unites, gains_dict)
                self.jeux.append(jeu)

    def get_jeu(self, nom):
        for jeu in self.jeux:
            if jeu.nom == nom:
                return jeu
        return None
