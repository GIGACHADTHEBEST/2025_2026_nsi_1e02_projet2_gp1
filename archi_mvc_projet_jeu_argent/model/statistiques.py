class Statistiques:
    def __init__(self, jeu):
        self.jeu = jeu
    

    def resume(self):
        return {
            "prix": self.jeu.prix,
            "proba_gain": self.jeu.proba_gagner(),
            "esperance": self.jeu.esperance(),
            "nb_gagnants": sum(self.jeu.gains_dict.values()),
            "nb_tickets": self.jeu.unites
        }

    def proba_couleurs(self):
        """
        Regroupe les gains par catégories de couleurs
        et renvoie un dict {couleur: probabilité}.
        """

        total_gagnants = sum(self.jeu.gains_dict.values())
        if total_gagnants == 0:
            return {}
        categories = {
            "green": lambda g: g <= 20,
            "orange": lambda g: 20 < g <= 200,
            "red": lambda g: g > 200
        }
        compte = {c: 0 for c in categories}

        for montant, nb in self.jeu.gains_dict.items():
            for couleur, condition in categories.items():
                if condition(montant):
                    compte[couleur] += nb
                    break
                
        return {
            couleur: nb / total_gagnants
            for couleur, nb in compte.items()
            if nb > 0
        }
