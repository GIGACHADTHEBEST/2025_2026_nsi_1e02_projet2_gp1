import tkinter as tk
import os
from controller.accueil_controller import AccueilController
from model.catalogue import Catalogue

def main():
    root = tk.Tk()

    # Trouver le chemin absolu du dossier où est main.py
    dossier_script = os.path.dirname(os.path.abspath(__file__))

    # Construire le chemin complet vers le CSV jeux.csv
    chemin_csv = os.path.join(dossier_script, "data", "jeux.csv")

    print("Chemin CSV absolu :", chemin_csv)
    print("Fichier existe ?", os.path.exists(chemin_csv))

    if not os.path.exists(chemin_csv):
        print(f"Erreur : fichier CSV introuvable à {chemin_csv}")
        return

    catalogue = Catalogue(chemin_csv)

    AccueilController(root, catalogue)
    root.mainloop()


if __name__ == "__main__":
    main()
