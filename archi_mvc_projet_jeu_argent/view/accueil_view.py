import tkinter as tk
from tkinter import ttk


class AccueilView:
    def __init__(self, root):
        self.root = root
        self.root.title("Les jeux d'argent")
        self.root.geometry("750x450")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2f")

        # ===== STYLE =====
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Titre.TLabel",
                        background="#1e1e2f",
                        foreground="white",
                        font=("Helvetica", 20, "bold"),
                        anchor="center")

        style.configure("Subtitle.TLabel",
                        background="#1e1e2f",
                        foreground="#cfcfe0",
                        font=("Helvetica", 11),
                        anchor="center")

        style.configure("Menu.TButton",
                        font=("Helvetica", 12, "bold"),
                        padding=10)

        
        # ===== FRAME PRINCIPAL =====
        self.main_frame = tk.Frame(root, bg="#1e1e2f")
        self.main_frame.pack(expand=True)

        # ===== TITRE =====
        self.label_titre = ttk.Label(
            self.main_frame,
            text="Les jeux d'argent",
            style="Titre.TLabel"
        )
        self.label_titre.pack(pady=(40, 10))

        # ===== SOUS-TITRE =====
        self.label_sous_titre = ttk.Label(
            self.main_frame,
            text="Quelles sont vraiment vos chances de gagner ?",
            style="Subtitle.TLabel"
        )
        self.label_sous_titre.pack(pady=(0, 40))

        # ===== FRAME BOUTONS =====
        self.frame_boutons = tk.Frame(self.main_frame, bg="#1e1e2f")
        self.frame_boutons.pack()

        # Bouton tester un jeu
        self.btn_tester = ttk.Button(
            self.frame_boutons,
            text="  Tester un jeu",
            width=30,
            style="Menu.TButton"
        )
        self.btn_tester.grid(row=0, column=0, padx=15, pady=12)

        # Bouton simulation
        self.btn_simulation = ttk.Button(
            self.frame_boutons,
            text="  Lancer une simulation",
            width=30,
            style="Menu.TButton"
        )
        self.btn_simulation.grid(row=1, column=0, padx=15, pady=12)

        # Bouton statistiques
        self.btn_stats = ttk.Button(
            self.frame_boutons,
            text="  Voir les statistiques",
            width=30,
            style="Menu.TButton"
        )
        self.btn_stats.grid(row=2, column=0, padx=15, pady=12)


if __name__ == "__main__":
    root = tk.Tk()
    app = AccueilView(root)
    root.mainloop()

