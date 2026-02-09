class Simulation:
    def __init__(self, jeu):
        self.jeu = jeu

    def lancer(self, n):
        gain_total = 0
        for _ in range(n):
            gain_total += self.jeu.tirage_aleatoire()

        cout_total = n * self.jeu.prix
        return gain_total, cout_total, gain_total - cout_total
