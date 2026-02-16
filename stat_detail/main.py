import tkinter as tk

# ==============================
# CONFIG VISUELLE
# ==============================
COULEURS = ["#e6194B", "#3cb44b", "#ffe119", "#4363d8",
            "#f58231", "#911eb4", "#46f0f0", "#f032e6",
            "#bcf60c", "#fabebe", "#008080", "#e6beff"]
TAILLE = 6
MARGE = 2
PAR_LIGNE = 100
CARRE_PAR_TICKETS = 10000

# injecter dans view
import view
view.COULEURS = COULEURS
view.TAILLE = TAILLE
view.MARGE = MARGE
view.PAR_LIGNE = PAR_LIGNE
view.CARRE_PAR_TICKETS = CARRE_PAR_TICKETS

# imports après injection
from model import JeuModel
from my_controller import StatsController

# ==============================
# APPLICATION
# ==============================
def main():
    root = tk.Tk()
    root.title("Menu principal")
    root.geometry("500x400")

    model = JeuModel("jeux.csv")
    controller = StatsController(root, model)

    tk.Label(root, text="Choisissez un jeu", font=("Arial", 16, "bold")).pack(pady=20)

    for nom_jeu in model.jeux.keys():
        tk.Button(root, text=nom_jeu, width=30,
                  command=lambda n=nom_jeu: controller.ouvrir_stats(n)).pack(pady=3)

    root.mainloop()


if __name__ == "__main__":
    main()
