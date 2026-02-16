from view.stats_view import StatsView
from model.statistiques import Statistiques
import tkinter as tk

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

        probabilites = stats.proba_couleurs()
        if not probabilites:
            print("Aucune probabilité disponible")
            return

        self.canvas.delete("all")

        x = 10
        y = 10
        hauteur = 100
        largeur_totale = 480

        for couleur, prob in probabilites.items():
            largeur = prob * largeur_totale
            self.canvas.create_rectangle(x, y, x + largeur, y + hauteur, fill=couleur, outline="white")
            x += largeur

