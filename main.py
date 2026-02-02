import tkinter as tk
from projet.model import Model
from projet.view import View
from projet.controller import Controller

def main():
    root = tk.Tk()
    model = Model("jeux.csv")
    view = View(root)
    Controller(model, view)

    root.mainloop()


if __name__ == "__main__":
    main()
