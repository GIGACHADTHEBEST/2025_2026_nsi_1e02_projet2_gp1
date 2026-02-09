import csv
import tkinter as tk
import random
from math import ceil

# =========================
# ===== IMPORT CSV ========
# =========================

def nettoyer_nombre(texte):
    return int(
        texte
        .replace(" ", "")
        .replace("\u202f", "")  # espace insécable fine
        .replace("\xa0", "")    # espace insécable classique
    )

def charger_jeux_depuis_csv(fichier):
    jeux = {}
    try:
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
                jeux[nom] = {"prix": prix, "tickets": tickets, "gains": gains}
    except FileNotFoundError:
        print("CSV non trouvé, aucun jeu disponible.")
    return jeux

JEUX = charger_jeux_depuis_csv("archi_mvc_projet_jeu_argent/data/jeux.csv")

# =========================
# ===== PARAMÈTRES VISUELS
# =========================

CARRE_PAR_TICKETS = 10_000
TAILLE = 18
MARGE = 4
PAR_LIGNE = 35

COULEURS = [
    "#4e79a7", "#f28e2b", "#e15759", "#76b7b2",
    "#59a14f", "#edc949", "#af7aa1", "#ff9da7",
    "#9c755f", "#bab0ab", "#1f77b4", "#ff7f0e"
]

# =========================
# ===== STATISTIQUES ======
# =========================

def fenetre_stats(nom_jeu, jeu):
    stats = tk.Toplevel(root)
    stats.title(f"Statistiques – {nom_jeu}")
    stats.geometry("1200x650")

    canvas = tk.Canvas(stats, bg="white")
    canvas.pack(fill="both", expand=True)

    canvas.create_text(600, 30, text=f"{nom_jeu} – répartition réelle des issues",
                       font=("Arial", 16, "bold"))

    x0, y0 = 20, 80
    index = 0
    stats_y = 100
    couleur_index = 0

    canvas.create_text(850, 80, text="Statistiques détaillées",
                       font=("Arial", 14, "bold"), anchor="w")

    for gain, nb_tickets in sorted(jeu["gains"].items()):
        couleur = COULEURS[couleur_index % len(COULEURS)]
        couleur_index += 1

        nb_carres = ceil(nb_tickets / CARRE_PAR_TICKETS)
        proba = nb_tickets / jeu["tickets"] * 100
        gain_total = gain * nb_tickets

        for _ in range(nb_carres):
            cx = x0 + (index % PAR_LIGNE) * (TAILLE + MARGE)
            cy = y0 + (index // PAR_LIGNE) * (TAILLE + MARGE)
            canvas.create_rectangle(cx, cy, cx + TAILLE, cy + TAILLE, fill=couleur, outline="")
            index += 1

        canvas.create_rectangle(820, stats_y - 10, 840, stats_y + 10, fill=couleur, outline="")
        canvas.create_text(
            850, stats_y,
            text=(f"Gain {gain} €\n{nb_tickets:,} tickets • {proba:.4f} %\nGains totaux : {gain_total:,} €").replace(",", " "),
            anchor="w", font=("Arial", 10)
        )
        stats_y += 60

    mises = jeu["prix"] * jeu["tickets"]
    gains_totaux = sum(g * n for g, n in jeu["gains"].items())
    perte_moyenne = (mises - gains_totaux) / jeu["tickets"]

    canvas.create_text(
        850, stats_y + 20,
        text=(f"Prix du ticket : {jeu['prix']} €\nMise totale : {mises:,} €\n"
              f"Gains redistribués : {gains_totaux:,} €\nPerte moyenne par ticket : {perte_moyenne:.2f} €").replace(",", " "),
        anchor="w", font=("Arial", 11, "bold"), fill="darkred"
    )

    tk.Button(stats, text="⬅ Retour au menu", font=("Arial", 11), command=stats.destroy).pack(pady=10)

def ouvrir_stats_csv():
    nom = selection.get()
    if nom:
        fenetre_stats(nom, JEUX[nom])

# =========================
# ===== JEU À GRATTER =====
# =========================

PRIX_TICKET = 5

lots = [
    (0, 0.737),
    (5, 0.102),
    (10, 0.119),
    (20, 0.0277),
    (50, 0.0074),
    (100, 0.0074),
    (500, 0.0001),
    (5000, 0.0000004),
    (10000, 0.0000002),
    (100000, 0.0000001),
    (500000, 0.00000016)
]

tickets = 0
argent_net = 0

def ouvrir_jeux():
    global tickets, argent_net

    fenetre = tk.Toplevel(root)
    fenetre.title("Ticket à gratter")
    fenetre.geometry("460x360")
    fenetre.resizable(False, False)

    def gratter_ticket():
        r = random.random()
        cumul = 0
        for gain, proba in lots:
            cumul += proba
            if r <= cumul:
                return gain
        return 0

    def gratter_n(n):
        global tickets, argent_net

        gain_total = 0
        for _ in range(n):
            gain = gratter_ticket()
            gain_total += gain
            argent_net += gain - PRIX_TICKET
            tickets += 1

        if n == 1:
            if gain_total == 0:
                resultat_label.config(text="Perdu\n0 €", fg="red")
            else:
                resultat_label.config(text=f"Gagné\n{gain_total} €", fg="green")
        else:
            resultat_label.config(text=f"{n} tickets grattés\nGain : {gain_total} €", fg="blue")

        depense_totale = tickets * PRIX_TICKET
        if argent_net > 0:
            net = f"Argent gagné : {argent_net} €"
            couleur = "green"
        elif argent_net < 0:
            net = f"Argent perdu : {-argent_net} €"
            couleur = "red"
        else:
            net = "Ni gain ni perte"
            couleur = "black"

        stats_label.config(
            text=f"Tickets grattés : {tickets}\nPrix total : {depense_totale} €\n{net}",
            fg=couleur
        )

    tk.Label(fenetre, text="JEU DE TICKETS À GRATTER", font=("Arial", 16, "bold")).pack(pady=10)
    resultat_label = tk.Label(fenetre, text="Clique pour gratter", font=("Arial", 18), fg="blue")
    resultat_label.pack(pady=15)

    frame = tk.Frame(fenetre)
    frame.pack(pady=10)

    tk.Button(frame, text="Gratter 1 ticket (5 €)", bg="#FFD700", font=("Arial", 12), command=lambda: gratter_n(1)).grid(row=0, column=0, padx=10)
    tk.Button(frame, text="Gratter 100 tickets (500 €)", bg="#FFB347", font=("Arial", 12), command=lambda: gratter_n(100)).grid(row=0, column=1, padx=10)

    stats_label = tk.Label(fenetre, text="Tickets grattés : 0\nPrix total : 0 €\nNi gain ni perte", font=("Arial", 12), justify="left")
    stats_label.pack(pady=15)

    tk.Button(fenetre, text="⬅ Retour au menu", font=("Arial", 11), command=fenetre.destroy).pack(pady=10)

# =========================
# ===== MENU PRINCIPAL =====
# =========================

root = tk.Tk()
root.title("Menu principal")
root.geometry("400x350")

tk.Label(root, text="Bienvenue", font=("Arial", 18, "bold")).pack(pady=20)

# Bouton jeu à gratter
tk.Button(root, text="🎟 Jeu à gratter", font=("Arial", 12), width=25, command=ouvrir_jeux).pack(pady=10)

# Bouton statistiques CSV (si disponible)
if JEUX:
    selection = tk.StringVar()
    menu = tk.OptionMenu(root, selection, *JEUX.keys())
    menu.config(width=25, font=("Arial", 11))
    menu.pack(pady=10)
    tk.Button(root, text="📊 Afficher les statistiques du jeu choisi", font=("Arial", 12), width=25, command=ouvrir_stats_csv).pack(pady=5)
else:
    tk.Label(root, text="Aucun jeu disponible depuis le CSV.", fg="red").pack(pady=20)

root.mainloop()
