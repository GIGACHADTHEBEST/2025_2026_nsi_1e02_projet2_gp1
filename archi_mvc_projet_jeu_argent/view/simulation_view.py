import tkinter as tk
from tkinter import ttk


class SimulationView:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Simulation")
        self.window.geometry("650x750")
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

        style.configure("Custom.TEntry",
                        padding=5)

        # ===== FRAME PRINCIPAL =====
        self.main_frame = tk.Frame(self.window, bg="#1e1e2f")
        self.main_frame.pack(expand=True)

        # ===== TITRE =====
        self.label_titre = ttk.Label(
            self.main_frame,
            text="Simulation à grande échelle",
            style="Titre.TLabel"
        )
        self.label_titre.pack(pady=(40, 10))

        # ===== SOUS-TITRE =====
        self.label_sous_titre = ttk.Label(
            self.main_frame,
            text="Analysez vos gains et pertes sur un grand nombre de tickets",
            style="Subtitle.TLabel"
        )
        self.label_sous_titre.pack(pady=(0, 30))

        # ===== FRAME CONTENU =====
        self.frame_contenu = tk.Frame(self.main_frame, bg="#1e1e2f")
        self.frame_contenu.pack()

        # ---- Choix du jeu ----
        self.label_jeu = ttk.Label(
            self.frame_contenu,
            text="Jeu :",
            style="Subtitle.TLabel"
        )
        self.label_jeu.pack(pady=(0, 5))

        self.combo_jeu = ttk.Combobox(
            self.frame_contenu,
            state="readonly",
            width=30,
            style="Custom.TCombobox"
        )
        self.combo_jeu.pack(pady=10)

        # ---- Nombre de tickets ----
        self.label_nb = ttk.Label(
            self.frame_contenu,
            text="Nombre de tickets :",
            style="Subtitle.TLabel"
        )
        self.label_nb.pack(pady=(10, 5))

        self.entry_nb = ttk.Entry(
            self.frame_contenu,
            width=20,
            style="Custom.TEntry"
        )
        self.entry_nb.pack(pady=10)

        # ---- Bouton lancer ----
        self.btn_lancer = ttk.Button(
            self.frame_contenu,
            text=" Lancer la simulation",
            width=30,
            style="Menu.TButton"
        )
        self.btn_lancer.pack(pady=20)

        # ---- Résultats ----
        self.label_resultats = ttk.Label(
            self.frame_contenu,
            text="",
            style="Subtitle.TLabel",
            justify="center"
        )
        self.label_resultats.pack(pady=15)

        # ===== BOUTON RETOUR =====
        self.btn_retour = ttk.Button(
            self.main_frame,
            text="⬅ Retourner au menu",
            style="Retour.TButton",
            command=self.window.destroy
        )
        self.btn_retour.pack(pady=(10, 20))


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    app = SimulationView(root)
    root.mainloop()
