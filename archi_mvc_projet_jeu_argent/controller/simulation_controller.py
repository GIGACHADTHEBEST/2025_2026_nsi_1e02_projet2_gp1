from view.simulation_view import SimulationView


class SimulationController:
    def __init__(self, root, catalogue):
        self.catalogue = catalogue
        self.view = SimulationView(root)

        self.view.combo_jeu["values"] = [jeu.nom for jeu in catalogue.jeux]
        self.view.btn_lancer.config(command=self.lancer_simulation)

    def lancer_simulation(self):
        nom_jeu = self.view.combo_jeu.get()
        if not nom_jeu:
            return

        try:
            n = int(self.view.entry_nb.get())
        except ValueError:
            return

        jeu = self.catalogue.get_jeu(nom_jeu)

        gain_total = 0
        for _ in range(n):
            gain_total += jeu.tirage_aleatoire()

        cout_total = n * jeu.prix
        bilan = gain_total - cout_total

        self.view.label_resultats.config(
            text=(
                f"Tickets joués : {n}\n"
                f"Coût total : {cout_total} €\n"
                f"Gains totaux : {gain_total} €\n\n"
                f"Bilan : {bilan} €"
