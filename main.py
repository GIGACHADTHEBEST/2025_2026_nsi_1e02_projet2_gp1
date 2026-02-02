import tkinter as tk
from PROJET.model import Model
from PROJET.view import View
from PROJET.controller import Controller

def main():
    root = tk.Tk()
    model = Model("jeux.csv")
    view = View(root)
    Controller(model, view)

    root.mainloop()


if __name__ == "__main__":
    main()
