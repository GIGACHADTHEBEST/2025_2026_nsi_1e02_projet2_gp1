import tkinter as tk
from tkinter import ttk


class JeuView:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Tester un jeu")
        self.window.geometry("600x500")
        self.window.resizable(False, False)
        self.window.configure(bg="#1e1e2f")

        # ===== STYLE =====
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Titre.TLabel",
                        background="#1e1e2f",
                        foreground="white",
                        font=("Helvetica", 18, "bold"),
                        anchor="center")

        style.configure("Subtitle.TLabel",
                        background="#1e1e2f",
                        foreground="#cfcfe0",
                        font=("Helvetica", 11),
                        anchor="center")

        style.configure("Menu.TButton",
                        font=("Helvetica", 12, "bold"),
                        padding=10)

        style.configure("Retour.TButton",
                        font=("Helvetica", 10),
                        padding=6)

        style.configure("Custom.TCombobox",
                        fieldbackground="white",
                        padding=5)

        # ===== FRAME PRINCIPAL =====
        self.main_frame = tk.Frame(self.window, bg="#1e1e2f")
        self.main_frame.pack(expand=True)

        # ===== TITRE =====
        self.label_titre = ttk.Label(
            self.main_frame,
            text="Tester un jeu",
            style="Titre.TLabel"
        )
        self.label_titre.pack(pady=(40, 10))

        # ===== SOUS-TITRE =====
        self.label_sous_titre = ttk.Label(
            self.main_frame,
            text="Choisissez un jeu et tentez votre chance",
            style="Subtitle.TLabel"
        )
        self.label_sous_titre.pack(pady=(0, 20))

        # ===== TEXTE INTRODUCTIF SUR LES DANGERS =====
        self.label_intro = ttk.Label(
            self.main_frame,
            text=(
                "Sous leur apparence anodine et ludique, les jeux à gratter déploient une "
                "mécanique subtile où l’espérance de gain, rigoureusement calculée, demeure "
                "structurellement défavorable au joueur. L’illusion d’un enrichissement instantané, "
                "entretenue par la rareté savamment mise en scène des gains, peut progressivement "
                "engendrer une dépendance insidieuse et des déséquilibres financiers durables."
            ),
            style="Subtitle.TLabel",
            wraplength=550,
            justify="left"
        )
        self.label_intro.pack(pady=(0, 30))

        # ===== FRAME CONTENU =====
        self.frame_contenu = tk.Frame(self.main_frame, bg="#1e1e2f")
        self.frame_contenu.pack()

        # Label choix jeu
        self.label_choix = ttk.Label(
            self.frame_contenu,
            text="Choisissez un jeu :",
            style="Subtitle.TLabel"
        )
        self.label_choix.pack(pady=(0, 5))

        # Combobox
        self.combo_jeu = ttk.Combobox(
            self.frame_contenu,
            state="readonly",
            width=30,
            style="Custom.TCombobox"
        )
        self.combo_jeu.pack(pady=10)

        # Bouton jouer
        self.btn_jouer = ttk.Button(
            self.frame_contenu,
            text="Gratter un ticket",
            width=25,
            style="Menu.TButton"
        )
        self.btn_jouer.pack(pady=20)

        # Résultat
        self.label_resultat = ttk.Label(
            self.frame_contenu,
            text="",
            style="Subtitle.TLabel"
        )
        self.label_resultat.pack(pady=15)

        # ===== BOUTON RETOUR =====
        self.btn_retour = ttk.Button(
            self.main_frame,
            text="Retourner au menu",
            style="Retour.TButton",
            command=self.window.destroy
        )
        self.btn_retour.pack(pady=(10, 20))


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    app = JeuView(root)
    root.mainloop()
