import tkinter as tk
from archi_mvc_projet_jeu_argent.model.catalogue import Catalogue
from archi_mvc_projet_jeu_argent.controller.accueil_controller import AccueilController



def main():
    root = tk.Tk()

    catalogue = Catalogue("data/jeux.csv")
    AccueilController(root, catalogue)

    root.mainloop()


if __name__ == "__main__":
    main()
