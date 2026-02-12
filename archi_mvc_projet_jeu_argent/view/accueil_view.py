import tkinter as tk
from tkinter import ttk


class AccueilView:
    def __init__(self, root):
        self.root = root
        self.root.title("Les jeux d'argent")
        self.root.geometry("700x400")
        self.root.resizable(False, False)

        # ===== TITRE =====
        self.label_titre = ttk.Label(
            root,
            text="Les jeux d'argent :\nquelles sont vraiment vos chances de gagner ?",
            font=("Helvetica", 18, "bold"),
            justify="center"
        )
        self.label_titre.pack(pady=30)

        # ===== FRAME BOUTONS =====
        self.frame_boutons = ttk.Frame(root)
        self.frame_boutons.pack(pady=40)

        # Bouton tester un jeu
        self.btn_tester = ttk.Button(
            self.frame_boutons,
            text=" Tester un jeu",
            width=25
        )
        self.btn_tester.grid(row=0, column=0, padx=15, pady=10)

        # Bouton simulation
        self.btn_simulation = ttk.Button(
            self.frame_boutons,
            text=" Lancer une simulation",
            width=25
        )
        self.btn_simulation.grid(row=1, column=0, padx=15, pady=10)

        # Bouton statistiques
        self.btn_stats = ttk.Button(
            self.frame_boutons,
            text=" Voir les statistiques",
            width=25
        )
        self.btn_stats.grid(row=2, column=0, padx=15, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = AccueilView(root)
    root.mainloop()
