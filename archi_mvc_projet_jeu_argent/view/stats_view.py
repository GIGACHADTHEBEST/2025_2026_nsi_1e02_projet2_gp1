import tkinter as tk
from tkinter import ttk


class StatsView:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Statistiques")
        self.window.geometry("750x450")
        self.window.resizable(False, False)
        self.window.configure(bg="#1e1e2f")

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

        style.configure("Dark.TLabel",
                        background="#1e1e2f",
                        foreground="white",
                        font=("Helvetica", 11))

        # ===== FRAME PRINCIPAL =====
        self.main_frame = tk.Frame(self.window, bg="#1e1e2f")
        self.main_frame.pack(expand=True)

        # ===== TITRE =====
        self.label_titre = ttk.Label(
            self.main_frame,
            text="Statistiques du jeu",
            style="Titre.TLabel"
        )
        self.label_titre.pack(pady=(40, 20))

        # ===== CHOIX JEU =====
        ttk.Label(
            self.main_frame,
            text="Jeu :",
            style="Dark.TLabel"
        ).pack()

        self.combo_jeu = ttk.Combobox(
            self.main_frame,
            state="readonly",
            width=30,
            font=("Helvetica", 11)
        )
        self.combo_jeu.pack(pady=10)

        # ===== BOUTON CALCULER =====
        self.btn_calculer = ttk.Button(
            self.main_frame,
            text="Calculer",
            width=30,
            style="Menu.TButton"
        )
        self.btn_calculer.pack(pady=15)

        # ===== RESULTATS =====
        self.label_stats = ttk.Label(
            self.main_frame,
            text="",
            style="Dark.TLabel",
            justify="left"
        )
        self.label_stats.pack(pady=20)

        # ===== BOUTON VISUALISATION =====
        self.btn_visualiser = ttk.Button(
            self.main_frame,
            text="Visualisation avancée",
            width=30,
            style="Menu.TButton"
        )
        self.btn_visualiser.pack(pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    app = StatsView(root)
    root.mainloop()
