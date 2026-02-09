import tkinter as tk
from tkinter import ttk


class StatsView:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Statistiques")
        self.window.geometry("500x350")

        ttk.Label(
            self.window,
            text="Statistiques du jeu",
            font=("Helvetica", 16, "bold")
        ).pack(pady=20)

        ttk.Label(self.window, text="Jeu :").pack()
        self.combo_jeu = ttk.Combobox(self.window, state="readonly", width=30)
        self.combo_jeu.pack(pady=10)

        self.btn_calculer = ttk.Button(self.window, text="📊 Calculer")
        self.btn_calculer.pack(pady=15)

        self.label_stats = ttk.Label(self.window, text="", justify="left")
        self.label_stats.pack(pady=20)
