import tkinter as tk
from tkinter import ttk


class JeuView:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Tester un jeu")
        self.window.geometry("500x350")
        self.window.configure(bg="#dbeafe")  # Nouvelle couleur de fond (bleu clair)

        # Style ttk
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Titre.TLabel",
            background="#dbeafe",
            foreground="#1e3a8a",
            font=("Segoe UI", 18, "bold")
        )

        style.configure(
            "Custom.TLabel",
            background="#dbeafe",
            font=("Segoe UI", 11)
        )

        style.configure(
            "Custom.TButton",
            font=("Segoe UI", 11, "bold"),
            padding=6,
            background="#2563eb",
            foreground="white"
        )

        style.map(
            "Custom.TButton",
            background=[("active", "#1e40af")]
        )

        # Titre
        ttk.Label(
            self.window,
            text="Tester un jeu",
            style="Titre.TLabel"
        ).pack(pady=20)

        # Choix du jeu
        ttk.Label(
            self.window,
            text="Choisissez un jeu :",
            style="Custom.TLabel"
        ).pack()

        self.combo_jeu = ttk.Combobox(
            self.window,
            state="readonly",
            width=30,
            font=("Segoe UI", 10)
        )
        self.combo_jeu.pack(pady=10)

        # Bouton jouer
        self.btn_jouer = ttk.Button(
            self.window,
            text="Gratter un ticket",
            style="Custom.TButton"
        )
        self.btn_jouer.pack(pady=15)

        # Résultat
        self.label_resultat = ttk.Label(
            self.window,
            text="",
            font=("Segoe UI", 12, "bold"),
            foreground="#065f46",
            background="#dbeafe"
        )
        self.label_resultat.pack(pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    app = JeuView(root)
    root.mainloop()
