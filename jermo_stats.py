import csv
import tkinter as tk
from math import ceil

# ================== IMPORT CSV ==================

def nettoyer_nombre(texte):
    return int(
        texte
        .replace(" ", "")
        .replace("\u202f", "")  # espace insécable fine
        .replace("\xa0", "")    # espace insécable classique
    )

def charger_jeux_depuis_csv(fichier):
    jeux = {}

    with open(fichier, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            nom = row["jeu"]
            prix = float(row["prix"])
            tickets = nettoyer_nombre(row["unites"])

            gains = {}
            total_gagnants = 0

            for col, val in row.items():
                if col.isdigit() and val.strip():
                    nb = nettoyer_nombre(val)
                    gain = int(col)
                    gains[gain] = nb
                    total_gagnants += nb

            gains[0] = tickets - total_gagnants

            jeux[nom] = {
                "prix": prix,
                "tickets": tickets,
                "gains": gains
            }

    return jeux


JEUX = charger_jeux_depuis_csv("archi_mvc_projet_jeu_argent/data/jeux.csv")


# ================= PARAMÈTRES VISUELS =================

CARRE_PAR_TICKETS = 10_000
TAILLE = 18
MARGE = 4
PAR_LIGNE = 35

COULEURS = [
    "#4e79a7", "#f28e2b", "#e15759", "#76b7b2",
    "#59a14f", "#edc949", "#af7aa1", "#ff9da7",
    "#9c755f", "#bab0ab", "#1f77b4", "#ff7f0e"
]

# ================= FENÊTRE STATS =================

def fenetre_stats(nom_jeu, jeu):
    stats = tk.Toplevel()
    stats.title(f"Statistiques – {nom_jeu}")
    stats.geometry("1200x650")

    canvas = tk.Canvas(stats, bg="white")
    canvas.pack(fill="both", expand=True)

    canvas.create_text(
        600, 30,
        text=f"{nom_jeu} – répartition réelle des issues",
        font=("Arial", 16, "bold")
    )

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
                f"{nb_tickets:,} tickets • {proba:.4f} %\n"
                f"Gains totaux : {gain_total:,} €"
            ).replace(",", " "),
            anchor="w",
            font=("Arial", 10)
        )

        stats_y += 60

    mises = jeu["prix"] * jeu["tickets"]
    gains_totaux = sum(g * n for g, n in jeu["gains"].items())
    perte_moyenne = (mises - gains_totaux) / jeu["tickets"]

    canvas.create_text(
        850, stats_y + 20,
        text=(
            f"Prix du ticket : {jeu['prix']} €\n"
            f"Mise totale : {mises:,} €\n"
            f"Gains redistribués : {gains_totaux:,} €\n"
            f"Perte moyenne par ticket : {perte_moyenne:.2f} €"
        ).replace(",", " "),
        anchor="w",
        font=("Arial", 11, "bold"),
        fill="darkred"
    )

# ================= FENÊTRE DE SÉLECTION =================

def ouvrir_stats():
    nom = selection.get()
    if nom:
        fenetre_stats(nom, JEUX[nom])

root = tk.Tk()
root.title("Choisir un jeu")
root.geometry("420x300")

tk.Label(
    root,
    text="Choisis un jeu\n(importé depuis le CSV)",
    font=("Arial", 14, "bold"),
    justify="center"
).pack(pady=20)

selection = tk.StringVar()
menu = tk.OptionMenu(root, selection, *JEUX.keys())
menu.config(width=30, font=("Arial", 11))
menu.pack(pady=10)

tk.Button(
    root,
    text="Afficher les statistiques",
    font=("Arial", 12),
    command=ouvrir_stats
).pack(pady=20)

root.mainloop()
