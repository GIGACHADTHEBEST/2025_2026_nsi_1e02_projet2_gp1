import tkinter as tk
import random
from math import ceil

# =========================
# ===== STATISTIQUES ======
# =========================

def ouvrir_statistiques():
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

    COULEURS = [
        "#4e79a7", "#f28e2b", "#e15759", "#76b7b2",
        "#59a14f", "#edc949", "#af7aa1", "#ff9da7",
        "#9c755f", "#bab0ab"
    ]

    fen = tk.Toplevel(root)
    fen.title(f"Répartition réelle – {jeu['nom']}")
    fen.geometry("1200x650")

    canvas = tk.Canvas(fen, bg="white")
    canvas.pack(fill="both", expand=True)

    canvas.create_text(
        600, 30,
        text=f"{jeu['nom']} – répartition réelle des issues",
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
            f"Mise totale : {mises:,} €\n"
            f"Gains redistribués : {gains_totaux:,} €\n"
            f"Perte moyenne par ticket : {perte_moyenne:.2f} €"
        ).replace(",", " "),
        anchor="w",
        font=("Arial", 11, "bold"),
        fill="darkred"
    )

    tk.Button(
        fen,
        text="⬅ Retour au menu",
        font=("Arial", 11),
        command=fen.destroy
    ).place(x=20, y=20)


# ==================
# ===== JEU ========
# ==================

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
            resultat_label.config(
                text=f"{n} tickets grattés\nGain : {gain_total} €",
                fg="blue"
            )

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
            text=(
                f"Tickets grattés : {tickets}\n"
                f"Prix total : {depense_totale} €\n"
                f"{net}"
            ),
            fg=couleur
        )

    tk.Label(
        fenetre,
        text="JEU DE TICKETS À GRATTER",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    resultat_label = tk.Label(
        fenetre,
        text="Clique pour gratter",
        font=("Arial", 18),
        fg="blue"
    )
    resultat_label.pack(pady=15)

    frame = tk.Frame(fenetre)
    frame.pack(pady=10)

    tk.Button(
        frame,
        text="Gratter 1 ticket (5 €)",
        bg="#FFD700",
        font=("Arial", 12),
        command=lambda: gratter_n(1)
    ).grid(row=0, column=0, padx=10)

    tk.Button(
        frame,
        text="Gratter 100 tickets (500 €)",
        bg="#FFB347",
        font=("Arial", 12),
        command=lambda: gratter_n(100)
    ).grid(row=0, column=1, padx=10)

    stats_label = tk.Label(
        fenetre,
        text=(
            "Tickets grattés : 0\n"
            "Prix total : 0 €\n"
            "Ni gain ni perte"
        ),
        font=("Arial", 12),
        justify="left"
    )
    stats_label.pack(pady=15)

    tk.Button(
        fenetre,
        text="⬅ Retour au menu",
        font=("Arial", 11),
        command=fenetre.destroy
    ).pack(pady=10)


# =========================
# ===== MENU PRINCIPAL ====
# =========================

root = tk.Tk()
root.title("Menu principal")
root.geometry("400x300")

tk.Label(
    root,
    text="Bienvenue",
    font=("Arial", 18, "bold")
).pack(pady=30)

tk.Button(
    root,
    text="📊 Statistiques",
    font=("Arial", 12),
    width=20,
    command=ouvrir_statistiques
).pack(pady=10)

tk.Button(
    root,
    text="🎟 Jeu à gratter",
    font=("Arial", 12),
    width=20,
    command=ouvrir_jeux
).pack(pady=10)

root.mainloop()
