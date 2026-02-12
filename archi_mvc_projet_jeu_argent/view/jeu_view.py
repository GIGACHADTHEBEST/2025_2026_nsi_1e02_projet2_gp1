import tkinter as tk
from tkinter import ttk


class JeuView:
    def __init__(self, root):
        
        self.root = root
        self.root.title("Tester un jeu")
        self.root.geometry("500x350")
        self.root.resizable(False, False)
        self.root.configure(bg="#ffce84")

        ttk.Label(
            self.root,
            text="Tester un jeu",
            font=("Helvetica", 16, "bold")
        ).pack(pady=20)

        # Choix du jeu
        ttk.Label(self.root, text="Choisissez un jeu :").pack()
        self.combo_jeu = ttk.Combobox(self.root, state="readonly", width=30)
        self.combo_jeu.pack(pady=10)

        # Bouton jouer
        self.btn_jouer = ttk.Button(self.root, text="🎟 Gratter un ticket")
        self.btn_jouer.pack(pady=15)

        # Résultat
        self.label_resultat = ttk.Label(
            self.root,
            text="",
            font=("Helvetica", 12)
        )
        self.label_resultat.pack(pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # cache la fenêtre principale (optionnel)
    app = JeuView(root)
    root.mainloop()
