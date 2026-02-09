import tkinter as tk
from view.accueil_view import AccueilView

if __name__ == "__main__":
    root = tk.Tk()
    app = AccueilView(root)
    root.mainloop()
