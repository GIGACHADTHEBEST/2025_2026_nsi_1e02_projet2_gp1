import tkinter as tk
from tkinter import ttk


class JeuView:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Tester un jeu")
        self.window.geometry("500x350")

        ttk.Label(
            self.window,
            text="Tester un jeu",
            font=("Helvetica", 16, "bold")
        ).pack(pady=20)

        # Choix du jeu
        ttk.Label(self.window, text="Choisissez un jeu :").pack()
        self.combo_jeu = ttk.Combobox(self.window, state="readonly", width=30)
        self.combo_jeu.pack(pady=10)

        # Bouton jouer
        self.btn_jouer = ttk.Button(self.window, text="🎟 Gratter un ticket")
        self.btn_jouer.pack(pady=15)

        # Résultat
        self.label_resultat = ttk.Label(
            self.window,
            text="",
            font=("Helvetica", 12)
        )
        self.label_resultat.pack(pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # cache la fenêtre principale (optionnel)
    app = JeuView(root)
    root.mainloop()

