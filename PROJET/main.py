import tkinter as tk
from model import JeuxModel
from view import JeuxView
from controller import JeuxController


def main():
    root = tk.Tk()

    model = JeuxModel("jeux.csv")
    view = JeuxView(root)
    JeuxController(model, view)

    root.mainloop()


if __name__ == "__main__":
    main()
