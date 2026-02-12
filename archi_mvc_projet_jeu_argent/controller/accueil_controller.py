from view.accueil_view import AccueilView
from controller.jeu_controller import JeuController
from controller.simulation_controller import SimulationController
from controller.stats_controllers import StatsController


class AccueilController:
    def __init__(self, root, catalogue):
        self.root = root
        self.catalogue = catalogue

        self.view = AccueilView(root)

        # Connexion des boutons
        self.view.btn_tester.config(command=self.ouvrir_jeu)
        self.view.btn_simulation.config(command=self.ouvrir_simulation)
        self.view.btn_stats.config(command=self.ouvrir_stats)

    def ouvrir_jeu(self):
        JeuController(self.root, self.catalogue)

    def ouvrir_simulation(self):
        SimulationController(self.root, self.catalogue)

    def ouvrir_stats(self):
        StatsController(self.root, self.catalogue)


