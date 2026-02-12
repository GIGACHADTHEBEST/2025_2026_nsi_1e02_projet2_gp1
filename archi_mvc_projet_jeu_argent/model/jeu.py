import random

class Jeu:
    def __init__(self, nom, prix, unites, gains_dict):
        self.nom = nom
        self.prix = prix
        self.unites = unites
        self.gains_dict = gains_dict  # {montant_gain: nombre_de_tickets}

        # Calcul des tickets perdants
        total_gagnants = sum(gains_dict.values())
        self.perdants = unites - total_gagnants

    def tirage_aleatoire(self):
        gains = []
        poids = []

        # Gains positifs
        for montant, nb in self.gains_dict.items():
            gains.append(int(montant))
            poids.append(int(nb))

        # Ajouter les tickets perdants
        gains.append(0)
        poids.append(self.perdants)

        return random.choices(gains, weights=poids, k=1)[0]
