class Statistiques:
    def __init__(self, jeu):
        self.jeu = jeu

    def resume(self):
        return {
            "prix": self.jeu.prix,
            "proba_gain": self.jeu.proba_gagner(),
            "esperance": self.jeu.esperance(),
            "nb_gagnants": sum(self.jeu.gains.values()),
            "nb_tickets": self.jeu.unites
        }
