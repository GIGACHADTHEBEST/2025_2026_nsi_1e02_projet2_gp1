import tkinter as tk
from projet.model import JeuxModel
from projet.view import JeuxView
from projet.controller import JeuxController


def main():
    root = tk.Tk()

    model = JeuxModel("jeux.csv")
    view = JeuxView(root)
    JeuxController(model, view)

    root.mainloop()


if __name__ == "__main__":
    main()
