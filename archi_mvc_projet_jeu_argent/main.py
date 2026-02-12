import tkinter as tk
from model.catalogue import Catalogue
from controller.accueil_controller import AccueilController

def main():
    root = tk.Tk()

    catalogue = Catalogue("data/jeux.csv")

    app = AccueilController(root, catalogue)

    root.mainloop()

if __name__ == "__main__":
    main()
