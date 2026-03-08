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
            return

        jeu = self.catalogue.get_jeu(nom_jeu)
        gains = jeu.gains_dict
        perdants = jeu.perdants
        total = jeu.unites

        # --- Nouvelle fenêtre ---
        win = tk.Toplevel(self.view.window)
        win.title("Visualisation avancée")
        win.geometry("900x650")
        win.configure(bg="#1e1e2f")

        # --- Canvas ---
        canvas = tk.Canvas(win, width=850, height=350, bg="#1e1e2f", highlightthickness=0)
        canvas.pack(pady=20)

        # --- Légende ---
        frame_legende = tk.Frame(win, bg="#1e1e2f")
        frame_legende.pack()

        # Couleur unique par montant
        def couleur_depuis_montant(montant):
            random.seed(montant)
            r = random.randint(80, 255)
            g = random.randint(80, 255)
            b = random.randint(80, 255)
            return f"#{r:02x}{g:02x}{b:02x}"

        # --- Construction des catégories ---
        categories = []

        # Gains
        for montant, nb in gains.items():
            proba = nb / total
            couleur = couleur_depuis_montant(montant)
            categories.append((f"{montant} €", nb, proba, couleur))

        # Perdants
        proba_perdants = perdants / total
        categories.append(("Perdants", perdants, proba_perdants, "#cc0000"))


        # --- Normalisation : 1 carré = 1 % ---
        carre_par_pourcent = 1
        taille = 20
        marge = 5
        x, y = 10, 10
        max_ligne = 30

        for label, nb, proba, couleur in categories:
            nb_carres = max(1, int(proba * 100))  # au moins 1 carré

            # Légende
            tk.Label(
                frame_legende,
                text=f"{label} — {nb} tickets — {proba*100:.5f} %",
                bg="#1e1e2f",
                fg=couleur,
                font=("Helvetica", 11)
            ).pack(anchor="w")

            # Carrés
            for _ in range(nb_carres):
                canvas.create_rectangle(
                    x, y, x + taille, y + taille,
                    fill=couleur, outline="#1e1e2f"
                )
                x += taille + marge
                if x > max_ligne * (taille + marge):
                    x = 10
                    y += taille + marge


