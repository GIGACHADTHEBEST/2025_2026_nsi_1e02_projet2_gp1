import tkinter as tk
from tkinter import ttk


class SimulationView:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title("Simulation")
        self.window.geometry("550x400")

        ttk.Label(
            self.window,
            text="Simulation à grande échelle",
            font=("Helvetica", 16, "bold")
        ).pack(pady=20)

        ttk.Label(self.window, text="Jeu :").pack()
        self.combo_jeu = ttk.Combobox(self.window, state="readonly", width=30)
        self.combo_jeu.pack(pady=5)

        ttk.Label(self.window, text="Nombre de tickets :").pack()
        self.entry_nb = ttk.Entry(self.window, width=15)
        self.entry_nb.pack(pady=5)

        self.btn_lancer = ttk.Button(self.window, text="🔁 Lancer la simulation")
        self.btn_lancer.pack(pady=15)

        self.label_resultats = ttk.Label(self.window, text="", justify="left")
        self.label_resultats.pack(pady=20)
