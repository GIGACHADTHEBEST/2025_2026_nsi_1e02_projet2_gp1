import tkinter as tk
from model.catalogue import Catalogue
from controller.accueil_controller import AccueilController

if __name__ == "__main__":
    root = tk.Tk()

    # Chargement des données
    catalogue = Catalogue("data/jeux.csv")

    # Lancement de l'accueil
    AccueilController(root, catalogue)

    root.mainloop()
