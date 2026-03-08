from view.stats_view import StatsView
from model.statistiques import Statistiques
import tkinter as tk
import random

class StatsController:
    def __init__(self, root, catalogue):
        self.catalogue = catalogue
        self.view = StatsView(root)

        # Remplir le combo
        self.view.combo_jeu["values"] = [jeu.nom for jeu in catalogue.jeux]

        # Boutons
        self.view.btn_calculer.config(command=self.afficher_stats)
        self.view.btn_visualiser.config(command=self.visualiser_couleurs)

        # Canvas pour la visualisation
        self.canvas = tk.Canvas(self.view.main_frame, width=500, height=150, bg="#1e1e2f", highlightthickness=0)
        self.canvas.pack(pady=20)


    def afficher_stats(self):
        nom_jeu = self.view.combo_jeu.get()
        if not nom_jeu:
            return

        jeu = self.catalogue.get_jeu(nom_jeu)
        stats = Statistiques(jeu)

        self.view.label_stats.config(
            text=(
                f"Prix du ticket : {stats.resume()['prix']} €\n"
                f"Probabilité de gain : {stats.resume()['proba_gain']*100:.2f} %\n"
                f"Espérance mathématique : {stats.resume()['esperance']:.2f} €\n\n"
                f"(Une espérance négative = perte moyenne)"
            )
        )

    def visualiser_couleurs(self):
        nom_jeu = self.view.combo_jeu.get()
        if not nom_jeu:
            print("Aucun jeu sélectionné")
            return

        jeu = self.catalogue.get_jeu(nom_jeu)
        stats = Statistiques(jeu)

        # Récupération des données
        gains = jeu.gains_dict
        total = sum(gains.values())

        if total == 0:
            print("Aucun gain disponible")
            return

        # --- Nouvelle fenêtre ---
        win = tk.Toplevel(self.view.window)
        win.title("Visualisation avancée")
        win.geometry("900x600")
        win.configure(bg="#1e1e2f")

        # --- Canvas pour les carrés ---
        canvas = tk.Canvas(win, width=850, height=350, bg="#1e1e2f", highlightthickness=0)
        canvas.pack(pady=20)

        # --- Légende ---
        frame_legende = tk.Frame(win, bg="#1e1e2f")
        frame_legende.pack()

        # Génération d'une couleur unique par montant
        def couleur_depuis_montant(montant):
            random.seed(montant)
            r = random.randint(50, 255)
            g = random.randint(50, 255)
            b = random.randint(50, 255)
            return f"#{r:02x}{g:02x}{b:02x}"

        # --- Dessin des carrés ---
        taille = 20
        marge = 5
        x, y = 10, 10
        max_ligne = 40  # nombre de carrés par ligne

        for montant, nb in gains.items():
            couleur = couleur_depuis_montant(montant)

            # Légende
            proba = nb / total * 100
            tk.Label(
                frame_legende,
                text=f"{montant} € — {nb} tickets — {proba:.2f} %",
                bg="#1e1e2f",
                fg=couleur,
                font=("Helvetica", 11)
            ).pack(anchor="w")

            # Dessin des carrés
            for _ in range(min(nb, 300)):  # limite pour éviter 100k carrés
                canvas.create_rectangle(
                    x, y, x + taille, y + taille,
                    fill=couleur, outline="#1e1e2f"
                )
                x += taille + marge
                if x > max_ligne * (taille + marge):
                    x = 10
                    y += taille + marge


