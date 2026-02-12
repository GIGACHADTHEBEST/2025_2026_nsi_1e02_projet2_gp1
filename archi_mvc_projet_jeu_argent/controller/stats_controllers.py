from view.stats_view import StatsView


class StatsController:
    def __init__(self, root, catalogue):
        self.catalogue = catalogue
        self.view = StatsView(root)

        self.view.combo_jeu["values"] = [jeu.nom for jeu in catalogue.jeux]
        self.view.btn_calculer.config(command=self.afficher_stats)

    def afficher_stats(self):
        nom_jeu = self.view.combo_jeu.get()
        if not nom_jeu:
            return

        jeu = self.catalogue.get_jeu(nom_jeu)

        esperance = jeu.esperance()
        proba = jeu.proba_gagner() * 100

        self.view.label_stats.config(
            text=(
                f"Prix du ticket : {jeu.prix} €\n"
                f"Probabilité de gain : {proba:.2f} %\n"
                f"Espérance mathématique : {esperance:.2f} €\n\n"
                f"(Une espérance négative = perte moyenne)"
            )
        )
    