from view import StatsView

print("Controller chargé correctement")

class StatsController:
    def __init__(self, root, model):
        self.model = model
        self.view = StatsView(root)

    def ouvrir_stats(self, nom_jeu):
        jeu = self.model.get_jeu(nom_jeu)
        if not jeu:
            print("Jeu introuvable")
            return
        stats = self.model.calculer_stats(jeu)
        self.view.afficher(nom_jeu, jeu, stats)
