import random

class Jeu:
    def __init__(self, nom, prix, unites, gains_dict):
        self.nom = nom
        self.prix = prix
        self.unites = unites
        self.gains_dict = gains_dict
        total_gagnants = sum(gains_dict.values())
        self.perdants = unites - total_gagnants
    def proba_gagner(self):
        total_gagnants = sum(self.gains_dict.values())
        return total_gagnants / self.unites

    def esperance(self):
        esperance = 0
        for montant, nb in self.gains_dict.items():
            proba = nb / self.unites
            esperance += montant * proba
        return esperance - self.prix


    def tirage_aleatoire(self):
        gains = []
        poids = []
        for montant, nb in self.gains_dict.items():
            gains.append(int(montant))
            poids.append(int(nb))
        gains.append(0)
        poids.append(self.perdants)

        return random.choices(gains, weights=poids, k=1)[0]
