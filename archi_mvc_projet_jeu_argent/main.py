import tkinter as tk
import os

from controller.accueil_controller import AccueilController
from model.catalogue import Catalogue



def main():
    root = tk.Tk()

    catalogue = Catalogue("data/jeux.csv")
    AccueilController(root, catalogue)

    root.mainloop()


if __name__ == "__main__":
    main()
