import os
import tkinter as tk
from model.catalogue import Catalogue
from controller.accueil_controller import AccueilController

def main():
    root = tk.Tk()

    base_dir = os.path.dirname(__file__)
    chemin_csv = os.path.join(base_dir, "data", "jeux.csv")

    catalogue = Catalogue(chemin_csv)

    app = AccueilController(root, catalogue)

    root.mainloop()

if __name__ == "__main__":
    main()
