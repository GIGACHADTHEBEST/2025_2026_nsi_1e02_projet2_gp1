import tkinter as tk
from model.catalogue import Catalogue
from controller.stats_controller import StatsController


if __name__ == "__main__":
    root = tk.Tk()

    # Chargement des données
    catalogue = Catalogue("data/jeux.csv")

    # Lancement de l'accueil
    AccueilController(root, catalogue)

    root.mainloop()
