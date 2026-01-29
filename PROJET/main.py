import tkinter as tk
from PROJET.model import JeuxModel
from PROJET.view import JeuxView
from PROJET.controller import JeuxController


def main():
    root = tk.Tk()

    model = JeuxModel("jeux.csv")
    view = JeuxView(root)
    JeuxController(model, view)

    root.mainloop()


if __name__ == "__main__":
    main()
