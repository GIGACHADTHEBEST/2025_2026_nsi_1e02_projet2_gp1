import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class View:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeux à gratter")
        self.root.geometry("900x700")

        self.prix_var = tk.StringVar(value="Tous")
        self.jeu_var = tk.StringVar()

        self._creer_filtres()
        self._creer_graphique()
        self._creer_stats()
        self._creer_boutons()

    def _creer_filtres(self):
        frame = ttk.Frame(self.root)
        frame.pack(pady=10)

        ttk.Label(frame, text="Prix (€)").grid(row=0, column=0)
        self.prix_menu = ttk.Combobox(
            frame, textvariable=self.prix_var, state="readonly"
        )
        self.prix_menu.grid(row=0, column=1)

        ttk.Label(frame, text="Jeu").grid(row=0, column=2)
        self.jeu_menu = ttk.Combobox(
            frame, textvariable=self.jeu_var, state="readonly"
        )
        self.jeu_menu.grid(row=0, column=3)

    def _creer_graphique(self):
        self.fig, self.ax = plt.subplots(figsize=(8, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, self.root)
        self.canvas.get_tk_widget().pack()

    def _creer_stats(self):
        self.stats_label = ttk.Label(self.root, text="", justify="left")
        self.stats_label.pack(pady=10)

    def _creer_boutons(self):
        frame = ttk.Frame(self.root)
        frame.pack(pady=10)

        self.btn_update = ttk.Button(frame, text="Actualiser")
        self.btn_update.grid(row=0, column=0, padx=5)

        ttk.Button(
            frame, text="Quitter", command=self.root.destroy
        ).grid(row=0, column=1, padx=5)
