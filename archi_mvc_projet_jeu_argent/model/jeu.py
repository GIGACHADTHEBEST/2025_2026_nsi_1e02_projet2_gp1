import random


class Jeu:
    def __init__(self, nom, prix, unites, gains):
        """
        gains : dict {montant_gain (int) : nombre_de_tickets (int)}
        """
        self.nom = nom
        self.prix = prix
        self.unites = unites
        self.gains = gains

    def tirage_aleatoire(self):
        """
        Simule un ticket de façon réaliste
        """
        population = []

        for gain, nb in self.gains.items():
            population.extend([gain] * nb)

        tickets_perdants = self.unites - sum(self.gains.values())
        population.extend([0] * tickets_perdants)

        return random.choice(population)

    def proba_gagner(self):
        """
        Probabilité de gagner au moins quelque chose
        """
        return sum(self.gains.values()) / self.unites

    def esperance(self):
        """
        Espérance mathématique du joueur
        """
        gain_total = 0
        for gain, nb in self.gains.items():
            gain_total += gain * nb

        gain_moyen = gain_total / self.unites
        return gain_moyen - self.prix
