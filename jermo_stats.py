import tkinter as tk
from math import ceil

# ===== JEU (PARAMÈTRE UNIQUE) =====
jeu = {
    "nom": "Banco",
    "prix": 1,
    "tickets": 6_000_000,
    "gains": {
        0: 5_293_992,
        1: 591_496,
        2: 706_008,
        5: 150_000,
        10: 120_000,
        80: 80,
        1_000: 3
    }
}

CARRE_PAR_TICKETS = 10_000
TAILLE = 18
MARGE = 4
PAR_LIGNE = 35

# Couleurs uniques par gain
COULEURS = [
    "#4e79a7", "#f28e2b", "#e15759", "#76b7b2",
    "#59a14f", "#edc949", "#af7aa1", "#ff9da7",
    "#9c755f", "#bab0ab"
]

# ===== FENÊTRE =====
root = tk.Tk()
root.title(f"Répartition réelle – {jeu['nom']}")
root.geometry("1200x650")

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill="both", expand=True)

# ===== TITRE =====
canvas.create_text(
    600, 30,
    text=f"{jeu['nom']} – répartition réelle des issues",
    font=("Arial", 16, "bold")
)

# ===== DESSIN DES CARRÉS =====
x0, y0 = 20, 80
index = 0
stats_y = 100
couleur_index = 0

canvas.create_text(
    850, 80,
    text="Statistiques détaillées",
    font=("Arial", 14, "bold"),
    anchor="w"
)

for gain, nb_tickets in sorted(jeu["gains"].items()):
    couleur = COULEURS[couleur_index % len(COULEURS)]
    couleur_index += 1

    nb_carres = ceil(nb_tickets / CARRE_PAR_TICKETS)
    proba = nb_tickets / jeu["tickets"] * 100
    gain_total = gain * nb_tickets

    # Dessin des carrés
    for _ in range(nb_carres):
        cx = x0 + (index % PAR_LIGNE) * (TAILLE + MARGE)
        cy = y0 + (index // PAR_LIGNE) * (TAILLE + MARGE)

        canvas.create_rectangle(
            cx, cy,
            cx + TAILLE,
            cy + TAILLE,
            fill=couleur,
            outline=""
        )
        index += 1

    # Bloc stats à droite
    canvas.create_rectangle(
        820, stats_y - 10,
        840, stats_y + 10,
        fill=couleur,
        outline=""
    )

    canvas.create_text(
        850, stats_y,
        text=(
            f"Gain {gain} €\n"
            f"{nb_tickets:,} tickets  •  {proba:.4f} %\n"
            f"Gains totaux : {gain_total:,} €"
        ).replace(",", " "),
        anchor="w",
        font=("Arial", 10)
    )

    stats_y += 60

# ===== RÉSUMÉ GLOBAL (DISCRET) =====
mises = jeu["prix"] * jeu["tickets"]
gains_totaux = sum(g * n for g, n in jeu["gains"].items())
perte_moyenne = (mises - gains_totaux) / jeu["tickets"]

canvas.create_text(
    850, stats_y + 20,
    text=(
        f"Mise totale : {mises:,} €\n"
        f"Gains redistribués : {gains_totaux:,} €\n"
        f"Perte moyenne par ticket : {perte_moyenne:.2f} €"
    ).replace(",", " "),
    anchor="w",
    font=("Arial", 11, "bold"),
    fill="darkred"
)

root.mainloop()
 