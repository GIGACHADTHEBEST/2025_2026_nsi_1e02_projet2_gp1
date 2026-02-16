import os
import sys
import tkinter as tk
from model.catalogue import Catalogue
from controller.accueil_controller import AccueilController


def main():
    # Création de la fenêtre principale
    root = tk.Tk()

    # Détermination du chemin absolu du fichier CSV
    base_dir = os.path.dirname(os.path.abspath(__file__))
    chemin_csv = os.path.join(base_dir, "data", "jeux.csv")

    # Vérification de l'existence du fichier
    if not os.path.exists(chemin_csv):
        print(f"Erreur : fichier introuvable -> {chemin_csv}")
        sys.exit(1)

    # Initialisation du modèle
    catalogue = Catalogue(chemin_csv)

    # Initialisation du contrôleur
    app = AccueilController(root, catalogue)

    # Lancement de l'application
    root.mainloop()


if __name__ == "__main__":
    main()
    